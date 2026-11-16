/* ===== X-Mas: PDF per Mail verschicken =======================================
   POST /api/xmas-pdf  { email, datei, firma }
   Schickt das PDF zum gewaehlten Vorsatz von Daniels Postfach an die Adresse.
   Die Mail liegt danach in Daniels Outlook unter "Gesendet" - so sieht er,
   wer was angefordert hat. Keine Datenbank, keine weiteren Felder.

   Versand ueber Microsoft Graph (App-Anmeldung, nur Recht Mail.Send, in
   Exchange auf Daniels Postfach beschraenkt). Zugangsdaten nur als
   Umgebungsvariablen in Vercel:
     XMAS_MANDANT        Verzeichnis-ID (Tenant) der empiria GmbH
     XMAS_CLIENT_ID      Anwendungs-ID der App "empiria Website Versand"
     XMAS_CLIENT_SECRET  geheimer Clientschluessel
     XMAS_ABSENDER       optional, Standard daniel.stroebel@empiria.de

   Schutz gegen Missbrauch: nur die sechs festen PDFs, Honigtopf-Feld "firma",
   Herkunftspruefung, Grenze je Adresse und je IP (pro laufender Instanz). */

const fs = require('fs');
const path = require('path');

const PDF_ORDNER = path.join(__dirname, '..', 'site', 'assets', 'downloads', '2.0');
const DATEIEN = {
  'innovation':                    { titel: 'Innovation & Geschäftsmodell neu denken', datei: 'empiria-innovation.pdf' },
  'strategie':                     { titel: 'Strategie in den Alltag überführen',       datei: 'empiria-strategie.pdf' },
  'ki-zum-anfassen':               { titel: 'KI zum Anfassen',                          datei: 'empiria-ki-zum-anfassen.pdf' },
  'sprint-landingpage':            { titel: 'Sprint Landingpage',                       datei: 'empiria-sprint-landingpage.pdf' },
  'dashboard-digitales-marketing': { titel: 'MarketingEcoSystem (MES)',                 datei: 'empiria-dashboard-digitales-marketing.pdf' },
  'sparring':                      { titel: '1:1 Sparring',                             datei: 'empiria-sparring.pdf' },
};

const ERLAUBTE_HERKUNFT = /^https:\/\/((www\.)?empiria\.de|empiria-[a-z0-9-]+-empiria-gmb-h\.vercel\.app)$/;
const MAIL_MUSTER = /^[^\s@<>"',;]+@[^\s@<>"',;]+\.[a-z]{2,}$/i;

// Grenzen je laufender Instanz - kein Ersatz fuer echte Drosselung, haelt aber
// Wiederholungen aus einem Browser oder Skript im Zaum.
const zaehler = new Map();
function zuViel(schluessel, max, fensterMs) {
  const jetzt = Date.now();
  const liste = (zaehler.get(schluessel) || []).filter(t => jetzt - t < fensterMs);
  liste.push(jetzt);
  zaehler.set(schluessel, liste);
  return liste.length > max;
}

function html(s) {
  return String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

function mailText(titel) {
  const p = 'margin:0 0 14px;font-family:Arial,Helvetica,sans-serif;font-size:11pt;line-height:1.5;color:#1a1817';
  const signatur = fs.readFileSync(path.join(__dirname, '_xmas', 'signatur.html'), 'utf8');
  return `<div>
<p style="${p}">Ein Klick – und schon liegt es unterm Baum. Beziehungsweise in Deinem Postfach: Das PDF zu Deinem Vorsatz „${html(titel)}“.</p>
<p style="${p}">Lust, das gemeinsam ins Rollen zu bringen? Eine kurze Antwort auf diese Mail reicht.</p>
<p style="${p}">Frohe Weihnachten und einen guten Start in 2027</p>
${signatur}
</div>`;
}

async function token() {
  const r = await fetch(`https://login.microsoftonline.com/${process.env.XMAS_MANDANT}/oauth2/v2.0/token`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({
      client_id: process.env.XMAS_CLIENT_ID,
      client_secret: process.env.XMAS_CLIENT_SECRET,
      scope: 'https://graph.microsoft.com/.default',
      grant_type: 'client_credentials',
    }),
  });
  if (!r.ok) throw new Error('Anmeldung bei Microsoft fehlgeschlagen: ' + r.status);
  return (await r.json()).access_token;
}

module.exports = async function handler(req, res) {
  if (req.method !== 'POST') { res.setHeader('Allow', 'POST'); return res.status(405).json({ ok: false }); }

  const herkunft = req.headers.origin || '';
  if (!ERLAUBTE_HERKUNFT.test(herkunft)) return res.status(403).json({ ok: false });

  const body = typeof req.body === 'object' && req.body ? req.body : {};
  const email = String(body.email || '').trim();
  const schluessel = String(body.datei || '');
  const eintrag = Object.prototype.hasOwnProperty.call(DATEIEN, schluessel) ? DATEIEN[schluessel] : null;

  // Honigtopf: Menschen sehen das Feld nicht. Bots bekommen ein "ok" ohne Versand.
  if (body.firma) return res.status(200).json({ ok: true });
  if (!eintrag || email.length > 200 || !MAIL_MUSTER.test(email)) return res.status(400).json({ ok: false });

  const ip = String(req.headers['x-forwarded-for'] || '').split(',')[0].trim() || 'unbekannt';
  if (zuViel('ip:' + ip, 8, 60 * 60 * 1000) || zuViel('mail:' + email.toLowerCase(), 4, 24 * 60 * 60 * 1000)) {
    return res.status(429).json({ ok: false });
  }

  if (!process.env.XMAS_MANDANT || !process.env.XMAS_CLIENT_ID || !process.env.XMAS_CLIENT_SECRET) {
    console.error('[xmas-pdf] Zugangsdaten fehlen in den Umgebungsvariablen');
    return res.status(503).json({ ok: false });
  }

  const absender = process.env.XMAS_ABSENDER || 'daniel.stroebel@empiria.de';
  try {
    const nachricht = {
      message: {
        subject: `Dein Vorsatz für 2027: ${eintrag.titel}`,
        body: { contentType: 'HTML', content: mailText(eintrag.titel) },
        toRecipients: [{ emailAddress: { address: email } }],
        attachments: [
          { '@odata.type': '#microsoft.graph.fileAttachment', name: eintrag.datei,
            contentType: 'application/pdf',
            contentBytes: fs.readFileSync(path.join(PDF_ORDNER, eintrag.datei)).toString('base64') },
          { '@odata.type': '#microsoft.graph.fileAttachment', name: 'doppelpfeil.png',
            contentType: 'image/png', isInline: true, contentId: 'doppelpfeil',
            contentBytes: fs.readFileSync(path.join(__dirname, '_xmas', 'doppelpfeil.png')).toString('base64') },
        ],
      },
      saveToSentItems: true,
    };
    const r = await fetch(`https://graph.microsoft.com/v1.0/users/${encodeURIComponent(absender)}/sendMail`, {
      method: 'POST',
      headers: { Authorization: 'Bearer ' + await token(), 'Content-Type': 'application/json' },
      body: JSON.stringify(nachricht),
    });
    if (!r.ok) throw new Error('Graph sendMail: ' + r.status + ' ' + (await r.text()).slice(0, 300));
    return res.status(200).json({ ok: true });
  } catch (e) {
    console.error('[xmas-pdf]', e.message);
    return res.status(502).json({ ok: false });
  }
};

import sys
from pdf_vorlage import build, icon, head, FOOTER
theme = sys.argv[1] if len(sys.argv)>1 else "magenta"
sketch=open("ws-sketch.svg").read()
p1=f'''<section class="page cover">
  <img src="assets/empiria-logo.svg" alt="empiria" style="height:10mm">
  <p class="kicker">Workshops</p>
  <h1>Workshops, <span class="hl">die wirken.</span><br>Nicht nur Theorie.</h1>
  <p class="sub">Formate aus unzähligen Projekten, die Du direkt buchen kannst – mit echten Tools, echten Ergebnissen und einer Moderation, die Dein Team ans Ziel bringt.</p>
  <div class="sketch">{sketch}</div>
  <div class="facts" style="grid-template-columns:repeat(3,1fr)">
    <div><span class="label">Format 01</span><b>KI zum Anfassen</b></div>
    <div><span class="label">Format 02</span><b>Sprint Landingpage</b></div>
    <div><span class="label">Format 03</span><b>Moderation Deines Workshops</b></div>
  </div>
</section>'''
p2=f'''<section class="page">
  {head(2,3)}
  <p class="kicker">Unser Ansatz</p>
  <h2>Workshops, die nicht bei der Theorie bleiben.</h2>
  <p class="lead">Wir gehen direkt in die Anwendung – mit echten Tools, echten Ergebnissen und einer Moderation, die trägt. Jeder Workshop ist auf einen konkreten Anwendungsfall zugeschnitten.</p>
  <div class="cards" style="grid-template-columns:repeat(3,1fr)">
    <div class="card"><div class="ic">{icon("tool")}</div><h3>Direkt anwendbar</h3><p>Kein Arbeitskreis ohne Praxis: Wir arbeiten mit echten Tools und echten Fällen aus Deinem Alltag.</p></div>
    <div class="card"><div class="ic">{icon("team")}</div><h3>Auf Dein Team zugeschnitten</h3><p>Jeder Workshop passt zu Deinem Anwendungsfall und Deinem Team – nicht von der Stange.</p></div>
    <div class="card"><div class="ic">{icon("target")}</div><h3>Professionell moderiert</h3><p>Klare Strukturen, gute Stimmung und Ergebnisse, mit denen sich weiterarbeiten lässt.</p></div>
  </div>
  <div style="margin-top:14mm">
    <p class="kicker">Unsere Workshops</p>
    <h2>Drei Formate. Ein Ziel: Ergebnisse.</h2>
  </div>
  <div class="rows">
    <div class="row"><span class="n">01</span><div><h3>KI zum Anfassen</h3><p>Über KI wird viel geredet – wir nutzen sie. Wir testen verschiedene KI-Tools an echten Fällen aus der Versicherungsbranche und sorgen für Erkenntnisse, die sofort etwas bringen.</p></div></div>
    <div class="row"><span class="n">02</span><div><h3>Sprint Landingpage</h3><p>Wenn es schnell gehen muss: In nur 48 Stunden entsteht Deine fokussierte Landingpage – eine Zielgruppe, ein Problem, eine Lösung. Ohne Abstriche bei Qualität, Layout und Wirkung.</p></div></div>
    <div class="row"><span class="n">03</span><div><h3>Moderation Deines Workshops</h3><p>Wir aktivieren die Beteiligten, wechseln bewusst die Perspektive und führen alles so zusammen, dass Handlungsklarheit entsteht – mit Ergebnissen, mit denen sich direkt weiterarbeiten lässt.</p></div></div>
  </div>
</section>'''
p3=f'''<section class="page">
  {head(3,3)}
  <p class="kicker">Umfang &amp; Investition</p>
  <h2>Wähle das Format, <span class="hl">das zu Dir passt.</span></h2>
  <div class="detail" style="margin-top:4mm">
    <div class="detail-head"><h3>KI zum Anfassen</h3><p>Vom ersten Ausprobieren bis zum konkreten Usecase</p></div>
    <div class="opts" style="grid-template-columns:repeat(3,1fr)">
      <div class="opt"><b>KI-Einstieg</b><small>½ Tag · Tools ausprobieren</small><span class="price">2.500 €</span></div>
      <div class="opt opt--feat"><b>KI-Sprint</b><small>1 Tag · kompakte Fragestellung</small><span class="price">3.900 €</span></div>
      <div class="opt"><b>KI-Deep-Dive</b><small>2 Tage · konkreter Usecase</small><span class="price">7.350 €</span></div>
    </div>
  </div>
  <div class="detail">
    <div class="detail-head"><h3>Sprint Landingpage</h3><p>Onboarding · 2 Tage Sprint vor Ort · Review</p></div>
    <div class="opts" style="grid-template-columns:2fr 1fr">
      <div class="opt"><b>Leistungspaket</b><small>Konzeption, Text, Design, Umsetzung und Live-Schaltung – durchgeführt von zwei Beraterinnen und Beratern</small></div>
      <div class="opt"><b>Investition</b><small>Ein Paket, ein Preis</small><span class="price">15.850 €</span></div>
    </div>
  </div>
  <div class="detail">
    <div class="detail-head"><h3>Moderation Deines Workshops</h3><p>Umfang und Ablauf nach Deinem Thema</p></div>
    <p style="font-size:9.5pt;line-height:1.6;color:var(--g70)">Von Strukturen, Prozessen und Rollen bis zu Kreativworkshops und Vertriebsansätzen – wir stimmen Umfang und Investition individuell mit Dir ab.</p>
  </div>
  <p class="note">Alle Preise zzgl. Umsatzsteuer in gesetzlicher Höhe und zzgl. Spesen.</p>
  <div class="contact">
    <p class="kicker">Kontakt</p>
    <h2>Bereit für einen Workshop, der Dich wirklich weiterbringt?</h2>
    <div class="people">
      <div class="person"><img src="assets/ansprechpartner-daniel.webp" alt=""><div><b>Daniel Ströbel</b><span>Strategiehandwerker</span></div></div>
      <div class="person"><img src="assets/ansprechpartner-kerstin.webp" alt=""><div><b>Kerstin Christ</b><span>Expertin HR &amp; Weiterbildung</span></div></div>
      <div class="person"><img src="assets/ansprechpartner-noah.webp" alt=""><div><b>Noah Hermanns</b><span>Experte Performance Marketing</span></div></div>
    </div>
    <div class="direct"><span><span class="label">E-Mail</span>daniel.stroebel@empiria.de</span><span><span class="label">Telefon</span>+49 176 3134 7217</span><span><span class="label">Web</span>www.empiria.de</span></div>
  </div>
  {FOOTER}
</section>'''
open(f"workshops-{theme}.html","w",encoding="utf-8").write(build(theme,p1+p2+p3,"Workshops – empiria"))

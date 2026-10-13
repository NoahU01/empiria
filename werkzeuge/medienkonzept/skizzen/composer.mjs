import React from "react";
import { renderToStaticMarkup } from "react-dom/server";
import M1 from "./node_modules/@opeepsfun/open-peeps/build/head/Afro.js";
import M2 from "./node_modules/@opeepsfun/open-peeps/build/head/Bald.js";
import M3 from "./node_modules/@opeepsfun/open-peeps/build/head/Bangs.js";
import M4 from "./node_modules/@opeepsfun/open-peeps/build/head/BangsTwo.js";
import M5 from "./node_modules/@opeepsfun/open-peeps/build/head/BantuKnots.js";
import M6 from "./node_modules/@opeepsfun/open-peeps/build/head/Beanie.js";
import M7 from "./node_modules/@opeepsfun/open-peeps/build/head/Bear.js";
import M8 from "./node_modules/@opeepsfun/open-peeps/build/head/Bun.js";
import M9 from "./node_modules/@opeepsfun/open-peeps/build/head/BunClip.js";
import M10 from "./node_modules/@opeepsfun/open-peeps/build/head/BunKnots.js";
import M11 from "./node_modules/@opeepsfun/open-peeps/build/head/BunTwo.js";
import M12 from "./node_modules/@opeepsfun/open-peeps/build/head/ColorBun.js";
import M13 from "./node_modules/@opeepsfun/open-peeps/build/head/ColorMedium.js";
import M14 from "./node_modules/@opeepsfun/open-peeps/build/head/Cornrows.js";
import M15 from "./node_modules/@opeepsfun/open-peeps/build/head/CornrowsLight.js";
import M16 from "./node_modules/@opeepsfun/open-peeps/build/head/DocOne.js";
import M17 from "./node_modules/@opeepsfun/open-peeps/build/head/DocThree.js";
import M18 from "./node_modules/@opeepsfun/open-peeps/build/head/DocTwo.js";
import M19 from "./node_modules/@opeepsfun/open-peeps/build/head/DreadsOne.js";
import M20 from "./node_modules/@opeepsfun/open-peeps/build/head/DreadsTwo.js";
import M21 from "./node_modules/@opeepsfun/open-peeps/build/head/FlatTop.js";
import M22 from "./node_modules/@opeepsfun/open-peeps/build/head/FlatTopLong.js";
import M23 from "./node_modules/@opeepsfun/open-peeps/build/head/GrayShort.js";
import M24 from "./node_modules/@opeepsfun/open-peeps/build/head/HatHip.js";
import M25 from "./node_modules/@opeepsfun/open-peeps/build/head/Hijab.js";
import M26 from "./node_modules/@opeepsfun/open-peeps/build/head/LongAfro.js";
import M27 from "./node_modules/@opeepsfun/open-peeps/build/head/LongBangs.js";
import M28 from "./node_modules/@opeepsfun/open-peeps/build/head/LongCurly.js";
import M29 from "./node_modules/@opeepsfun/open-peeps/build/head/LongHair.js";
import M30 from "./node_modules/@opeepsfun/open-peeps/build/head/MediumBangs.js";
import M31 from "./node_modules/@opeepsfun/open-peeps/build/head/MediumBangsColor.js";
import M32 from "./node_modules/@opeepsfun/open-peeps/build/head/MediumBangsOne.js";
import M33 from "./node_modules/@opeepsfun/open-peeps/build/head/MediumOne.js";
import M34 from "./node_modules/@opeepsfun/open-peeps/build/head/MediumStraight.js";
import M35 from "./node_modules/@opeepsfun/open-peeps/build/head/MediumThree.js";
import M36 from "./node_modules/@opeepsfun/open-peeps/build/head/MediumTwo.js";
import M37 from "./node_modules/@opeepsfun/open-peeps/build/head/Mohawk.js";
import M38 from "./node_modules/@opeepsfun/open-peeps/build/head/MohawkKnots.js";
import M39 from "./node_modules/@opeepsfun/open-peeps/build/head/NoHairThree.js";
import M40 from "./node_modules/@opeepsfun/open-peeps/build/head/NoHairTwo.js";
import M41 from "./node_modules/@opeepsfun/open-peeps/build/head/Pomp.js";
import M42 from "./node_modules/@opeepsfun/open-peeps/build/head/Shaved.js";
import M43 from "./node_modules/@opeepsfun/open-peeps/build/head/ShavedOne.js";
import M44 from "./node_modules/@opeepsfun/open-peeps/build/head/ShavedThree.js";
import M45 from "./node_modules/@opeepsfun/open-peeps/build/head/ShortFive.js";
import M46 from "./node_modules/@opeepsfun/open-peeps/build/head/ShortFour.js";
import M47 from "./node_modules/@opeepsfun/open-peeps/build/head/ShortOne.js";
import M48 from "./node_modules/@opeepsfun/open-peeps/build/head/ShortThree.js";
import M49 from "./node_modules/@opeepsfun/open-peeps/build/head/ShortTwo.js";
import M50 from "./node_modules/@opeepsfun/open-peeps/build/head/Turban.js";
import M51 from "./node_modules/@opeepsfun/open-peeps/build/head/Twists.js";
import M52 from "./node_modules/@opeepsfun/open-peeps/build/head/TwistsTwo.js";
import M53 from "./node_modules/@opeepsfun/open-peeps/build/head/Wavy.js";
import M54 from "./node_modules/@opeepsfun/open-peeps/build/face/Angry.js";
import M55 from "./node_modules/@opeepsfun/open-peeps/build/face/AngryFang.js";
import M56 from "./node_modules/@opeepsfun/open-peeps/build/face/Awe.js";
import M57 from "./node_modules/@opeepsfun/open-peeps/build/face/BigSmile.js";
import M58 from "./node_modules/@opeepsfun/open-peeps/build/face/Blank.js";
import M59 from "./node_modules/@opeepsfun/open-peeps/build/face/Calm.js";
import M60 from "./node_modules/@opeepsfun/open-peeps/build/face/CalmWithMask.js";
import M61 from "./node_modules/@opeepsfun/open-peeps/build/face/Cheeky.js";
import M62 from "./node_modules/@opeepsfun/open-peeps/build/face/CheersWithMask.js";
import M63 from "./node_modules/@opeepsfun/open-peeps/build/face/Concerned.js";
import M64 from "./node_modules/@opeepsfun/open-peeps/build/face/ConcernedFear.js";
import M65 from "./node_modules/@opeepsfun/open-peeps/build/face/Contempt.js";
import M66 from "./node_modules/@opeepsfun/open-peeps/build/face/Cute.js";
import M67 from "./node_modules/@opeepsfun/open-peeps/build/face/Cyclops.js";
import M68 from "./node_modules/@opeepsfun/open-peeps/build/face/Driven.js";
import M69 from "./node_modules/@opeepsfun/open-peeps/build/face/EatingHappy.js";
import M70 from "./node_modules/@opeepsfun/open-peeps/build/face/Explaining.js";
import M71 from "./node_modules/@opeepsfun/open-peeps/build/face/EyesClosed.js";
import M72 from "./node_modules/@opeepsfun/open-peeps/build/face/Fear.js";
import M73 from "./node_modules/@opeepsfun/open-peeps/build/face/Hectic.js";
import M74 from "./node_modules/@opeepsfun/open-peeps/build/face/LoveGrinTeeth.js";
import M75 from "./node_modules/@opeepsfun/open-peeps/build/face/LoveGrinTongue.js";
import M76 from "./node_modules/@opeepsfun/open-peeps/build/face/Monster.js";
import M77 from "./node_modules/@opeepsfun/open-peeps/build/face/Old.js";
import M78 from "./node_modules/@opeepsfun/open-peeps/build/face/Rage.js";
import M79 from "./node_modules/@opeepsfun/open-peeps/build/face/Serious.js";
import M80 from "./node_modules/@opeepsfun/open-peeps/build/face/Smile.js";
import M81 from "./node_modules/@opeepsfun/open-peeps/build/face/SmileLOL.js";
import M82 from "./node_modules/@opeepsfun/open-peeps/build/face/SmileTeeth.js";
import M83 from "./node_modules/@opeepsfun/open-peeps/build/face/SmileWithMask.js";
import M84 from "./node_modules/@opeepsfun/open-peeps/build/face/Solemn.js";
import M85 from "./node_modules/@opeepsfun/open-peeps/build/face/Suspicious.js";
import M86 from "./node_modules/@opeepsfun/open-peeps/build/face/Tired.js";
import M87 from "./node_modules/@opeepsfun/open-peeps/build/beard/Chin.js";
import M88 from "./node_modules/@opeepsfun/open-peeps/build/beard/Full.js";
import M89 from "./node_modules/@opeepsfun/open-peeps/build/beard/FullColor.js";
import M90 from "./node_modules/@opeepsfun/open-peeps/build/beard/FullMax.js";
import M91 from "./node_modules/@opeepsfun/open-peeps/build/beard/FullMedium.js";
import M92 from "./node_modules/@opeepsfun/open-peeps/build/beard/Goatee.js";
import M93 from "./node_modules/@opeepsfun/open-peeps/build/beard/GoateeFull.js";
import M94 from "./node_modules/@opeepsfun/open-peeps/build/beard/MustacheBull.js";
import M95 from "./node_modules/@opeepsfun/open-peeps/build/beard/MustacheEight.js";
import M96 from "./node_modules/@opeepsfun/open-peeps/build/beard/MustacheFive.js";
import M97 from "./node_modules/@opeepsfun/open-peeps/build/beard/MustacheNine.js";
import M98 from "./node_modules/@opeepsfun/open-peeps/build/beard/MustacheSeven.js";
import M99 from "./node_modules/@opeepsfun/open-peeps/build/beard/MustacheSix.js";
import M100 from "./node_modules/@opeepsfun/open-peeps/build/beard/MustacheThin.js";
import M101 from "./node_modules/@opeepsfun/open-peeps/build/beard/MustacheThinBull.js";
import M102 from "./node_modules/@opeepsfun/open-peeps/build/beard/MustacheYosemite.js";
import M103 from "./node_modules/@opeepsfun/open-peeps/build/accessory/Eyepatch.js";
import M104 from "./node_modules/@opeepsfun/open-peeps/build/accessory/Glasses.js";
import M105 from "./node_modules/@opeepsfun/open-peeps/build/accessory/GlassesFive.js";
import M106 from "./node_modules/@opeepsfun/open-peeps/build/accessory/GlassesFour.js";
import M107 from "./node_modules/@opeepsfun/open-peeps/build/accessory/GlassesSix.js";
import M108 from "./node_modules/@opeepsfun/open-peeps/build/accessory/GlassesThree.js";
import M109 from "./node_modules/@opeepsfun/open-peeps/build/accessory/GlassesTwo.js";
import M110 from "./node_modules/@opeepsfun/open-peeps/build/accessory/Sunglasses.js";
import M111 from "./node_modules/@opeepsfun/open-peeps/build/accessory/SunglassesTwo.js";
import M112 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/BlazerBlackTee.js";
import M113 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/ButtonPocketShirt.js";
import M114 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/ButtonShirt.js";
import M115 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/Coffee.js";
import M116 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/Computer.js";
import M117 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/Dress.js";
import M118 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/Explaining.js";
import M119 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/Gaming.js";
import M120 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/GymShirt.js";
import M121 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/Hoodie.js";
import M122 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/Jacket.js";
import M123 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/Killer.js";
import M124 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/Paper.js";
import M125 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/PointingUp.js";
import M126 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/PolkadotJacket.js";
import M127 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/PoloSweater.js";
import M128 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/ShirtCoat.js";
import M129 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/SportyTee.js";
import M130 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/StripedTee.js";
import M131 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/StrippedPocketTee.js";
import M132 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/SweaterDots.js";
import M133 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/Tee.js";
import M134 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/TeeArmsCrossed.js";
import M135 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/TeeSelena.js";
import M136 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/ThunderTee.js";
import M137 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/Turtleneck.js";
import M138 from "./node_modules/@opeepsfun/open-peeps/build/body/effigy/Whatever.js";
const REG = {"head/Afro": M1,"head/Bald": M2,"head/Bangs": M3,"head/BangsTwo": M4,"head/BantuKnots": M5,"head/Beanie": M6,"head/Bear": M7,"head/Bun": M8,"head/BunClip": M9,"head/BunKnots": M10,"head/BunTwo": M11,"head/ColorBun": M12,"head/ColorMedium": M13,"head/Cornrows": M14,"head/CornrowsLight": M15,"head/DocOne": M16,"head/DocThree": M17,"head/DocTwo": M18,"head/DreadsOne": M19,"head/DreadsTwo": M20,"head/FlatTop": M21,"head/FlatTopLong": M22,"head/GrayShort": M23,"head/HatHip": M24,"head/Hijab": M25,"head/LongAfro": M26,"head/LongBangs": M27,"head/LongCurly": M28,"head/LongHair": M29,"head/MediumBangs": M30,"head/MediumBangsColor": M31,"head/MediumBangsOne": M32,"head/MediumOne": M33,"head/MediumStraight": M34,"head/MediumThree": M35,"head/MediumTwo": M36,"head/Mohawk": M37,"head/MohawkKnots": M38,"head/NoHairThree": M39,"head/NoHairTwo": M40,"head/Pomp": M41,"head/Shaved": M42,"head/ShavedOne": M43,"head/ShavedThree": M44,"head/ShortFive": M45,"head/ShortFour": M46,"head/ShortOne": M47,"head/ShortThree": M48,"head/ShortTwo": M49,"head/Turban": M50,"head/Twists": M51,"head/TwistsTwo": M52,"head/Wavy": M53,"face/Angry": M54,"face/AngryFang": M55,"face/Awe": M56,"face/BigSmile": M57,"face/Blank": M58,"face/Calm": M59,"face/CalmWithMask": M60,"face/Cheeky": M61,"face/CheersWithMask": M62,"face/Concerned": M63,"face/ConcernedFear": M64,"face/Contempt": M65,"face/Cute": M66,"face/Cyclops": M67,"face/Driven": M68,"face/EatingHappy": M69,"face/Explaining": M70,"face/EyesClosed": M71,"face/Fear": M72,"face/Hectic": M73,"face/LoveGrinTeeth": M74,"face/LoveGrinTongue": M75,"face/Monster": M76,"face/Old": M77,"face/Rage": M78,"face/Serious": M79,"face/Smile": M80,"face/SmileLOL": M81,"face/SmileTeeth": M82,"face/SmileWithMask": M83,"face/Solemn": M84,"face/Suspicious": M85,"face/Tired": M86,"beard/Chin": M87,"beard/Full": M88,"beard/FullColor": M89,"beard/FullMax": M90,"beard/FullMedium": M91,"beard/Goatee": M92,"beard/GoateeFull": M93,"beard/MustacheBull": M94,"beard/MustacheEight": M95,"beard/MustacheFive": M96,"beard/MustacheNine": M97,"beard/MustacheSeven": M98,"beard/MustacheSix": M99,"beard/MustacheThin": M100,"beard/MustacheThinBull": M101,"beard/MustacheYosemite": M102,"accessory/Eyepatch": M103,"accessory/Glasses": M104,"accessory/GlassesFive": M105,"accessory/GlassesFour": M106,"accessory/GlassesSix": M107,"accessory/GlassesThree": M108,"accessory/GlassesTwo": M109,"accessory/Sunglasses": M110,"accessory/SunglassesTwo": M111,"body/effigy/BlazerBlackTee": M112,"body/effigy/ButtonPocketShirt": M113,"body/effigy/ButtonShirt": M114,"body/effigy/Coffee": M115,"body/effigy/Computer": M116,"body/effigy/Dress": M117,"body/effigy/Explaining": M118,"body/effigy/Gaming": M119,"body/effigy/GymShirt": M120,"body/effigy/Hoodie": M121,"body/effigy/Jacket": M122,"body/effigy/Killer": M123,"body/effigy/Paper": M124,"body/effigy/PointingUp": M125,"body/effigy/PolkadotJacket": M126,"body/effigy/PoloSweater": M127,"body/effigy/ShirtCoat": M128,"body/effigy/SportyTee": M129,"body/effigy/StripedTee": M130,"body/effigy/StrippedPocketTee": M131,"body/effigy/SweaterDots": M132,"body/effigy/Tee": M133,"body/effigy/TeeArmsCrossed": M134,"body/effigy/TeeSelena": M135,"body/effigy/ThunderTee": M136,"body/effigy/Turtleneck": M137,"body/effigy/Whatever": M138};

var Effigy = function (_a) {
    var style = _a.style, body = _a.body, head = _a.head, face = _a.face, beard = _a.beard, mask = _a.mask, accessory = _a.accessory;
    return (React.createElement("svg", { style: style, xmlns: 'http://www.w3.org/2000/svg', viewBox: '184.21621621621625 210.7874999999999 940.2702702702704 1130.5875', overflow: 'visible', width: '940.2702702702704px', height: '1130.5875px' },
        React.createElement("g", { id: 'Bust' },
            React.createElement("g", { id: 'Body', transform: 'translate(147, 639) scale(1 1)' }, createBody(body)),
            createHead(body, React.createElement(React.Fragment, null,
                React.createElement("g", { id: 'Hair', transform: 'translate(342, 190) scale(1 1)' }, createHair(head)),
                React.createElement("g", { id: 'Face', transform: 'translate(531, 366) scale(1 1)' }, createFace(face)),
                React.createElement("g", { id: 'Beard', transform: 'translate(495, 518) scale(1 1)' }, createBeard(beard)),
                React.createElement("g", { id: 'Mask', transform: 'translate(400, 480) scale(1 1)' }),
                React.createElement("g", { id: 'Accessories', transform: 'translate(419, 421) scale(1 1)' }, createAccessory(accessory)))))));
};
var createHair = function (head) {
    var _a;
    if (!head) {
        return null;
    }
    var element = (_a = REG["head/" + head.type]) === null || _a === void 0 ? void 0 : (_a.default || _a);
    var reactElement = React.createElement(element, head.options);
    if (head.type === "Bald") {
        return React.createElement("g", { transform: 'translate(50 20)' }, reactElement);
    }
    if (head.type === "BangsTwo") {
        return React.createElement("g", { transform: 'translate(20 0)' }, reactElement);
    }
    if (head.type === "BantuKnots") {
        return React.createElement("g", { transform: 'translate(30 0)' }, reactElement);
    }
    if (head.type === "Bear") {
        return React.createElement("g", { transform: 'translate(20 0)' }, reactElement);
    }
    if (head.type === "Bun") {
        return React.createElement("g", { transform: 'translate(-20 -30)' }, reactElement);
    }
    if (head.type === "Beanie") {
        return React.createElement("g", { transform: 'translate(20 0)' }, reactElement);
    }
    if (head.type === "BunClip") {
        return React.createElement("g", { transform: 'translate(20 -70)' }, reactElement);
    }
    if (head.type === "BunKnots") {
        return React.createElement("g", { transform: 'translate(10 -30)' }, reactElement);
    }
    if (head.type === "BunTwo") {
        return React.createElement("g", { transform: 'translate(-50 -90)' }, reactElement);
    }
    if (head.type === "ColorMedium") {
        return React.createElement("g", { transform: 'translate(30 0)' }, reactElement);
    }
    if (head.type === "CornrowsLight") {
        return React.createElement("g", { transform: 'translate(-15 0)' }, reactElement);
    }
    if (head.type === "DreadsTwo") {
        return React.createElement("g", { transform: 'translate(0 -15)' }, reactElement);
    }
    if (head.type === "FlatTop") {
        return React.createElement("g", { transform: 'translate(50 0)' }, reactElement);
    }
    if (head.type === "FlatTopLong") {
        return React.createElement("g", { transform: 'translate(50 0)' }, reactElement);
    }
    if (head.type === "GrayShort") {
        return React.createElement("g", { transform: 'translate(40 0)' }, reactElement);
    }
    if (head.type === "HatHip") {
        return React.createElement("g", { transform: 'translate(-30 0)' }, reactElement);
    }
    if (head.type === "Hijab") {
        return React.createElement("g", { transform: 'translate(50 20)' }, reactElement);
    }
    if (head.type === "LongAfro") {
        return React.createElement("g", { transform: 'translate(-100 -130)' }, reactElement);
    }
    if (head.type === "LongBangs") {
        return React.createElement("g", { transform: 'translate(-25 0)' }, reactElement);
    }
    if (head.type === "LongCurly") {
        return React.createElement("g", { transform: 'translate(-50 -40)' }, reactElement);
    }
    if (head.type === "LongHair") {
        return React.createElement("g", { transform: 'translate(-50 0)' }, reactElement);
    }
    if (head.type === "MediumBangs") {
        return React.createElement("g", { transform: 'translate(-50 0)' }, reactElement);
    }
    if (head.type === "MediumBangsColor") {
        return React.createElement("g", { transform: 'translate(-20 0)' }, reactElement);
    }
    if (head.type === "MediumBangsOne") {
        return React.createElement("g", { transform: 'translate(40 10)' }, reactElement);
    }
    if (head.type === "MediumOne") {
        return React.createElement("g", { transform: 'translate(40 10)' }, reactElement);
    }
    if (head.type === "MediumStraight") {
        return React.createElement("g", { transform: 'translate(40 0)' }, reactElement);
    }
    if (head.type === "MediumTwo") {
        return React.createElement("g", { transform: 'translate(-20 0)' }, reactElement);
    }
    if (head.type === "Mohawk") {
        return React.createElement("g", { transform: 'translate(40 0)' }, reactElement);
    }
    if (head.type === "MohawkKnots") {
        return React.createElement("g", { transform: 'translate(40 0)' }, reactElement);
    }
    if (head.type === "NoHairThree") {
        return React.createElement("g", { transform: 'translate(30 0)' }, reactElement);
    }
    if (head.type === "NoHairTwo") {
        return React.createElement("g", { transform: 'translate(30 0)' }, reactElement);
    }
    if (head.type === "Pomp") {
        return React.createElement("g", { transform: 'translate(40 0)' }, reactElement);
    }
    if (head.type === "Shaved") {
        return React.createElement("g", { transform: 'translate(40 0)' }, reactElement);
    }
    if (head.type === "ShavedOne") {
        return React.createElement("g", { transform: 'translate(40 0)' }, reactElement);
    }
    if (head.type === "ShavedThree") {
        return React.createElement("g", { transform: 'translate(10 -20)' }, reactElement);
    }
    if (head.type === "ShortFive") {
        return React.createElement("g", { transform: 'translate(40 -10)' }, reactElement);
    }
    if (head.type === "ShortFour") {
        return React.createElement("g", { transform: 'translate(40 -10)' }, reactElement);
    }
    if (head.type === "ShortOne") {
        return React.createElement("g", { transform: 'translate(40 -10)' }, reactElement);
    }
    if (head.type === "ShortThree") {
        return React.createElement("g", { transform: 'translate(40 0)' }, reactElement);
    }
    if (head.type === "ShortTwo") {
        return React.createElement("g", { transform: 'translate(40 0)' }, reactElement);
    }
    if (head.type === "Turban") {
        return React.createElement("g", { transform: 'translate(40 0)' }, reactElement);
    }
    if (head.type === "Twists") {
        return React.createElement("g", { transform: 'translate(40 0)' }, reactElement);
    }
    if (head.type === "TwistsTwo") {
        return React.createElement("g", { transform: 'translate(40 0)' }, reactElement);
    }
    if (head.type === "Wavy") {
        return React.createElement("g", { transform: 'translate(40 0)' }, reactElement);
    }
    return reactElement;
};
var createFace = function (face) {
    var _a;
    var element = (_a = REG["face/" + face.type]) === null || _a === void 0 ? void 0 : (_a.default || _a);
    var reactElement = React.createElement(element, face.options);
    return reactElement;
};
var createBody = function (body) {
    var _a;
    var element = (_a = REG["body/effigy/" + body.type]) === null || _a === void 0 ? void 0 : (_a.default || _a);
    var reactElement = React.createElement(element, body.options);
    return reactElement;
};
var createBeard = function (beard) {
    var _a;
    if (!beard) {
        return null;
    }
    var element = (_a = REG["beard/" + beard.type]) === null || _a === void 0 ? void 0 : (_a.default || _a);
    var reactElement = React.createElement(element, beard.options);
    if (beard.type === "FullColor") {
        return React.createElement("g", { transform: 'translate(0 -20) scale(0.94 0.97)' }, reactElement);
    }
    if (beard.type === "FullMax") {
        return React.createElement("g", { transform: 'translate(0 -20) scale(0.98 1)' }, reactElement);
    }
    if (beard.type === "FullMedium") {
        return React.createElement("g", { transform: 'translate(0 -10) scale(0.98 1)' }, reactElement);
    }
    if (beard.type === "MustacheBull") {
        return React.createElement("g", { transform: 'translate(0 -20)' }, reactElement);
    }
    if (beard.type === "MustacheEight") {
        return React.createElement("g", { transform: 'translate(-240 -75)' }, reactElement);
    }
    return reactElement;
};
var createAccessory = function (accessory) {
    var _a;
    if (!accessory) {
        return null;
    }
    var element = (_a = REG["accessory/" + accessory.type]) === null || _a === void 0 ? void 0 : (_a.default || _a);
    var reactElement = React.createElement(element, accessory.options);
    if (accessory.type === "Eyepatch") {
        return React.createElement("g", { transform: 'translate(0 -60)' }, reactElement);
    }
    if (accessory.type === "SunglassesTwo") {
        return React.createElement("g", { transform: 'translate(-10 0)' }, reactElement);
    }
    return reactElement;
};
var createHead = function (body, children) {
    var group = (React.createElement("g", { id: 'Head', transform: 'translate(0 0)' }, children));
    if (body.type === "Explaining") {
        return React.createElement("g", { transform: 'translate(0 30)' }, group);
    }
    if (body.type === "PointingUp") {
        return React.createElement("g", { transform: 'translate(0 30)' }, group);
    }
    if (body.type === "PolkadotJacket") {
        return React.createElement("g", { transform: 'translate(0 20)' }, group);
    }
    if (body.type === "Killer") {
        return React.createElement("g", { transform: 'translate(0 10)' }, group);
    }
    if (body.type === "StrippedPocketTee") {
        return React.createElement("g", { transform: 'translate(250 0)' }, group);
    }
    if (body.type === "Whatever") {
        return React.createElement("g", { transform: 'translate(90 0)' }, group);
    }
    return group;
};

const a = process.argv.slice(2); const [body, head, face, top, beard] = a;
const opt = { skinColor: "#ffffff", outlineColor: "#1a1817", topColor: top || "#ffffff", hairColor: "#1a1817", bodyColor: top || "#ffffff", accessoryColor: "#1a1817" };
process.stdout.write(renderToStaticMarkup(React.createElement(Effigy, { body: { type: body, options: opt }, head: { type: head, options: opt }, face: { type: face, options: opt }, beard: beard ? { type: beard, options: opt } : undefined })));

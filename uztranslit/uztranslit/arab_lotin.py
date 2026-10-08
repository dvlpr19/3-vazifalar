"""Arab yozuvidagi so'zlarni o'zbek lotin yozuviga o'girish (qoidalar: QOIDALAR.md)."""

import re
import unicodedata

TUTUQ = "ʼ"

# Undoshlar jadvali. Kontekstga bog'liq harflar (ا, ى, ة, hamza, و, ي, ع) alohida ko'riladi.
JADVAL = {
    "ب": "b", "ت": "t", "ث": "s", "ج": "j", "ح": "h", "خ": "x", "د": "d",
    "ذ": "z", "ر": "r", "ز": "z", "س": "s", "ش": "sh", "ص": "s", "ض": "z",
    "ط": "t", "ظ": "z", "ع": TUTUQ, "غ": "gʻ", "ف": "f", "ق": "q", "ك": "k",
    "ل": "l", "م": "m", "ن": "n", "ه": "h", "و": "v", "ي": "y",
}

# Hamza va uning kursilari. Qiymati — harakat qo'yilmagan bo'lsa o'qiladigan unli.
HAMZALAR = {"ء": "", "أ": "a", "إ": "i", "آ": "o", "ؤ": "", "ئ": ""}

SHADDA = "ّ"
KICHIK_ALIF = "ٰ"
HARAKATLAR = {
    "َ": "a",   # fatha
    "ِ": "i",   # kasra
    "ُ": "u",   # damma
    "ً": "an",  # tanvin fatha
    "ٍ": "in",  # tanvin kasra
    "ٌ": "un",  # tanvin damma
    "ْ": "",    # sukun
    KICHIK_ALIF: "o",
}

# (harakat, keyingi harakatsiz harf) -> cho'ziq unli: كِتَاب -> kitob, مُوسَى -> muso
CHOZIQ = {
    ("a", "ا"): "o", ("a", "ى"): "o",
    ("i", "ي"): "i",
    ("u", "و"): "u",
    ("an", "ا"): "an", ("an", "ى"): "an",
}

QUYOSH_HARFLARI = set("تثدذرزسشصضطظلن")

MAXSUS_SOZLAR = {
    "الله": "Alloh",
    "و": "va",
}

# Fors harflari arabcha shakliga, alif vasla oddiy alifga keltiriladi
ALMASHTIRISH = str.maketrans({"ک": "ك", "ی": "ي", "ٱ": "ا"})
# Tatvil (ـ) va Qur'on matnidagi qo'shimcha belgilar o'qilmaydi
KERAKSIZ = re.compile(r"[ـٓ-ٟۖ-ۭ]")

BELGILAR = str.maketrans({
    "،": ",", "؛": ";", "؟": "?",
    **{chr(0x0660 + i): str(i) for i in range(10)},  # arab raqamlari
    **{chr(0x06f0 + i): str(i) for i in range(10)},  # fors raqamlari
})

SOZ = re.compile(r"[ء-غـ-ٰٟٱکیۖ-ۭ]+")


def _harakatsiz(soz):
    """Harflarni harakatlarsiz qaytaradi: اللّٰهِ -> الله."""
    return "".join(b for b in soz if b not in HARAKATLAR and b != SHADDA)


def _bolaklar(soz):
    """So'zni [harf, harakatlar] juftliklariga ajratadi."""
    bolaklar = []
    for belgi in soz:
        if (belgi in HARAKATLAR or belgi == SHADDA) and bolaklar:
            bolaklar[-1][1] += belgi
        elif belgi not in HARAKATLAR and belgi != SHADDA:
            bolaklar.append([belgi, ""])
    return bolaklar


def _unli(harakatlar):
    """Harf ustidagi unlini qaytaradi; harakat umuman bo'lmasa None (sukun — "")."""
    if KICHIK_ALIF in harakatlar:
        return "o"
    for belgi in harakatlar:
        if belgi in HARAKATLAR:
            return HARAKATLAR[belgi]
    return None


def _oqish(bolaklar):
    """Harf-harakat juftliklarini lotin yozuviga o'giradi."""
    natija = []
    i = 0
    while i < len(bolaklar):
        harf, harakatlar = bolaklar[i]
        boshida = i == 0
        oxirida = i == len(bolaklar) - 1
        unli = _unli(harakatlar)

        # Cho'ziq unli: keyingi ا / ى / و / ي o'qilmaydi, faqat unlini cho'zadi
        if not oxirida:
            keyingi, keyingi_harakat = bolaklar[i + 1]
            if (unli, keyingi) in CHOZIQ and not _unli(keyingi_harakat) \
                    and SHADDA not in keyingi_harakat:
                unli = CHOZIQ[(unli, keyingi)]
                i += 1

        if harf == "ا":
            # So'z boshida — harakatdagi unli, o'rtada — harakatsiz cho'ziq "o"
            undosh, unli = "", (unli or "a") if boshida else "o"
        elif harf == "ى":
            undosh, unli = "", "o"
        elif harf == "ة":
            if unli:
                # Harakatli ta marbuta "t" deb o'qiladi: رَحْمَةُ -> rahmatu
                undosh = "t"
            else:
                # To'xtab o'qishda "a": فَاطِمَة -> fotima (fatha "a"sini takrorlamaymiz)
                undosh, unli = "", "" if "".join(natija).endswith("a") else "a"
        elif harf in HAMZALAR:
            undosh = "" if boshida else TUTUQ
            if harf == "آ" or unli is None:
                unli = HAMZALAR[harf]
        elif harf in "وي" and not boshida and unli is None and SHADDA not in harakatlar:
            # Harakatsiz va/yo so'z o'rtasida cho'ziq unli: harakatsiz matn uchun
            undosh, unli = "", "u" if harf == "و" else "i"
        elif harf == "ع" and boshida:
            undosh = ""
        else:
            undosh = JADVAL.get(harf, harf)

        # So'z oxiridagi shadda ikkilanmaydi: حَقّ -> haq
        if SHADDA in harakatlar and not oxirida:
            undosh *= 2
        natija.append(undosh + (unli or ""))
        i += 1

    return "".join(natija)


def _soz(moslik):
    soz = KERAKSIZ.sub("", unicodedata.normalize("NFC", moslik.group(0)))
    soz = soz.translate(ALMASHTIRISH)

    harflar = _harakatsiz(soz)
    if harflar in MAXSUS_SOZLAR:
        return MAXSUS_SOZLAR[harflar]

    bolaklar = _bolaklar(soz)
    # "al-" artikli: الْقَمَر -> al-qamar, الشَّمْس -> ash-shams
    if len(bolaklar) > 2 and bolaklar[0][0] == "ا" and bolaklar[1][0] == "ل":
        qolgani = bolaklar[2:]
        birinchi, harakatlar = qolgani[0]
        if birinchi in QUYOSH_HARFLARI:
            # Shadda artikl hisobiga yoziladi, so'zning o'zida qayta ikkilanmaydi
            qolgani[0] = [birinchi, harakatlar.replace(SHADDA, "")]
            return "a" + JADVAL[birinchi] + "-" + _oqish(qolgani)
        return "al-" + _oqish(qolgani)

    return _oqish(bolaklar)


def arab_lotin(matn):
    """Arab yozuvidagi so'zlarni o'zbek lotin yozuviga o'giradi.

    To'g'ri natija uchun matn harakatli bo'lishi kerak (QOIDALAR.md, "Cheklovlar").

    >>> arab_lotin("مُحَمَّد")
    'muhammad'
    """
    return SOZ.sub(_soz, matn).translate(BELGILAR)

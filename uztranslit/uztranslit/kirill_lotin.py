"""O'zbek kirill yozuvidan lotin yozuviga o'girish (1995-yilgi imlo qoidalari)."""

import re

# Oddiy harflar jadvali. Kontekstga bog'liq harflar (е, ц) alohida ko'riladi.
JADVAL = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "ё": "yo", "ж": "j",
    "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m", "н": "n",
    "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f",
    "х": "x", "ч": "ch", "ш": "sh", "ъ": "ʼ", "ь": "", "э": "e", "ю": "yu",
    "я": "ya", "ў": "oʻ", "қ": "q", "ғ": "gʻ", "ҳ": "h",
}

UNLILAR = set("аеёиоуэюяў")
SOZ = re.compile(r"[а-яёўқғҳ]+", re.IGNORECASE)


def _harf(soz, i):
    """So'zning i-harfini lotin yozuvida qaytaradi (kichik harflarda)."""
    harf = soz[i].lower()
    oldingi = soz[i - 1].lower() if i > 0 else ""

    if harf == "е":
        # So'z boshida, unli yoki ъ/ь dan keyin "ye" bo'ladi: ер -> yer, поезд -> poyezd
        if i == 0 or oldingi in UNLILAR or oldingi in "ъь":
            return "ye"
        return "e"
    if harf == "ц":
        # Unlidan keyin "ts", qolgan holatlarda "s": милиция -> militsiya, цирк -> sirk
        if i > 0 and oldingi in UNLILAR:
            return "ts"
        return "s"
    return JADVAL.get(harf, harf)


def _soz(moslik):
    soz = moslik.group(0)
    natija = []
    for i, belgi in enumerate(soz):
        lotin = _harf(soz, i)
        if belgi.isupper() and lotin:
            lotin = lotin[0].upper() + lotin[1:]
        natija.append(lotin)

    lotin_soz = "".join(natija)
    # Butun so'z bosh harflarda bo'lsa (ТОШКЕНТ), natija ham bosh harflarda
    if len(soz) > 1 and soz.isupper():
        lotin_soz = lotin_soz.upper()
    return lotin_soz


def kirill_lotin(matn):
    """Kirill yozuvidagi matnni lotin yozuviga o'giradi.

    >>> kirill_lotin("Ўзбекистон")
    'Oʻzbekiston'
    """
    return SOZ.sub(_soz, matn)

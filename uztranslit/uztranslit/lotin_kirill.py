"""O'zbek lotin yozuvidan kirill yozuviga o'girish."""

# Apostrofning amalda uchraydigan barcha ko'rinishlari
APOSTROFLAR = "ʻʼ'‘’`"

# Ikki harfli birikmalar birinchi tekshiriladi
BIRIKMALAR = {
    "sh": "ш", "ch": "ч", "yo": "ё", "yu": "ю", "ya": "я", "ye": "е",
}

JADVAL = {
    "a": "а", "b": "б", "d": "д", "e": "е", "f": "ф", "g": "г", "h": "ҳ",
    "i": "и", "j": "ж", "k": "к", "l": "л", "m": "м", "n": "н", "o": "о",
    "p": "п", "q": "қ", "r": "р", "s": "с", "t": "т", "u": "у", "v": "в",
    "x": "х", "y": "й", "z": "з",
}


def _katta(manba, natija):
    """Manba harfi bosh harf bo'lsa, natijani ham bosh harf qiladi."""
    return natija.upper() if manba[:1].isupper() else natija


def lotin_kirill(matn):
    """Lotin yozuvidagi matnni kirill yozuviga o'giradi.

    >>> lotin_kirill("Oʻzbekiston")
    'Ўзбекистон'
    """
    natija = []
    i = 0
    while i < len(matn):
        belgi = matn[i]
        kichik = belgi.lower()
        keyingi = matn[i + 1] if i + 1 < len(matn) else ""

        # oʻ va gʻ
        if kichik in "og" and keyingi and keyingi in APOSTROFLAR:
            natija.append(_katta(belgi, "ў" if kichik == "o" else "ғ"))
            i += 2
            continue

        # Tutuq belgisi: maʼno -> маъно
        if belgi in APOSTROFLAR:
            natija.append("ъ")
            i += 1
            continue

        ikki = matn[i:i + 2].lower()
        if ikki in BIRIKMALAR:
            natija.append(_katta(belgi, BIRIKMALAR[ikki]))
            i += 2
            continue

        # So'z boshidagi "e" -> "э": ekran -> экран
        if kichik == "e" and (i == 0 or not matn[i - 1].isalpha()):
            natija.append(_katta(belgi, "э"))
            i += 1
            continue

        if kichik in JADVAL:
            natija.append(_katta(belgi, JADVAL[kichik]))
        else:
            natija.append(belgi)
        i += 1

    return "".join(natija)

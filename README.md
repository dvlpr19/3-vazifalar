# 3-vazifa: uztranslit — arab yozuvidan o'zbek lotin yozuviga o'girish

**Ism-familiya:** Ermamatov Nurullokh
**Sana:** 08.10.2026
**AI chat tarixi:** `ai-chat-tarixi.md` (Claude Code sessiyasi, uchala vazifa bitta suhbatda)

Mavjud `uztranslit` kutubxonasiga (kirill ↔ lotin) yangi imkoniyat qo'shildi:
**arab yozuvidagi so'zlarni o'zbek lotin yozuviga o'girish** (ismlar, diniy atamalar, iboralar).

```bash
cd uztranslit
python -m uztranslit.cli --from arab "السَّلَامُ عَلَيْكُمْ"   # as-salomu alaykum
python -m unittest -v                                      # 32 ta test
```

## Nima qilindi

| Topshiriq | Fayl |
|---|---|
| 1. Qoidalar jadvali | [`uztranslit/QOIDALAR.md`](uztranslit/QOIDALAR.md) |
| 2. `arab_lotin(matn)` funksiyasi, `__init__.py` ga qo'shildi | [`uztranslit/uztranslit/arab_lotin.py`](uztranslit/uztranslit/arab_lotin.py) |
| 3. CLI'da `--from arab` | [`uztranslit/uztranslit/cli.py`](uztranslit/uztranslit/cli.py) |
| 4. Testlar (18 ta test metodi, 56 ta holat) | [`uztranslit/tests/test_arab_lotin.py`](uztranslit/tests/test_arab_lotin.py) |
| 5. Eski testlar o'zgarmadi va o'tadi (14 ta) | `tests/test_kirill_lotin.py`, `tests/test_lotin_kirill.py` |
| 6. Loyiha uslubi | pastda |

Mavjud kodga o'zgarish minimal: `__init__.py` va `cli.py` ga 1–3 qatordan, `README.md` ga misol va havola.
Birinchi commit — o'zgartirilmagan boshlang'ich kod, shuning uchun `git log -p` da har bir o'zgarish ko'rinadi.

## Asosiy qoidalar (qisqacha)

To'liq jadval — [QOIDALAR.md](uztranslit/QOIDALAR.md). O'zbek diniy adabiyotidagi an'anaviy yozilishga tayanildi:

| Arabcha | Lotin | Misol |
|---|---|---|
| ع | ʼ (so'z boshida yozilmaydi) | سَعْد → saʼd, عُمَر → umar |
| ح / ق / غ / خ | h / q / gʻ / x | حَسَن → hasan, قُرْآن → qurʼon, غَفُور → gʻafur, خَالِد → xolid |
| cho'ziq ā (ـَا, ى, ـٰ) | o | كِتَاب → kitob, مُوسَى → muso, الرَّحْمٰن → ar-rahmon |
| cho'ziq ū / ī | u / i | غَفُور → gʻafur, رَحِيم → rahim |
| al- + qamariy harf | al- | الْقَمَر → al-qamar |
| al- + shamsiy harf | harf ikkilanadi | الشَّمْس → ash-shams |
| ة | a (vaqf), t (harakatli) | فَاطِمَة → fotima, رَحْمَةُ → rahmatu |
| الله | Alloh | |

## Qanday ishlaydi

`kirill_lotin.py` kabi tuzilgan: so'zlar `SOZ` regulyar ifodasi bilan topiladi va har biri `_soz()` da o'giriladi.

1. So'z tozalanadi: Unicode NFC, tatvil (ـ) va Qur'on belgilari olib tashlanadi, fors ک/ی → ك/ي.
2. Maxsus so'zlar tekshiriladi (الله → Alloh, alohida و → va).
3. "al-" artikli ajratiladi; shamsiy harf bo'lsa, "l" o'sha harfga aylanadi.
4. `_oqish()` so'zni [harf, harakatlar] juftliklari bo'yicha o'qiydi. Harakatdan keyin harakatsiz
   ا/ى/و/ي kelsa — cho'ziq unli (`CHOZIQ` jadvali). Kontekstga bog'liq harflar (ة, hamza, so'z boshidagi ع)
   alohida shartlarda ko'riladi.
5. Arab tinish belgilari va raqamlari (، ؟ ٢٠٢٤) lotinchaga o'giriladi; boshqa matn o'zgarmaydi.

## Loyiha uslubiga rioya

- Nomlar o'zbekcha, mavjud fayllardagidek: `JADVAL`, `SOZ`, `_soz()`, `_harf`-ga o'xshash `_oqish()`, `harakatlar`, `boshida`.
- Modul boshida bir qatorli docstring, funksiyada `>>>` misol — `kirill_lotin.py` dagidek.
- Testlar `tekshir(holatlar)` yordamchisi va `subTest` bilan — mavjud test fayllaridagidek.
- Tashqi kutubxona qo'shilmadi (faqat `re`, `unicodedata`).

## Cheklovlar (ataylab qilinmagan)

- **Harakatsiz matn** to'g'ri o'qilmaydi: محمد → mhmd. Arab yozuvida qisqa unlilar yozilmaydi, ularni
  lug'atsiz tiklab bo'lmaydi. To'g'ri natija uchun matn harakatli bo'lishi kerak.
- **Vasl** hisobga olinmaydi: بِسْمِ اللّٰهِ → "bismi Alloh", عَبْدُ اللّٰه → "abdu Alloh" (Abdulloh emas).
- **Old qo'shimchalar** (وَ, بِ, لِ, فَ) so'zga qo'shib yozilsa, artikl aniqlanmaydi.
- **O'rnashib qolgan shakllar** qoidadan farq qiladi: عَائِشَة → oʼisha (Oisha), خَدِيجَة → xadija (Xadicha).
- **Bosh harf** yo'q (arab yozuvida yo'q), faqat "Alloh" bosh harf bilan.

## AI bilan ishlash

Kodni AI (Claude Code) yozdi. Qoidalar avval `QOIDALAR.md` da yozildi, keyin kod va testlar shu jadvalga mos qilindi.

- AI an'anaviy shakli boshqacha bo'lgan ismlarni (Oisha, Xadicha) avval testga "to'g'ri javob" sifatida
  qo'ygan edi: `oʼisha`, `xadija`. Bu qoidaga mos, lekin o'zbekcha to'g'ri emas — shuning uchun ular testdan
  olinib, "Cheklovlar" bo'limiga ko'chirildi.
- CLI testi avval `StringIO` bilan yozilgan edi va yiqildi: `cli.py` `sys.stdout.reconfigure()` chaqiradi,
  `StringIO` da bunday metod yo'q. Mavjud `cli.py` ni o'zgartirmaslik uchun test alohida jarayonda
  (`subprocess`) ishga tushiriladigan qilindi.
- Bir nechta yozilish an'anasi bor joylarda (ī → "i" yoki "iy", so'z oxiridagi shadda: Ali yoki Aliy)
  AI bittasini tanladi; ular `QOIDALAR.md` da ko'rsatilgan va bitta jadvalni o'zgartirib almashtirsa bo'ladi.

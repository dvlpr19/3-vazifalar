# 3-vazifa: Mavjud loyihaga funksiya qo'shish

**Taxminiy vaqt:** 4–5 soat
**AI:** ruxsat etiladi.

## Vaziyat

`uztranslit/` papkasidagi loyiha o'zbek matnini kirill yozuvidan lotin yozuviga va aksincha o'giradi. Loyihaning testlari bor va hammasi o'tadi.

Loyihaga yangi imkoniyat qo'shish kerak: **arab yozuvidagi so'zlarni o'zbek lotin yozuviga o'girish.** Masalan, ismlar va diniy atamalar.

Siz Islom akademiyasida o'qiysiz, shuning uchun bu vazifada sizning bilimingiz AI'nikidan ustun turadi.

## Topshiriq

1. **`QOIDALAR.md` faylini yozing** (qisqa jadval ko'rinishida). Unda arab harflari va harakatlar o'zbek lotin yozuviga qanday o'tishi ko'rsatilsin. Kamida quyidagilar bo'lsin:
   - o'zbek tilida aniq mosi yo'q harflar: **ع, ح, ق, غ, خ**
   - cho'ziq unlilar: **ا, و, ي**
   - **"al-"** artikli va quyosh harflari (ash-shams, ar-rahmon)
   - **ta marbuta (ة)**
2. **`uztranslit/arab_lotin.py` modulini yozing** va unda `arab_lotin(matn)` funksiyasini yarating. Funksiyani `__init__.py` ga qo'shing.
3. **CLI'ga `--from arab` imkoniyatini qo'shing.**
4. **`tests/test_arab_lotin.py` faylini yozing.** Unda kamida 20 ta test holati bo'lsin: so'zlar, ismlar, iboralar, bo'sh matn va aralash matn.
5. **Eski testlarning hammasi o'tishi kerak.** Mavjud kodni buzmang.
6. **Loyiha uslubiga rioya qiling.** Yangi kod nomlash, izohlar va tuzilish bo'yicha mavjud kodga o'xshab yozilsin.

Testlarni ishga tushirish:

```bash
cd uztranslit
python -m unittest -v
```

## Baholanadi

- Qoidalar to'g'riligi (sohani bilishingiz)
- Kod mavjud loyihaga qanchalik tabiiy qo'shilgani
- Testlar sifati

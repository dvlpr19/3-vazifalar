# uztranslit

O'zbek tili uchun transliteratsiya kutubxonasi: kirill ↔ lotin, arab → lotin.

## Ishlatish

```bash
python -m uztranslit.cli --from kirill "Ўзбекистон"     # Oʻzbekiston
python -m uztranslit.cli --from lotin "Oʻzbekiston"     # Ўзбекистон
python -m uztranslit.cli --from arab "مُحَمَّد"           # muhammad
python -m uztranslit.cli --from kirill --fayl matn.txt
```

Python kodida:

```python
from uztranslit import arab_lotin, kirill_lotin, lotin_kirill

kirill_lotin("Ўзбекистон")   # 'Oʻzbekiston'
arab_lotin("الرَّحْمٰن")      # 'ar-rahmon'
```

Arab yozuvidan o'girish qoidalari va cheklovlari: [QOIDALAR.md](QOIDALAR.md).
Matn harakatli (unli belgilari qo'yilgan) bo'lishi kerak.

## Testlar

```bash
python -m unittest -v
```

## Tuzilishi

```
uztranslit/
├── kirill_lotin.py   kirill -> lotin
├── lotin_kirill.py   lotin -> kirill
├── arab_lotin.py     arab -> lotin
└── cli.py            buyruq qatori
tests/
```

Hech qanday tashqi kutubxona talab qilinmaydi (Python 3.10+).

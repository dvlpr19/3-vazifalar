# uztranslit

O'zbek tili uchun transliteratsiya kutubxonasi: kirill ↔ lotin.

## Ishlatish

```bash
python -m uztranslit.cli --from kirill "Ўзбекистон"     # Oʻzbekiston
python -m uztranslit.cli --from lotin "Oʻzbekiston"     # Ўзбекистон
python -m uztranslit.cli --from kirill --fayl matn.txt
```

Python kodida:

```python
from uztranslit import kirill_lotin, lotin_kirill

kirill_lotin("Ўзбекистон")   # 'Oʻzbekiston'
```

## Testlar

```bash
python -m unittest -v
```

## Tuzilishi

```
uztranslit/
├── kirill_lotin.py   kirill -> lotin
├── lotin_kirill.py   lotin -> kirill
└── cli.py            buyruq qatori
tests/
```

Hech qanday tashqi kutubxona talab qilinmaydi (Python 3.10+).

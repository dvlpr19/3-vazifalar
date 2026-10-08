"""Buyruq qatori interfeysi.

Ishlatish:
    python -m uztranslit.cli --from kirill "Ўзбекистон"
    python -m uztranslit.cli --from lotin "Oʻzbekiston"
    python -m uztranslit.cli --from arab "مُحَمَّد"
    python -m uztranslit.cli --from kirill --fayl matn.txt
"""

import argparse
import sys

from .arab_lotin import arab_lotin
from .kirill_lotin import kirill_lotin
from .lotin_kirill import lotin_kirill

OGIRUVCHILAR = {
    "kirill": kirill_lotin,
    "lotin": lotin_kirill,
    "arab": arab_lotin,
}


def main(argv=None):
    parser = argparse.ArgumentParser(description="O'zbek tili transliteratori")
    parser.add_argument("--from", dest="manba", choices=OGIRUVCHILAR, required=True,
                        help="manba yozuv")
    parser.add_argument("matn", nargs="?", help="o'giriladigan matn")
    parser.add_argument("--fayl", help="matnni fayldan o'qish (UTF-8)")
    args = parser.parse_args(argv)

    if args.fayl:
        with open(args.fayl, encoding="utf-8") as f:
            matn = f.read()
    elif args.matn is not None:
        matn = args.matn
    else:
        parser.error("matn yoki --fayl berilishi kerak")

    sys.stdout.reconfigure(encoding="utf-8")
    print(OGIRUVCHILAR[args.manba](matn))


if __name__ == "__main__":
    main()

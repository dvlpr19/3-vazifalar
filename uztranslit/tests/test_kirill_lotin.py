import unittest

from uztranslit import kirill_lotin


class KirillLotinTest(unittest.TestCase):
    def tekshir(self, holatlar):
        for kirill, lotin in holatlar:
            with self.subTest(kirill=kirill):
                self.assertEqual(kirill_lotin(kirill), lotin)

    def test_oddiy_sozlar(self):
        self.tekshir([
            ("китоб", "kitob"),
            ("мактаб", "maktab"),
            ("шаҳар", "shahar"),
            ("чиройли", "chiroyli"),
        ])

    def test_maxsus_harflar(self):
        self.tekshir([
            ("ўқитувчи", "oʻqituvchi"),
            ("ғалаба", "gʻalaba"),
            ("қалам", "qalam"),
            ("ҳаёт", "hayot"),
        ])

    def test_e_harfi(self):
        self.tekshir([
            ("ер", "yer"),
            ("поезд", "poyezd"),
            ("келди", "keldi"),
            ("эълон", "eʼlon"),
        ])

    def test_ts_harfi(self):
        self.tekshir([
            ("цирк", "sirk"),
            ("милиция", "militsiya"),
        ])

    def test_tutuq_va_yumshatish_belgisi(self):
        self.tekshir([
            ("маъно", "maʼno"),
            ("апрель", "aprel"),
        ])

    def test_bosh_harflar(self):
        self.tekshir([
            ("Ўзбекистон", "Oʻzbekiston"),
            ("Шаҳло", "Shahlo"),
            ("ТОШКЕНТ", "TOSHKENT"),
            ("Ёшлар", "Yoshlar"),
        ])

    def test_gap(self):
        self.assertEqual(
            kirill_lotin("Бугун ҳаво жуда яхши, 25 даража."),
            "Bugun havo juda yaxshi, 25 daraja.",
        )

    def test_kirill_bolmagan_matn_ozgarmaydi(self):
        self.assertEqual(kirill_lotin("Python 3.12"), "Python 3.12")


if __name__ == "__main__":
    unittest.main()

import unittest

from uztranslit import lotin_kirill


class LotinKirillTest(unittest.TestCase):
    def tekshir(self, holatlar):
        for lotin, kirill in holatlar:
            with self.subTest(lotin=lotin):
                self.assertEqual(lotin_kirill(lotin), kirill)

    def test_oddiy_sozlar(self):
        self.tekshir([
            ("kitob", "китоб"),
            ("shahar", "шаҳар"),
            ("chiroyli", "чиройли"),
        ])

    def test_apostrof_turlari(self):
        # Foydalanuvchilar apostrofni har xil yozadi, hammasi bir xil natija berishi kerak
        for yozuv in ["oʻqituvchi", "o'qituvchi", "o’qituvchi", "o`qituvchi"]:
            with self.subTest(yozuv=yozuv):
                self.assertEqual(lotin_kirill(yozuv), "ўқитувчи")

    def test_e_harfi(self):
        self.tekshir([
            ("ekran", "экран"),
            ("keldi", "келди"),
            ("yer", "ер"),
        ])

    def test_tutuq_belgisi(self):
        self.assertEqual(lotin_kirill("maʼno"), "маъно")

    def test_bosh_harflar(self):
        self.tekshir([
            ("Oʻzbekiston", "Ўзбекистон"),
            ("Shahlo", "Шаҳло"),
        ])

    def test_gap(self):
        self.assertEqual(
            lotin_kirill("Bugun havo juda yaxshi."),
            "Бугун ҳаво жуда яхши.",
        )


if __name__ == "__main__":
    unittest.main()

import subprocess
import sys
import unittest

from uztranslit import arab_lotin


class ArabLotinTest(unittest.TestCase):
    def tekshir(self, holatlar):
        for arab, lotin in holatlar:
            with self.subTest(arab=arab):
                self.assertEqual(arab_lotin(arab), lotin)

    def test_oddiy_sozlar(self):
        self.tekshir([
            ("كِتَاب", "kitob"),
            ("سَلَام", "salom"),
            ("ذِكْر", "zikr"),
            ("صَبْر", "sabr"),
            ("رَمَضَان", "ramazon"),
        ])

    def test_ozbekchada_mosi_yoq_harflar(self):
        self.tekshir([
            ("سَعْد", "saʼd"),      # ع so'z o'rtasida — tutuq belgisi
            ("عُمَر", "umar"),      # ع so'z boshida yozilmaydi
            ("حَسَن", "hasan"),     # ح
            ("قُرْآن", "qurʼon"),   # ق
            ("غَفُور", "gʻafur"),   # غ
            ("خَالِد", "xolid"),    # خ
        ])

    def test_choziq_unlilar(self):
        self.tekshir([
            ("طَالِب", "tolib"),    # fatha + ا
            ("مُوسَى", "muso"),     # alif maqsura
            ("آدَم", "odam"),       # alif madda
            ("يُوسُف", "yusuf"),    # damma + و
            ("رَحِيم", "rahim"),    # kasra + ي
        ])

    def test_diftonglar(self):
        self.tekshir([
            ("حُسَيْن", "husayn"),
            ("يَوْم", "yavm"),
        ])

    def test_shadda_va_tanvin(self):
        self.tekshir([
            ("مُحَمَّد", "muhammad"),
            ("حَقّ", "haq"),        # so'z oxiridagi shadda ikkilanmaydi
            ("عَلِيّ", "aliy"),
            ("شُكْرًا", "shukran"),
        ])

    def test_hamza(self):
        self.tekshir([
            ("أَحْمَد", "ahmad"),   # so'z boshida yozilmaydi
            ("إِسْلَام", "islom"),
            ("رَأْس", "raʼs"),      # so'z o'rtasida — tutuq belgisi
        ])

    def test_qamariy_harflar_bilan_artikl(self):
        self.tekshir([
            ("الْقَمَر", "al-qamar"),
            ("الْكِتَاب", "al-kitob"),
        ])

    def test_quyosh_harflari_bilan_artikl(self):
        self.tekshir([
            ("الشَّمْس", "ash-shams"),
            ("الرَّحْمٰن", "ar-rahmon"),
            ("السَّلَام", "as-salom"),
            ("النُّور", "an-nur"),
        ])

    def test_ta_marbuta(self):
        self.tekshir([
            ("فَاطِمَة", "fotima"),   # to'xtab o'qishda — "a"
            ("مَكَّة", "makka"),
            ("رَحْمَةُ", "rahmatu"),  # harakatli — "t"
        ])

    def test_alloh(self):
        self.tekshir([
            ("الله", "Alloh"),
            ("اللّٰهِ", "Alloh"),
        ])

    def test_ismlar(self):
        self.tekshir([
            ("إِبْرَاهِيم", "ibrohim"),
            ("عُثْمَان", "usmon"),
            ("زَيْنَب", "zaynab"),
            ("أَبُو بَكْر", "abu bakr"),
        ])

    def test_iboralar(self):
        self.tekshir([
            ("السَّلَامُ عَلَيْكُمْ", "as-salomu alaykum"),
            ("إِنْ شَاءَ اللّٰه", "in shoʼa Alloh"),
            ("مُحَمَّد وَ عَلِيّ", "muhammad va aliy"),
        ])

    def test_bosh_matn(self):
        self.assertEqual(arab_lotin(""), "")

    def test_aralash_matn(self):
        self.tekshir([
            ("Ismi: مُحَمَّد, 2024", "Ismi: muhammad, 2024"),
            ("Салом سَلَام", "Салом salom"),
            ("Python 3.12", "Python 3.12"),
        ])

    def test_arab_tinish_belgilari_va_raqamlari(self):
        self.assertEqual(arab_lotin("كِتَاب، ٢٠٢٤؟"), "kitob, 2024?")

    def test_fors_harflari_va_qoshimcha_belgilar(self):
        self.tekshir([
            ("کِتَاب", "kitob"),       # fors ک
            ("كِتَـــاب", "kitob"),     # tatvil (cho'zish chizig'i)
            ("ٱلْقَمَر", "al-qamar"),   # alif vasla
        ])

    def test_harakatsiz_matn(self):
        # Harakatsiz matnda qisqa unlilar yo'q — faqat cho'ziq unlilar o'qiladi
        self.tekshir([
            ("محمد", "mhmd"),
            ("كتاب", "ktob"),
            ("الشمس", "ash-shms"),
        ])

    def test_cli(self):
        natija = subprocess.run(
            [sys.executable, "-m", "uztranslit.cli", "--from", "arab", "الرَّحْمٰن"],
            capture_output=True, text=True, encoding="utf-8",
        )
        self.assertEqual(natija.returncode, 0, natija.stderr)
        self.assertEqual(natija.stdout.strip(), "ar-rahmon")


if __name__ == "__main__":
    unittest.main()

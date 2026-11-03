"""Praktik 4: Unit test lengkap dengan unittest.

Fungsi yang diuji:
  (a) hitung_ipk()          : IPK dari list dict {'bobot', 'sks'}
  (b) validasi_nim()        : format NIM = 10 digit angka
  (c) konversi_nilai_huruf(): angka 0-100 -> huruf (A, A-, B+, B, B-, C+, C, D, E)

Mencakup: happy path, edge case, dan input tidak valid.
Jalankan:  python3 praktik4_unittest.py -v
"""


def hitung_ipk(nilai_list):
    """Hitung IPK = total(bobot*sks) / total(sks); 0.0 bila kosong."""
    if not nilai_list:
        return 0.0
    total_bobot = sum(n["bobot"] * n["sks"] for n in nilai_list)
    total_sks = sum(n["sks"] for n in nilai_list)
    if total_sks == 0:
        return 0.0
    return total_bobot / total_sks


def validasi_nim(nim):
    """True jika NIM terdiri dari tepat 10 digit angka."""
    return isinstance(nim, str) and len(nim) == 10 and nim.isdigit()


def konversi_nilai_huruf(angka):
    """Konversi nilai angka 0-100 menjadi huruf mutu."""
    if not isinstance(angka, (int, float)) or isinstance(angka, bool):
        raise TypeError("Nilai harus berupa angka.")
    if angka < 0 or angka > 100:
        raise ValueError("Nilai harus berada pada rentang 0-100.")
    if angka >= 85:
        return "A"
    if angka >= 80:
        return "A-"
    if angka >= 75:
        return "B+"
    if angka >= 70:
        return "B"
    if angka >= 65:
        return "B-"
    if angka >= 60:
        return "C+"
    if angka >= 55:
        return "C"
    if angka >= 40:
        return "D"
    return "E"


import unittest  # noqa: E402  (import di bawah fungsi sesuai gaya modul)


class TestHitungIPK(unittest.TestCase):
    def test_normal(self):
        nilai = [
            {"bobot": 4.0, "sks": 3},
            {"bobot": 3.0, "sks": 2},
            {"bobot": 3.7, "sks": 3},
        ]
        self.assertAlmostEqual(hitung_ipk(nilai), 3.6375)

    def test_kosong(self):
        self.assertEqual(hitung_ipk([]), 0.0)

    def test_total_sks_nol(self):
        self.assertEqual(hitung_ipk([{"bobot": 4.0, "sks": 0}]), 0.0)

    def test_satu_matakuliah(self):
        self.assertEqual(hitung_ipk([{"bobot": 3.5, "sks": 4}]), 3.5)


class TestValidasiNIM(unittest.TestCase):
    def test_nim_benar(self):
        self.assertTrue(validasi_nim("2024132001"))

    def test_nim_ada_huruf(self):
        self.assertFalse(validasi_nim("20241A2001"))

    def test_nim_kurang_dari_10_digit(self):
        self.assertFalse(validasi_nim("202413200"))

    def test_nim_lebih_dari_10_digit(self):
        self.assertFalse(validasi_nim("20241320011"))

    def test_nim_bukan_string(self):
        self.assertFalse(validasi_nim(2024132001))
        self.assertFalse(validasi_nim(None))


class TestKonversiNilaiHuruf(unittest.TestCase):
    def test_batas_atas_tiap_huruf(self):
        self.assertEqual(konversi_nilai_huruf(100), "A")
        self.assertEqual(konversi_nilai_huruf(85), "A")
        self.assertEqual(konversi_nilai_huruf(84.9), "A-")
        self.assertEqual(konversi_nilai_huruf(80), "A-")
        self.assertEqual(konversi_nilai_huruf(75), "B+")
        self.assertEqual(konversi_nilai_huruf(70), "B")
        self.assertEqual(konversi_nilai_huruf(65), "B-")
        self.assertEqual(konversi_nilai_huruf(60), "C+")
        self.assertEqual(konversi_nilai_huruf(55), "C")
        self.assertEqual(konversi_nilai_huruf(40), "D")
        self.assertEqual(konversi_nilai_huruf(39.9), "E")
        self.assertEqual(konversi_nilai_huruf(0), "E")

    def test_nilai_di_luar_rentang(self):
        with self.assertRaises(ValueError):
            konversi_nilai_huruf(101)
        with self.assertRaises(ValueError):
            konversi_nilai_huruf(-5)

    def test_tipe_tidak_valid(self):
        with self.assertRaises(TypeError):
            konversi_nilai_huruf("delapan puluh")
        with self.assertRaises(TypeError):
            konversi_nilai_huruf(None)


if __name__ == "__main__":
    unittest.main(verbosity=2)

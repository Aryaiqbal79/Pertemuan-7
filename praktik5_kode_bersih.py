"""Praktik 5 (SESUDAH): hasil refactoring dari praktik5_kode_kotor.py.

Perbaikan tiap code smell:
  1. Magic Number  -> diganti konstanta bernama (NIM_LENGTH, BATAS_LULUS, ...)
  2. Duplicate Code -> validasi NIM dipusatkan di validasi_nim()
  3. Long Method    -> dipecah: hitung_rata_rata(), tentukan_kelulusan(),
                       proses_kelulusan()
  4. Deep Nesting   -> guard clause (return dini) di tentukan_kelulusan()
  5. Dead Code      -> fungsi_tidak_dipakai() dihapus

Perilaku (output) dipertahankan sama dengan versi kotor.
"""

# --- Konstanta pengganti magic number ---------------------------------------
NIM_LENGTH = 10
BATAS_LULUS = 60.0
STATUS_LULUS_ADMIN = 3

DATA = [
    {"nim": "2024132018", "nama": "Arya", "nilai": [80, 75, 90], "status": 3},
    {"nim": "202413200", "nama": "Aisma", "nilai": [85, 88], "status": 3},
    {"nim": "ABC", "nama": "Sona", "nilai": [70, 65], "status": 3},
    {"nim": "2024132043", "nama": "Paiton", "nilai": [50, 55], "status": 3},
    {"nim": "2024132011", "nama": "Adrian", "nilai": [], "status": 1},
]


def validasi_nim(nim: str) -> bool:
    """True jika NIM berupa string digit dengan panjang tepat NIM_LENGTH."""
    return isinstance(nim, str) and nim.isdigit() and len(nim) == NIM_LENGTH


def hitung_rata_rata(nilai: list) -> float:
    """Hitung rata-rata list nilai; 0.0 jika list kosong."""
    if not nilai:
        return 0.0
    return sum(nilai) / len(nilai)


def tentukan_kelulusan(mahasiswa: dict) -> str:
    """Tentukan status kelulusan satu mahasiswa dengan guard clause."""
    nama = mahasiswa.get("nama", "-")
    if not mahasiswa.get("nim"):
        return "TANPA NIM"
    if not validasi_nim(mahasiswa["nim"]):
        return "NIM TIDAK VALID"
    if not mahasiswa.get("nilai"):
        return f"{nama} TIDAK ADA NILAI"
    if hitung_rata_rata(mahasiswa["nilai"]) < BATAS_LULUS:
        return f"{nama} TIDAK LULUS"
    if mahasiswa.get("status") != STATUS_LULUS_ADMIN:
        return f"{nama} BELUM LULUS ADMIN"
    return f"{nama} LULUS"


def proses_kelulusan(daftar_mahasiswa: list) -> list:
    """Proses seluruh daftar mahasiswa menjadi list status kelulusan."""
    return [tentukan_kelulusan(m) for m in daftar_mahasiswa if m]


if __name__ == "__main__":
    for baris in proses_kelulusan(DATA):
        print(baris)

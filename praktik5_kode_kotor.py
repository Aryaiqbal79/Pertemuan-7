"""Praktik 5 (SEBELUM): kode dengan 5 code smell.

Code smell yang disengaja:
  1. Magic Number      : 10, 60, dan 3 tanpa penjelasan
  2. Duplicate Code    : validasi NIM ditulis ulang di cek_nim_lagi()
  3. Long Method       : proses_data() mengerjakan semuanya (±30 baris)
  4. Deep Nesting      : if bertingkat 5 level di proses_data()
  5. Dead Code         : fungsi_tidak_dipakai() tidak pernah dipanggil
"""

DATA = [
    {"nim": "2024132018", "nama": "Arya", "nilai": [80, 75, 90], "status": 3},
    {"nim": "202413200", "nama": "Aisma", "nilai": [85, 88], "status": 3},
    {"nim": "ABC", "nama": "Sona", "nilai": [70, 65], "status": 3},
    {"nim": "2024132043", "nama": "Paiton", "nilai": [50, 55], "status": 3},
    {"nim": "2024132011", "nama": "Adrian", "nilai": [], "status": 1},
]


def proses_data(mahasiswa_list):
    hasil = []
    for m in mahasiswa_list:
        if m:
            if m.get("nim"):
                if m["nim"].isdigit() and len(m["nim"]) == 10:
                    if m.get("nilai"):
                        total = 0
                        for n in m["nilai"]:
                            total += n
                        rata = total / len(m["nilai"])
                        if rata >= 60:
                            if m.get("status") == 3:
                                hasil.append(m["nama"] + " LULUS")
                            else:
                                hasil.append(m["nama"] + " BELUM LULUS ADMIN")
                        else:
                            hasil.append(m["nama"] + " TIDAK LULUS")
                    else:
                        hasil.append(m["nama"] + " TIDAK ADA NILAI")
                else:
                    hasil.append("NIM TIDAK VALID")
            else:
                hasil.append("TANPA NIM")
    return hasil


def cek_nim_lagi(nim):
    if nim.isdigit() and len(nim) == 10:
        return True
    return False


def fungsi_tidak_dipakai():
    x = 1
    return x * 2


if __name__ == "__main__":
    for baris in proses_data(DATA):
        print(baris)

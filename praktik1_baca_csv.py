"""Praktik 1: Membaca data mahasiswa dari file CSV dengan exception handling lengkap.

Menangani:
  - FileNotFoundError : file tidak ditemukan
  - csv.Error         : format CSV rusak (dibaca dengan strict=True)
  - ValueError        : konversi data tidak valid (mis. IPK bukan angka)

Blok finally memastikan file selalu ditutup, blok else menampilkan
ringkasan hanya jika pembacaan berhasil tanpa exception.
"""

import csv


def baca_data_mahasiswa(path: str):
    """Baca CSV data mahasiswa; kembalikan list dict atau None jika gagal."""
    f = None
    data = []
    try:
        f = open(path, newline="", encoding="utf-8")
        reader = csv.DictReader(f, strict=True)
        for baris in reader:
            # ValueError jika kolom 'ipk' bukan angka yang valid
            data.append(
                {
                    "nim": baris["nim"],
                    "nama": baris["nama"],
                    "ipk": float(baris["ipk"]),
                }
            )
    except FileNotFoundError:
        print(f"[FileNotFoundError] File '{path}' tidak ditemukan.")
        return None
    except csv.Error as e:
        print(f"[csv.Error] Format file '{path}' rusak: {e}")
        return None
    except ValueError as e:
        print(f"[ValueError] Data tidak valid di '{path}': {e}")
        return None
    else:
        # Hanya dijalankan jika TIDAK ada exception
        print(f"[OK] Berhasil membaca {len(data)} data mahasiswa dari '{path}'.")
        rata_ipk = sum(m["ipk"] for m in data) / len(data) if data else 0.0
        ipk_tertinggi = max(m["ipk"] for m in data) if data else 0.0
        print(f"     Rata-rata IPK : {rata_ipk:.2f}")
        print(f"     IPK tertinggi : {ipk_tertinggi:.2f}")
        return data
    finally:
        # Selalu dijalankan: sukses maupun gagal
        if f is not None:
            f.close()
            print(f"     (finally) File '{path}' sudah ditutup.\n")


def main() -> None:
    print("=== 1. File valid ===")
    baca_data_mahasiswa("data_mahasiswa.csv")

    print("=== 2. File tidak ada (FileNotFoundError) ===")
    baca_data_mahasiswa("data_tidak_ada.csv")

    print("=== 3. Nilai IPK bukan angka (ValueError) ===")
    baca_data_mahasiswa("data_nilai_rusak.csv")

    print("=== 4. Format CSV rusak / quote tak tertutup (csv.Error) ===")
    baca_data_mahasiswa("data_format_rusak.csv")


if __name__ == "__main__":
    main()

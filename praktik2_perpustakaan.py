"""Praktik 2: Hierarki custom exception untuk Sistem Informasi Perpustakaan.

Hierarki:
    PerpustakaanError (base)
    ├── BukuNotFoundError        : kode buku tidak terdaftar
    ├── BukuTidakTersediaError   : stok buku habis / sedang dipinjam semua
    └── AnggotaNotFoundError     : ID anggota tidak terdaftar
"""


class PerpustakaanError(Exception):
    """Base exception untuk seluruh error SI Perpustakaan."""


class BukuNotFoundError(PerpustakaanError):
    """Kode buku tidak terdaftar di katalog."""

    def __init__(self, kode_buku: str):
        self.kode_buku = kode_buku
        super().__init__(f"Buku dengan kode '{kode_buku}' tidak terdaftar.")


class BukuTidakTersediaError(PerpustakaanError):
    """Seluruh eksemplar buku sedang dipinjam (stok 0)."""

    def __init__(self, judul: str, stok: int):
        self.judul = judul
        self.stok = stok
        super().__init__(
            f"Buku '{judul}' sedang tidak tersedia (stok: {stok})."
        )


class AnggotaNotFoundError(PerpustakaanError):
    """ID anggota tidak terdaftar."""

    def __init__(self, id_anggota: str):
        self.id_anggota = id_anggota
        super().__init__(f"Anggota dengan ID '{id_anggota}' tidak terdaftar.")


# --- Data simulasi -----------------------------------------------------------
KATALOG = {
    "BK001": {"judul": "Pemrograman Python", "stok": 2},
    "BK002": {"judul": "Basis Data Lanjut", "stok": 0},
    "BK003": {"judul": "Sistem Informasi Manajemen", "stok": 1},
}

ANGGOTA = {
    "A001": {"nama": "Arya Adi Muhammad Iqbal"},
    "A002": {"nama": "Aisma Haidy Putri"},
}


def pinjam_buku(id_anggota: str, kode_buku: str) -> str:
    """Pinjam satu eksemplar buku; raise custom exception bila tidak valid."""
    if id_anggota not in ANGGOTA:
        raise AnggotaNotFoundError(id_anggota)
    if kode_buku not in KATALOG:
        raise BukuNotFoundError(kode_buku)
    buku = KATALOG[kode_buku]
    if buku["stok"] <= 0:
        raise BukuTidakTersediaError(buku["judul"], buku["stok"])
    buku["stok"] -= 1
    nama = ANGGOTA[id_anggota]["nama"]
    return (
        f"{nama} berhasil meminjam '{buku['judul']}' "
        f"(sisa stok: {buku['stok']})."
    )


def demonstrasi(id_anggota: str, kode_buku: str) -> None:
    """Satu skenario peminjaman dengan penanganan tiap jenis exception."""
    print(f"-- pinjam_buku({id_anggota!r}, {kode_buku!r}) --")
    try:
        hasil = pinjam_buku(id_anggota, kode_buku)
    except AnggotaNotFoundError as e:
        print(f"[AnggotaNotFoundError] {e}")
    except BukuNotFoundError as e:
        print(f"[BukuNotFoundError] {e}")
    except BukuTidakTersediaError as e:
        print(f"[BukuTidakTersediaError] {e}")
    except PerpustakaanError as e:
        # Menangkap sisa subclass PerpustakaanError yang belum dikenal
        print(f"[PerpustakaanError] {e}")
    else:
        print(f"[OK] {hasil}")
    print()


def main() -> None:
    print("=== Skenario 1: peminjaman berhasil ===")
    demonstrasi("A001", "BK001")

    print("=== Skenario 2: anggota tidak terdaftar ===")
    demonstrasi("A999", "BK001")

    print("=== Skenario 3: kode buku tidak terdaftar ===")
    demonstrasi("A001", "BK999")

    print("=== Skenario 4: buku habis dipinjam ===")
    demonstrasi("A002", "BK002")

    print("=== Skenario 5: stok habis setelah dipinjam ===")
    demonstrasi("A001", "BK003")  # stok 1 -> 0, berhasil
    demonstrasi("A002", "BK003")  # stok 0 -> BukuTidakTersediaError


if __name__ == "__main__":
    main()

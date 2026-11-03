"""Praktik 3: Konfigurasi logging untuk aplikasi Sistem Informasi.

  (a) File handler  : RotatingFileHandler, level DEBUG ke atas -> si_app.log
  (b) Console handler: StreamHandler, level WARNING ke atas -> terminal
  (c) Formatter      : timestamp | level | nama logger | pesan

Jalankan file ini, lalu periksa:
  - terminal hanya menampilkan WARNING, ERROR, CRITICAL
  - si_app.log menyimpan semua level mulai dari DEBUG
"""

import logging
from logging.handlers import RotatingFileHandler

NAMA_LOG = "si_app.log"


def buat_logger() -> logging.Logger:
    logger = logging.getLogger("si_akademik")
    logger.setLevel(logging.DEBUG)
    # Hindari handler ganda bila modul di-import ulang
    logger.handlers.clear()

    # (a) File handler dengan rotasi: maks 1 MB, simpan 2 file backup
    file_handler = RotatingFileHandler(
        NAMA_LOG, maxBytes=1 * 1024 * 1024, backupCount=2, encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )

    # (b) Console handler: hanya WARNING ke atas
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(
        logging.Formatter("%(levelname)s: %(message)s")
    )

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger


def main() -> None:
    logger = buat_logger()

    print("=== Mengirim log pada semua level ===", flush=True)
    logger.debug("Query SQL: SELECT nim, nama, ipk FROM mahasiswa")
    logger.info("User 'arya' berhasil login dari 192.168.1.10")
    logger.warning("Penggunaan memori server mencapai 85%")
    logger.error("Gagal mengirim email notifikasi ke dosen@ukri.ac.id")
    logger.critical("Koneksi database utama terputus!")

    print()
    print("=== Isi file si_app.log (semua level tercatat) ===")
    with open(NAMA_LOG, encoding="utf-8") as f:
        print(f.read(), end="")


if __name__ == "__main__":
    main()

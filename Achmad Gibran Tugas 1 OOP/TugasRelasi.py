class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.status_dipinjam = False

    def __str__(self):
        status = "Dipinjam" if self.status_dipinjam else "Tersedia"
        return f"{self.judul} oleh {self.penulis} ({status})"


class Anggota:
    def __init__(self, nama):
        self.nama = nama

    def __str__(self):
        return f"Anggota: {self.nama}"


class Peminjaman:
    def __init__(self, anggota, buku):
        self.anggota = anggota
        self.buku = buku
        buku.status_dipinjam = True

    def __str__(self):
        return f"{self.anggota.nama} meminjam buku '{self.buku.judul}'"


class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.koleksi_buku = []
        self.daftar_anggota = []
        self.transaksi = []

    def tambah_buku(self, buku):
        self.koleksi_buku.append(buku)

    def tambah_anggota(self, anggota):
        self.daftar_anggota.append(anggota)

    def pinjam_buku(self, anggota, judul_buku):
        for buku in self.koleksi_buku:
            if buku.judul == judul_buku:
                if not buku.status_dipinjam:
                    peminjaman = Peminjaman(anggota, buku)
                    self.transaksi.append(peminjaman)
                    return peminjaman
                else:
                    print(f"Buku '{buku.judul}' sudah dipinjam!")
                    return None
        print("Buku tidak ditemukan!")
        return None

    def tampilkan_buku(self):
        print(f"\nDaftar Buku di {self.nama}:")
        for i, buku in enumerate(self.koleksi_buku, start=1):
            print(f"{i}. {buku}")

    def tampilkan_anggota(self):
        print(f"\nDaftar Anggota di {self.nama}:")
        for anggota in self.daftar_anggota:
            print("-", anggota)

    def tampilkan_transaksi(self):
        print("\nRiwayat Peminjaman:")
        if not self.transaksi:
            print("Belum ada transaksi.")
        for transaksi in self.transaksi:
            print("-", transaksi)


# ===== CONTOH PENGGUNAAN =====
perpus = Perpustakaan("Perpustakaan Kota")

# Tambah buku (2 pilihan saja)
perpus.tambah_buku(Buku("Laskar Pelangi", "Andrea Hirata"))
perpus.tambah_buku(Buku("Bumi Manusia", "Pramoedya Ananta Toer"))

# Tambah anggota (Bram dan Gibran)
bram = Anggota("Bram")
gibran = Anggota("Gibran")
perpus.tambah_anggota(bram)
perpus.tambah_anggota(gibran)

# Bram otomatis pinjam buku pertama
perpus.pinjam_buku(bram, "Laskar Pelangi")

# Tampilkan daftar buku sebelum Gibran memilih
perpus.tampilkan_buku()

# Gibran memilih buku yang tersisa
pilihan = int(input("\nGibran, pilih nomor buku yang ingin dipinjam: "))

if pilihan in [1, 2]:
    buku_dipilih = perpus.koleksi_buku[pilihan - 1].judul
    perpus.pinjam_buku(gibran, buku_dipilih)
else:
    print("Buku tidak tersedia.")

# Tampilkan hasil akhir
perpus.tampilkan_buku()
perpus.tampilkan_anggota()
perpus.tampilkan_transaksi()

import datetime

# ==============================================================================
# CLASS PERPUSTAKAAN
# ==============================================================================
class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        # Implementasi: tambahkan atribut untuk koleksi buku dan daftar anggota
        self.koleksi_buku = []
        # ATRIBUT LIST DIGANTI NAMANYA untuk menghindari konflik dengan method daftar_anggota
        self.daftar_anggota_list = [] 
        self.riwayat_pinjaman = []

    def tambah_buku(self, buku):
        # Implementasi: tambahkan buku ke koleksi
        if buku not in self.koleksi_buku:
            self.koleksi_buku.append(buku)
        # pass

    def daftar_anggota(self, anggota):
        # Implementasi: tambahkan anggota ke daftar
        # Menggunakan nama list yang baru (self.daftar_anggota_list)
        if anggota not in self.daftar_anggota_list:
            self.daftar_anggota_list.append(anggota)
        # pass

    def pinjam_buku(self, anggota, buku):
        # Implementasi: proses peminjaman buku oleh anggota
        
        # Validasi ketersediaan dan keanggotaan
        if buku not in self.koleksi_buku or buku.status_pinjaman == "Dipinjam":
            return f"Gagal: Buku '{buku.judul}' tidak tersedia/sudah dipinjam."
        # Menggunakan nama list yang baru
        if anggota not in self.daftar_anggota_list: 
            return f"Gagal: Anggota {anggota.nama} belum terdaftar."
            
        # Buat Transaksi (Composition)
        tanggal_skrg = datetime.date.today()
        transaksi_baru = Peminjaman(anggota, buku, tanggal_skrg)
        
        # Catat dan Perbarui Status
        self.riwayat_pinjaman.append(transaksi_baru)
        anggota.daftar_pinjaman.append(buku) 
        return f"SUCCESS: {anggota.nama} berhasil meminjam '{buku.judul}'."
        # pass

# ==============================================================================
# CLASS BUKU
# ==============================================================================
class Buku:
    def __init__(self, judul, penulis):
        # Implementasi: inisialisasi atribut buku
        self.judul = judul
        self.penulis = penulis
        self.status_pinjaman = "Tersedia"
        # pass
    
    def __str__(self):
        return f"'{self.judul}' oleh {self.penulis}"

# ==============================================================================
# CLASS ANGGOTA
# ==============================================================================
class Anggota:
    def __init__(self, nama):
        # Implementasi: inisialisasi atribut anggota
        self.nama = nama
        self.daftar_pinjaman = [] 
        # pass
        
    def __str__(self):
        return f"Anggota: {self.nama}"

# ==============================================================================
# CLASS PEMINJAMAN
# ==============================================================================
class Peminjaman:
    def __init__(self, anggota, buku, tanggal_pinjam):
        # Implementasi: inisialisasi transaksi peminjaman
        self.anggota = anggota
        self.buku = buku
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = None 
        
        # Perbarui status buku (Logic Composition)
        self.buku.status_pinjaman = "Dipinjam" 
        # pass

    def __str__(self):
        return f"Pinjam {self.buku.judul} oleh {self.anggota.nama}"


# ==============================================================================
# TESTING (OUTPUT TERSTRUKTUR)
# ==============================================================================

# 1. Membuat objek Perpustakaan, Buku, dan Anggota
perpustakaan_utama = Perpustakaan("Pusat Kota")
buku_oop = Buku("Pemrograman Berorientasi Objek", "Abadi Nugroho")
buku_sd = Buku("Struktur Data", "Abadi Nugroho")
anggota_a = Anggota("Wulan")
anggota_b = Anggota("Dika")

# 2. Menambah buku ke perpustakaan (Aggregation)
perpustakaan_utama.tambah_buku(buku_oop)
perpustakaan_utama.tambah_buku(buku_sd)

# 3. Mendaftarkan anggota (Association)
# Baris ini sekarang memanggil METHOD daftar_anggota yang sudah benar.
perpustakaan_utama.daftar_anggota(anggota_a)
perpustakaan_utama.daftar_anggota(anggota_b)


# 4. Meminjam buku oleh anggota (Composition & Association)
print(perpustakaan_utama.pinjam_buku(anggota_a, buku_oop))
print(perpustakaan_utama.pinjam_buku(anggota_b, buku_sd))
print(perpustakaan_utama.pinjam_buku(anggota_b, buku_oop)) 

print("\n----------------------------------------------------")
# 5. Menampilkan status peminjaman (Output Terstruktur)
print(f"{anggota_a.nama} sedang meminjam:")
for buku in anggota_a.daftar_pinjaman:
    print(f"- {buku.judul}")

print(f"\nStatus buku '{buku_oop.judul}' saat ini: {buku_oop.status_pinjaman}")
print(f"Total transaksi peminjaman dicatat: {len(perpustakaan_utama.riwayat_pinjaman)}")
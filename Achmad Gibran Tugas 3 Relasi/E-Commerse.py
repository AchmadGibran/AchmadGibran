# Achmad Gibran - 202412003
# Tugas relasi 2

class Pelanggan:
    def __init__(self, nama, email):
        # Implementasi: inisialisasi pelanggan dengan keranjang dan riwayat pesanan
        self.nama = nama
        self.email = email
        self.keranjang = Keranjang()
        self.riwayat_pesanan = []

    def buat_pesanan(self):
        # Implementasi: buat pesanan dari keranjang
        if not self.keranjang.items:
            return None

        pesanan_baru = Pesanan(self)
        
        for produk, jumlah in self.keranjang.items.items():
            # Proses item, buat ItemPesanan, dan update stok
            item = ItemPesanan(produk, jumlah)
            pesanan_baru.item_pesanan_list.append(item)
            produk.stok -= jumlah 

        pesanan_baru.total_harga = sum(item.hitung_subtotal() for item in pesanan_baru.item_pesanan_list)
        self.riwayat_pesanan.append(pesanan_baru)
        self.keranjang.items = {} # Kosongkan keranjang
        
        return pesanan_baru

class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

class Keranjang:
    def __init__(self):
        self.items = {} # {Produk: jumlah}

    def tambah_produk(self, produk, jumlah):
        if produk.stok < jumlah:
            return

        self.items[produk] = self.items.get(produk, 0) + jumlah
    
    # Metode hapus_keranjang dihilangkan, langsung dikosongkan di Pelanggan.buat_pesanan

class Pesanan:
    def __init__(self, pelanggan):
        self.pelanggan = pelanggan
        self.item_pesanan_list = []
        self.total_harga = 0

    # Metode hitung total digabungkan langsung ke Pelanggan.buat_pesanan untuk penyederhanaan

class ItemPesanan:
    def __init__(self, produk, jumlah):

        self.produk = produk
        self.jumlah = jumlah
    
    def hitung_subtotal(self):
        return self.produk.harga * self.jumlah
        
# PROGRAM
if __name__ == "__main__":
    
    # SETUP
    p1 = Produk("Buku", 50000, 10)
    p2 = Produk("Pensil", 10000, 5)
    
    koko = Pelanggan("Gibran", "Gibran@gmail.com")
    
    # PROSES
    koko.keranjang.tambah_produk(p1, 2)
    koko.keranjang.tambah_produk(p2, 1)
    
    pesanan = koko.buat_pesanan()

    # OUTPUT
    if pesanan:
        print(f"Pesanan dari {pesanan.pelanggan.nama} berhasil dibuat.")
        print(f"Total Harga: Rp {pesanan.total_harga}")
        print(f"Stok Buku sekarang: {p1.stok}")
    else:
        print("Gagal membuat pesanan.")
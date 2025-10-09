class Dosen:
    def __init__(self, nama):
        self.nama = nama
        self.mata_kuliah = [] # Association dengan MataKuliah

    def ajar(self, mk):
        # Menambahkan hubungan association
        self.mata_kuliah.append(mk)
        mk.dosen = self # Hubungan dua arah

class MataKuliah:
    def __init__(self, nama):
        self.nama = nama
        self.dosen = None # Association dengan Dosen

# ===== CONTOH PENGGUNAAN =====
dosen1 = Dosen("Abadi Nugroho")
mk1 = MataKuliah("Pemrograman Berorientasi Objek")
mk2 = MataKuliah("Struktur Data")

# Membuat hubungan association
dosen1.ajar(mk1)
dosen1.ajar(mk2)

# Mengakses hubungan
print(f"{dosen1.nama} mengajar:")
for mk in dosen1.mata_kuliah:
    print(f"- {mk.nama}")

print(f"{mk1.nama} diajar oleh: {mk1.dosen.nama}")

# Objek dapat eksis secara independen
del dosen1
# mk1 dan mk2 masih tetap ada
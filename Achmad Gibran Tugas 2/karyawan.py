#Achmad Gibran

class Karyawan:
    perusahaan = "PT Python Jaya" # Class attribute

    def __init__(self, nama, gaji):
        self.nama = nama
        self.__gaji = gaji
        self._tunjangan = 0

    def hitung_gaji_bersih(self):
        return self.__gaji + self._tunjangan

    def set_tunjangan(self, tunjangan):
        if tunjangan >= 0:
            self._tunjangan = tunjangan

# kelas
karyawan1 = Karyawan("Budi", 5000000)
karyawan1.set_tunjangan(1000000)

# Akses langsung atribut _gaji dari luar kelas
print(f"akses langsung ke gaji: {karyawan1.__gaji}")

# memanggil method
gaji_bersih_budi = karyawan1.hitung_gaji_bersih()

# Output
print(f"Gaji Bersih Budi adalah: {gaji_bersih_budi}")

# mengubah instance
karyawan1.perusahaan = "PT Makmur Jaya"

# cetak 
print(karyawan1.perusahaan)
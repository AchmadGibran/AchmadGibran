#Achmad Gibran

from datetime import datetime 

class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        # a. Atribut: public, protected, private
        self.judul = judul              # Public
        self._penulis = penulis         # Protected
        self.__tahun_terbit = tahun_terbit # Private
        # Memanggil setter untuk memastikan validasi awal tahun terbit
        self.set_tahun_terbit(tahun_terbit) 

    def get_info(self):
        # c. Metode get_info()
        return (f"Judul: {self.judul}\n"
                f"Penulis: {self._penulis}\n"
                f"Tahun Terbit: {self.get_tahun_terbit()}")

    # d. Getter untuk __tahun_terbit
    def get_tahun_terbit(self):
        return self.__tahun_terbit

    # d & e. Setter untuk __tahun_terbit dengan validasi
    def set_tahun_terbit(self, tahun):
        # Menggunakan datetime.now().year untuk mendapatkan tahun saat ini
        tahun_sekarang = datetime.now().year 
        
        # Validasi (tahun terbit tidak boleh lebih dari tahun sekarang)
        if tahun <= tahun_sekarang:
            self.__tahun_terbit = tahun
        else:
            print(f"ERROR: Tahun terbit ({tahun}) tidak boleh lebih dari tahun sekarang ({tahun_sekarang}).")
            # Menetapkan nilai yang valid (tahun sekarang) sebagai fallback
            self.__tahun_terbit = tahun_sekarang 
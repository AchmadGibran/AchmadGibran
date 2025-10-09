#Achmad Gibran - 202412003
#Tugas 3 OOP

# Class Karyawan (Parent Class)
class Karyawan:
    
    def __init__(self, nama, id_karyawan, gaji_pokok):
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.gaji_pokok = gaji_pokok

    def hitung_gaji(self):
        return self.gaji_pokok

    def info(self):
        # Mengambil nilai integer gaji total dan menambahkan suffix '.0'
        gaji_terformat = f"{int(self.hitung_gaji())}.0"

        return f"Karyawan : {self.nama}, ID: {self.id_karyawan}, Gaji: {gaji_terformat}"

# Class Manager (Subclass)
class Manager(Karyawan):
    
    def __init__(self, nama, id_karyawan, gaji_pokok, tunjangan):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.tunjangan = tunjangan

    def hitung_gaji(self):
        return self.gaji_pokok + self.tunjangan

    def info(self):
        parent_info = super().info().replace("Karyawan", "Manager")
        return parent_info

# Class Programmer (Subclass)
class Programmer(Karyawan):
    
    def __init__(self, nama, id_karyawan, gaji_pokok, bonus):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.bonus = bonus

    def hitung_gaji(self):
        return self.gaji_pokok + self.bonus

    def info(self):
        parent_info = super().info().replace("Karyawan", "Programmer")
        return parent_info


# Manager: Achmad, A001, Total Gaji 8.000.000 (7jt + 1jt)
manager1 = Manager("Achmad", "A001", 7000000.0, 1000000.0) 

# Programmer: Gibran, G001, Total Gaji 13.000.000 (11jt + 2jt)
programmer1 = Programmer("Gibran", "G001", 11000000.0, 2000000.0) 

# Menampilkan
print(manager1.info())
print(programmer1.info())
#Achmad Gibran

class AkunBank:
    MIN_SALDO = 50000

    def __init__(self, nama_pemilik, saldo_awal, nomor_akun):
        self.nama_pemilik = nama_pemilik
        self.__nomor_akun = nomor_akun
        self.__saldo = 0
        
        # Validasi saldo awal
        if saldo_awal >= self.MIN_SALDO:
            self.__saldo = saldo_awal

    def setor(self, amount):
        if amount > 0:
            self.__saldo += amount
            return True

    def tarik(self, amount):
        # Validasi saldo minimal setelah penarikan
        if amount > 0 and (self.__saldo - amount) >= self.MIN_SALDO:
            self.__saldo -= amount
            return True
        return False

    def get_saldo(self):
        return self.__saldo

    def transfer(self, akun_tujuan, amount):
        if self.tarik(amount): # Menggunakan tarik() untuk validasi
            akun_tujuan.setor(amount)
            return True
        return False
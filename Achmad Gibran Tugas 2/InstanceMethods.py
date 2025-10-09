#Achmad Gibran

class Mobil:
    def __init__(self, merk):

        self.merk = merk 

    def info(self):
        print(f"Mobil ini bermerk {self.merk}")

toyota = Mobil("Toyota")
toyota.info()

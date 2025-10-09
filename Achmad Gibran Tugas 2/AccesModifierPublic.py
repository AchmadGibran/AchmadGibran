#Achmad Gibran

class person:
    def __init__(self, nama, umur):
        self.nama = nama #public attr
        self.umur = umur #public attr


    def display_info(self):
        print(f"Nama: {self.nama}, age: {self.umur}")

person = person("Dinda", 19)
print(person.nama)
person.umur = 20
person.display_info()

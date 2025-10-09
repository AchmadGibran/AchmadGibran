#Achmad Gibran

class person:
    def __init__(self, nama, umur):
        self.nama = nama #public attr
        self._umur = umur #public attr
        self.__id = 12345 #private

    #protected method
    def _internal_helper(self):
        print("This is a protected method")

person = person("Dinda", 19)
print(person.nama) 
person.umur = 20
person._internal_helper()

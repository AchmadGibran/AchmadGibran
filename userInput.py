
#Achmad Gibran - 202412003
# Program meminta tiga input kesukaan user dan menggabungkannya dalam sebuah kalimat.

nama = input("Masukkan nama Anda: ")
print(f"Halo {nama}")

fav1 = input("Apa **hewan kesukaan** Anda? ")

fav2 = input("Apa **warna kesukaan** Anda? ")

fav3 = input("Apa **angka kesukaan** Anda? ")

# Output
print("Menarik! Jadi, Anda paling menyukai:")
print(f"1. **{fav1}**")
print(f"2. **{fav2}**")
print(f"3. **{fav3}**")

print(f"\nKombinasi kesukaan Anda adalah: {fav1}, {fav2}, dan {fav3}.")
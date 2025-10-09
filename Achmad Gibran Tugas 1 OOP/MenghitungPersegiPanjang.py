#Achmad Gibran - 202412003
#program sederhana menghitung luas persegi panjang

def hitung_luas_persegi_panjang():
    print("--- Kalkulator Luas Persegi Panjang Sederhana ---")
    
    # 1. Input: Menerima panjang (sebagai teks/string)
    input_panjang = input("Masukkan nilai panjang: ").strip()
    
    # 2. Input: Menerima lebar (sebagai teks/string)
    input_lebar = input("Masukkan nilai lebar: ").strip()
    
    # Konversi Tipe Data: Mengubah teks/string menjadi angka (float)
    try:
        panjang = float(input_panjang)
        lebar = float(input_lebar)
    except ValueError:
        print("\n❌ Input tidak valid. Mohon masukkan angka saja.")
        return # Menghentikan program jika input bukan angka

    # 3. Perhitungan: Menghitung luas
    luas = panjang * lebar
    
    # 4. Output: Menampilkan hasil
    print("\n--- HASIL PERHITUNGAN ---")
    print(f"Panjang = {panjang}")
    print(f"Lebar   = {lebar}")
    print(f"Luasnya adalah: {luas}")
    print("-------------------------")

# Memanggil dan menjalankan fungsi
hitung_luas_persegi_panjang()
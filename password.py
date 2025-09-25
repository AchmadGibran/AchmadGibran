# Tidak perlu import modul lain selain yang ada di Python standar

def buat_jadwal_sortir():
    """
    Program untuk membuat jadwal dan mengurutkannya secara otomatis
    berdasarkan waktu mulai (format HH:MM).
    """
    
    jadwal = [] # Python Lists: List kosong untuk menampung acara
    
    # --- 1. Input Acara (Python While Loops) ---
    print("--- MASUKKAN JADWAL ACARA ---")
    print("Ketik 'selesai' di kolom manapun untuk mengakhiri input.")
    
    while True:
        # Input Waktu
        waktu = input("Waktu (format HH:MM, cth: 08:30): ").strip()
        
        # Pengecekan pertama: Keluar jika input waktu adalah 'selesai'
        if waktu.lower() == 'selesai':
            break

        # Input Nama Acara
        acara = input("Nama Acara: ").strip()
        
        # Pengecekan kedua: Keluar jika input acara adalah 'selesai'
        if acara.lower() == 'selesai':
            break
            
        # Python Dictionaries: Membuat entri acara
        event = {
            "acara": acara,
            "waktu": waktu
        }
        
        jadwal.append(event)
        print("✅ Acara ditambahkan.")

    # ----------------------------------------------------
    # 2. Proses Sorting Otomatis
    # ----------------------------------------------------
    
    if not jadwal:
        print("\nTidak ada jadwal yang dimasukkan. Program selesai.")
        return

    print("\n--- PROSES PENGURUTAN JADWAL OTOMATIS ---")
    
    # Python Functions / Lists: Mengurutkan List of Dictionaries
    jadwal.sort(key=lambda x: x['waktu']) 
    
    # ----------------------------------------------------
    # 3. Menampilkan Jadwal yang Sudah Terurut
    # ----------------------------------------------------
    
    print("\n\n*** JADWAL ACARA ANDA (TERURUT) ***")
    
    # Python For Loops: Menampilkan setiap acara
    for event in jadwal:
        print(f"⏰ [{event['waktu']}] | {event['acara']}")
        
    print("---------------------------------------")


# Memulai Program
if __name__ == "__main__":
    buat_jadwal_sortir()
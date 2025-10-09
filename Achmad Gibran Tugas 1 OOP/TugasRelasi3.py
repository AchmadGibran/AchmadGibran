# ==========================
# Implementasi Tugas 3 Gibran
# ==========================

class Perusahaan:
    def __init__(self, nama):
        # inisialisasi perusahaan dengan daftar proyek dan tim
        self.nama = nama
        self.proyek_list = []      # Aggregation: Perusahaan memiliki proyek
        self.tim_list = []         # Composition: Tim bagian dari perusahaan
        pass

    def buat_proyek(self, nama_proyek, deskripsi):
        # buat proyek baru
        proyek = Proyek(nama_proyek, deskripsi)
        self.proyek_list.append(proyek)
        return proyek
        pass

    def buat_tim(self, nama_tim):
        # buat tim baru
        tim = Tim(nama_tim)
        self.tim_list.append(tim)
        return tim
        pass


class Proyek:
    def __init__(self, nama, deskripsi):
        # inisialisasi proyek dengan daftar tugas
        self.nama = nama
        self.deskripsi = deskripsi
        self.tugas_list = []       # Composition: Tugas bagian dari proyek
        pass

    def tambah_tugas(self, deskripsi_tugas):
        # tambahkan tugas ke proyek
        tugas = Tugas(deskripsi_tugas)
        self.tugas_list.append(tugas)
        return tugas
        pass


class Tim:
    def __init__(self, nama):
        # Implementasi: inisialisasi tim dengan daftar developer
        self.nama = nama
        self.developers = []       # Aggregation: Tim memiliki developer
        pass

    def tambah_developer(self, developer):
        # Implementasi: tambahkan developer ke tim
        self.developers.append(developer)
        pass


class Developer:
    def __init__(self, nama, keahlian):
        # Implementasi: inisialisasi developer
        self.nama = nama
        self.keahlian = keahlian
        pass


class Tugas:
    def __init__(self, deskripsi):
        # Implementasi: inisialisasi tugas
        self.deskripsi = deskripsi
        self.developer = None      # Association: Tugas dapat ditugaskan ke developer
        pass

    def tugaskan_ke(self, developer):
        # Implementasi: tugaskan tugas ke developer
        self.developer = developer
        pass


# ==========================
# PROGRAM UTAMA (TESTING)
# ==========================
if __name__ == "__main__":
    # 1. Membuat Perusahaan
    perusahaan = Perusahaan("Tech Innovators")

    # 2. Membuat tim dan menambah developer
    tim_backend = perusahaan.buat_tim("Backend")
    dev1 = Developer("Bram", "Backend Developer")
    dev2 = Developer("Zaldy", "Database Specialist")
    tim_backend.tambah_developer(dev1)
    tim_backend.tambah_developer(dev2)

    tim_frontend = perusahaan.buat_tim("Frontend")
    dev3 = Developer("Gibran", "Frontend Developer")
    tim_frontend.tambah_developer(dev3)

    # 3. Membuat proyek dan menambah tugas
    proyek1 = perusahaan.buat_proyek("Sistem E-Commerce", "Membuat platform belanja online")
    tugas1 = proyek1.tambah_tugas("Membuat API Produk")
    tugas2 = proyek1.tambah_tugas("Mendesain Halaman Utama")

    # 4. Menugaskan tugas ke developer
    tugas1.tugaskan_ke(dev1)
    tugas2.tugaskan_ke(dev3)

    # 5. Menampilkan status proyek dan tugas
    print(f"Perusahaan: {perusahaan.nama}")
    print("\nDaftar Tim dan Developer:")
    for tim in perusahaan.tim_list:
        print(f"- Tim {tim.nama}:")
        for dev in tim.developers:
            print(f"   • {dev.nama} ({dev.keahlian})")

    print("\nDaftar Proyek dan Tugas:")
    for proyek in perusahaan.proyek_list:
        print(f"- Proyek: {proyek.nama} ({proyek.deskripsi})")
        for tugas in proyek.tugas_list:
            if tugas.developer:
                print(f"   • Tugas: {tugas.deskripsi} → Dikerjakan oleh {tugas.developer.nama}")
            else:
                print(f"   • Tugas: {tugas.deskripsi} → Belum ditugaskan")

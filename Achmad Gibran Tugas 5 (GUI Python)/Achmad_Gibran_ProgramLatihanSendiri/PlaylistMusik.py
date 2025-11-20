#Achmad Gibran - 202412003 (Playlist Musik)

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector # Library untuk menghubungkan Python ke database MySQL/MariaDB

class AppPlaylist:
    # Method __init__ adalah konstruktor, yang pertama kali dijalankan saat objek (app) dibuat
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Playlist Musik")
        self.root.geometry("650x450")
        self.root.resizable(False, False)

        # Memanggil method koneksi_db untuk memulai koneksi ke database
        self.koneksi_db() 
        # Memanggil method tampil_ui untuk membuat semua elemen tampilan (GUI)
        self.tampil_ui() 

    # ===================== KONEKSI DATABASE =====================
    def koneksi_db(self):
        try:
            # self.conn akan menyimpan objek koneksi ke database
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root", 
                password="", 
                database="db_playlist" # Pastikan database ini sudah ada di MySQL Anda
            )
            # self.cursor digunakan untuk mengeksekusi perintah (query) SQL
            self.cursor = self.conn.cursor() 
            print("[OK] Koneksi ke database db_playlist berhasil.")
        except mysql.connector.Error as err:
            # Jika koneksi gagal (misalnya XAMPP belum nyala), tampilkan pesan error
            messagebox.showerror("Error", f"Tidak bisa konek ke MySQL:\n{err}")
            self.root.destroy() # Tutup aplikasi jika koneksi gagal

    # ===================== GUI UTAMA =====================
    def tampil_ui(self):
        frame = tk.Frame(self.root, padx=15, pady=10)
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text="🎶 Playlist Musik", font=("Arial", 16, "bold"), fg="blue").pack(pady=5)

        form = tk.Frame(frame)
        form.pack(pady=10)

        # ... (Kode pembuatan Label) ...

        # self.ent_judul, self.ent_penyanyi, dan self.ent_genre menjadi ATTRIBUT objek
        # ini penting agar method lain (seperti tambah_lagu) bisa mengakses isinya
        self.ent_judul = tk.Entry(form, width=40)
        self.ent_penyanyi = tk.Entry(form, width=40)
        
        # ttk.Combobox: Widget dropdown dengan pilihan yang sudah ditentukan
        self.ent_genre = ttk.Combobox(form,
            values=["Pop", "Rock", "Jazz", "Hip-Hop", "Dangdut", "Lainnya"],
            width=37,
            state="readonly" # Agar pengguna hanya bisa memilih dari daftar (tidak mengetik bebas)
        )

        # ... (Kode grid layout untuk form) ...

        tombol_frame = tk.Frame(form)
        tombol_frame.grid(row=3, column=0, columnspan=2, pady=10)

        # command=self.tambah_lagu: Menghubungkan tombol "Tambah" ke method di class ini
        tk.Button(tombol_frame, text="Tambah", width=10, command=self.tambah_lagu).pack(side=tk.LEFT, padx=5)
        tk.Button(tombol_frame, text="Hapus", width=10, command=self.hapus_lagu).pack(side=tk.LEFT, padx=5)
        tk.Button(tombol_frame, text="Bersihkan", width=10, command=self.bersihkan_form).pack(side=tk.LEFT, padx=5)

        # ===================== TABEL LAGU =====================
        # ttk.Treeview: Widget yang digunakan untuk menampilkan data dalam bentuk tabel
        self.tree = ttk.Treeview(frame, columns=("id", "judul", "penyanyi", "genre"), show="headings")
        
        # Penentuan lebar dan judul kolom
        self.tree.column("id", width=40)
        # ... (Penentuan kolom lainnya) ...

        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # BINDING EVENT: Ketika pengguna mengklik (ButtonRelease-1) pada baris tabel,
        # method self.isi_form akan dipanggil untuk mengisi data ke form input
        self.tree.bind("<ButtonRelease-1>", self.isi_form) 

        self.tampil_data() # Panggil method untuk memuat data dari DB saat aplikasi dibuka

    # ===================== CRUD (CREATE, READ, DELETE) =====================
    def tampil_data(self):
        # 1. Menghapus data lama dari tampilan Treeview
        for i in self.tree.get_children():
            self.tree.delete(i)

        # 2. Mengambil data terbaru dari database
        self.cursor.execute("SELECT * FROM playlist ORDER BY id DESC")
        
        # 3. Memasukkan setiap baris data (row) ke dalam tabel Treeview
        for row in self.cursor.fetchall():
            self.tree.insert("", tk.END, values=row) # "" untuk parent, tk.END untuk posisi baris paling bawah

    def tambah_lagu(self):
        # Ambil input dari form
        judul = self.ent_judul.get().strip() 
        penyanyi = self.ent_penyanyi.get().strip()
        genre = self.ent_genre.get().strip()

        if not judul:
            messagebox.showwarning("Peringatan", "Judul lagu harus diisi!")
            return

        # Query SQL INSERT untuk memasukkan data baru ke tabel 'playlist'
        query = "INSERT INTO playlist (judul, penyanyi, genre) VALUES (%s, %s, %s)"
        
        # Eksekusi query dengan data dari form (menggunakan %s untuk mencegah SQL Injection)
        self.cursor.execute(query, (judul, penyanyi, genre))
        
        # COMMIT: Menyimpan (menerapkan) perubahan secara permanen ke database
        self.conn.commit() 

        self.tampil_data()
        self.bersihkan_form()
        messagebox.showinfo("Sukses", f"Lagu '{judul}' berhasil ditambahkan ke playlist!")

    def hapus_lagu(self):
        # Mendapatkan ID baris yang sedang dipilih di Treeview
        selected = self.tree.focus() 
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih lagu yang ingin dihapus!")
            return

        # Mendapatkan semua data dari baris yang dipilih
        data = self.tree.item(selected, "values") 
        id_lagu = data[0] # ID lagu adalah elemen pertama (indeks 0)

        if messagebox.askyesno("Konfirmasi", f"Hapus lagu '{data[1]}' dari playlist?"):
            # Query SQL DELETE berdasarkan ID lagu yang dipilih
            self.cursor.execute("DELETE FROM playlist WHERE id=%s", (id_lagu,))
            self.conn.commit()
            self.tampil_data()
            messagebox.showinfo("Sukses", "Lagu berhasil dihapus.")

    # ===================== UTILITAS =====================
    def isi_form(self, event):
        selected = self.tree.focus()
        if not selected:
            return

        data = self.tree.item(selected, "values")
        
        # Membersihkan form sebelum diisi
        self.ent_judul.delete(0, tk.END) 
        self.ent_penyanyi.delete(0, tk.END)
        self.ent_genre.set("")

        # Memasukkan data dari tabel (indeks 1 untuk judul, 2 untuk penyanyi, 3 untuk genre)
        self.ent_judul.insert(0, data[1]) 
        self.ent_penyanyi.insert(0, data[2])
        self.ent_genre.set(data[3]) # Menggunakan set() untuk Combobox

    def bersihkan_form(self):
        # Menghapus semua teks dari widget Entry dan Combobox
        self.ent_judul.delete(0, tk.END) 
        self.ent_penyanyi.delete(0, tk.END)
        self.ent_genre.set("")

    def jalankan(self):
        # mainloop() adalah inti dari aplikasi Tkinter. Menjaga jendela tetap terbuka
        # dan merespons event dari user (klik tombol, input, dll.)
        self.root.mainloop()


if __name__ == "__main__":
    # Inisiasi objek AppPlaylist (memanggil __init__)
    app = AppPlaylist()
    # Menjalankan aplikasi
    app.jalankan()
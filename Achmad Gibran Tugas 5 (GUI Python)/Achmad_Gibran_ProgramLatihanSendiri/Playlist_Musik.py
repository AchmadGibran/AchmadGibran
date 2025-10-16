#Achmad Gibran - 202412003 (Playlist Musik)

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

class AppPlaylist:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Playlist Musik")
        self.root.geometry("650x450")
        self.root.resizable(False, False)

        self.koneksi_db()
        self.tampil_ui()

    # ===================== KONEKSI DATABASE =====================
    def koneksi_db(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",        # ubah jika MySQL kamu pakai user lain
                password="",        # kosong jika default XAMPP
                database="db_playlist"
            )
            self.cursor = self.conn.cursor()
            print("[OK] Koneksi ke database db_playlist berhasil.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Tidak bisa konek ke MySQL:\n{err}")
            self.root.destroy()

    # ===================== GUI UTAMA =====================
    def tampil_ui(self):
        frame = tk.Frame(self.root, padx=15, pady=10)
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text="🎶 Playlist Musik", font=("Arial", 16, "bold"), fg="blue").pack(pady=5)

        form = tk.Frame(frame)
        form.pack(pady=10)

        tk.Label(form, text="Judul Lagu").grid(row=0, column=0, padx=5, pady=3, sticky="w")
        tk.Label(form, text="Penyanyi").grid(row=1, column=0, padx=5, pady=3, sticky="w")
        tk.Label(form, text="Genre").grid(row=2, column=0, padx=5, pady=3, sticky="w")

        self.ent_judul = tk.Entry(form, width=40)
        self.ent_penyanyi = tk.Entry(form, width=40)
        self.ent_genre = ttk.Combobox(form,
            values=["Pop", "Rock", "Jazz", "Hip-Hop", "Dangdut", "Lainnya"],
            width=37,
            state="readonly"
        )

        self.ent_judul.grid(row=0, column=1, pady=3)
        self.ent_penyanyi.grid(row=1, column=1, pady=3)
        self.ent_genre.grid(row=2, column=1, pady=3)

        tombol_frame = tk.Frame(form)
        tombol_frame.grid(row=3, column=0, columnspan=2, pady=10)

        tk.Button(tombol_frame, text="Tambah", width=10, command=self.tambah_lagu).pack(side=tk.LEFT, padx=5)
        tk.Button(tombol_frame, text="Hapus", width=10, command=self.hapus_lagu).pack(side=tk.LEFT, padx=5)
        tk.Button(tombol_frame, text="Bersihkan", width=10, command=self.bersihkan_form).pack(side=tk.LEFT, padx=5)

        # ===================== TABEL LAGU =====================
        self.tree = ttk.Treeview(frame, columns=("id", "judul", "penyanyi", "genre"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("judul", text="Judul Lagu")
        self.tree.heading("penyanyi", text="Penyanyi")
        self.tree.heading("genre", text="Genre")

        self.tree.column("id", width=40)
        self.tree.column("judul", width=200)
        self.tree.column("penyanyi", width=150)
        self.tree.column("genre", width=100)

        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)
        self.tree.bind("<ButtonRelease-1>", self.isi_form)

        self.tampil_data()

    # ===================== CRUD (CREATE, READ, DELETE) =====================
    def tampil_data(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        self.cursor.execute("SELECT * FROM playlist ORDER BY id DESC")
        for row in self.cursor.fetchall():
            self.tree.insert("", tk.END, values=row)

    def tambah_lagu(self):
        judul = self.ent_judul.get().strip()
        penyanyi = self.ent_penyanyi.get().strip()
        genre = self.ent_genre.get().strip()

        if not judul:
            messagebox.showwarning("Peringatan", "Judul lagu harus diisi!")
            return

        query = "INSERT INTO playlist (judul, penyanyi, genre) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (judul, penyanyi, genre))
        self.conn.commit()

        self.tampil_data()
        self.bersihkan_form()
        messagebox.showinfo("Sukses", f"Lagu '{judul}' berhasil ditambahkan ke playlist!")

    def hapus_lagu(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih lagu yang ingin dihapus!")
            return

        data = self.tree.item(selected, "values")
        id_lagu = data[0]

        if messagebox.askyesno("Konfirmasi", f"Hapus lagu '{data[1]}' dari playlist?"):
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
        self.ent_judul.delete(0, tk.END)
        self.ent_penyanyi.delete(0, tk.END)
        self.ent_genre.set("")

        self.ent_judul.insert(0, data[1])
        self.ent_penyanyi.insert(0, data[2])
        self.ent_genre.set(data[3])

    def bersihkan_form(self):
        self.ent_judul.delete(0, tk.END)
        self.ent_penyanyi.delete(0, tk.END)
        self.ent_genre.set("")

    def jalankan(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = AppPlaylist()
    app.jalankan()

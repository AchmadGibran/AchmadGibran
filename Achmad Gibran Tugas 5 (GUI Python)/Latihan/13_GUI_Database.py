import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

class AppDatabase:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Aplikasi Login + Database")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.koneksi_db()
        self.frame_login()

    def koneksi_db(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",     # ubah jika MySQL kamu punya password
                database="login_db"
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            messagebox.showerror("Koneksi Gagal", f"Error: {err}")

    # ================= Frame Login =====================
    def frame_login(self):
        self.clear_frame()
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)

        tk.Label(frame, text="Login", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(frame, text="Username").grid(row=1, column=0, sticky=tk.W, pady=5)
        tk.Label(frame, text="Password").grid(row=2, column=0, sticky=tk.W, pady=5)

        self.ent_user = tk.Entry(frame, width=25)
        self.ent_pass = tk.Entry(frame, width=25, show="*")
        self.ent_user.grid(row=1, column=1, pady=5)
        self.ent_pass.grid(row=2, column=1, pady=5)

        tk.Button(frame, text="Login", width=15, command=self.login).grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        user = self.ent_user.get()
        pw = self.ent_pass.get()

        if not user or not pw:
            messagebox.showwarning("Peringatan", "Isi username dan password!")
            return

        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        self.cursor.execute(query, (user, pw))
        data = self.cursor.fetchone()

        if data:
            messagebox.showinfo("Sukses", f"Selamat datang, {user}")
            self.frame_dashboard()
        else:
            messagebox.showerror("Gagal", "Username atau password salah!")

    # ================= Dashboard =====================
    def frame_dashboard(self):
        self.clear_frame()
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Dashboard", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Button(frame, text="Manajemen User", width=20, command=self.frame_user).pack(pady=5)
        tk.Button(frame, text="Logout", width=20, command=self.frame_login).pack(pady=5)

    # ================= Manajemen User CRUD =====================
    def frame_user(self):
        self.clear_frame()
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Manajemen User", font=("Arial", 14, "bold")).pack(pady=5)

        form = tk.Frame(frame)
        form.pack(pady=5)

        tk.Label(form, text="Username").grid(row=0, column=0, padx=5, pady=2)
        tk.Label(form, text="Password").grid(row=1, column=0, padx=5, pady=2)

        self.ent_user_m = tk.Entry(form)
        self.ent_pass_m = tk.Entry(form, show="*")
        self.ent_user_m.grid(row=0, column=1, pady=2)
        self.ent_pass_m.grid(row=1, column=1, pady=2)

        btn_frame = tk.Frame(form)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=5)
        tk.Button(btn_frame, text="Simpan", command=self.simpan_user).pack(side=tk.LEFT, padx=3)
        tk.Button(btn_frame, text="Hapus", command=self.hapus_user).pack(side=tk.LEFT, padx=3)
        tk.Button(btn_frame, text="Kembali", command=self.frame_dashboard).pack(side=tk.LEFT, padx=3)

        # Table view
        self.tree = ttk.Treeview(frame, columns=("id", "username", "password"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("username", text="Username")
        self.tree.heading("password", text="Password")
        self.tree.pack(fill=tk.BOTH, expand=True, pady=5)
        self.tree.bind("<ButtonRelease-1>", self.isi_form_user)

        self.tampil_user()

    def tampil_user(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        self.cursor.execute("SELECT * FROM users")
        for data in self.cursor.fetchall():
            self.tree.insert("", tk.END, values=data)

    def simpan_user(self):
        username = self.ent_user_m.get()
        password = self.ent_pass_m.get()
        if not username or not password:
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return

        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        self.cursor.execute(query, (username, password))
        self.conn.commit()
        self.tampil_user()
        self.ent_user_m.delete(0, tk.END)
        self.ent_pass_m.delete(0, tk.END)
        messagebox.showinfo("Sukses", "Data user berhasil disimpan")

    def hapus_user(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih user yang akan dihapus!")
            return

        data = self.tree.item(selected, "values")
        id_user = data[0]
        query = "DELETE FROM users WHERE id=%s"
        self.cursor.execute(query, (id_user,))
        self.conn.commit()
        self.tampil_user()
        messagebox.showinfo("Sukses", "User berhasil dihapus")

    def isi_form_user(self, event):
        selected = self.tree.focus()
        if not selected:
            return
        data = self.tree.item(selected, "values")
        self.ent_user_m.delete(0, tk.END)
        self.ent_pass_m.delete(0, tk.END)
        self.ent_user_m.insert(0, data[1])
        self.ent_pass_m.insert(0, data[2])

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def jalankan(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = AppDatabase()
    app.jalankan()

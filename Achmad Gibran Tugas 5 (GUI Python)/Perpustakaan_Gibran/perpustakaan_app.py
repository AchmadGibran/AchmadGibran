# perpustakaan_app.py
# UI: Admin Dashboard modern (minimalis putih + aksen biru)
# Fitur sesuai tugas: Login (users), Dashboard (cards), Manajemen Buku (CRUD + search), Manajemen Anggota (CRUD)
# DB_CONFIG diset untuk environment tanpa password (sesuaikan bila berubah)

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error
import datetime

# -------------------------
# CONFIG (sesuaikan jika perlu)
# -------------------------
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',   # kosong karena Anda menyebut tidak memakai password
    'database': 'perpustakaan_db'
}
# warna tema
ACCENT = "#2B6EA3"       # biru aksen
ACCENT_LIGHT = "#E9F2FA" # very light blue
CARD_BG = "#FFFFFF"
TEXT_COLOR = "#222222"

# -------------------------
# DATABASE WRAPPER
# -------------------------
class Database:
    def __init__(self, config):
        self.config = config

    def connect(self):
        return mysql.connector.connect(**self.config)

db = Database(DB_CONFIG)

# -------------------------
# UTIL
# -------------------------
def center_window(win, width=1000, height=650):
    screen_w = win.winfo_screenwidth()
    screen_h = win.winfo_screenheight()
    x = (screen_w // 2) - (width // 2)
    y = (screen_h // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

# -------------------------
# APP
# -------------------------
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Perpustakaan — Admin Dashboard")
        center_window(self, 1100, 700)
        self.minsize(1000, 620)
        self.configure(bg="#f6f9fc")
        self.current_user = None

        # ttk style
        self.style = ttk.Style(self)
        try:
            self.style.theme_use('clam')
        except:
            pass
        default_font = ("Segoe UI", 10)
        self.option_add("*Font", default_font)

        # custom style for buttons
        self.style.configure("Accent.TButton", background=ACCENT, foreground="white", padding=6)
        self.style.map("Accent.TButton",
                       foreground=[('active', 'white')],
                       background=[('active', ACCENT)])
        self.style.configure("TFrame", background="#f6f9fc")
        self.style.configure("Card.TFrame", background=CARD_BG)
        self.style.configure("Header.TLabel", font=("Segoe UI", 14, "bold"), background="#f6f9fc")
        self.style.configure("CardTitle.TLabel", font=("Segoe UI", 11, "bold"), background=CARD_BG)
        self.style.configure("CardValue.TLabel", font=("Segoe UI", 20, "bold"), background=CARD_BG)

        # start with login screen
        self._build_login()

    # -------------------------
    # LOGIN
    # -------------------------
    def _build_login(self):
        for w in self.winfo_children():
            w.destroy()

        container = ttk.Frame(self, padding=20, style="TFrame")
        container.place(relx=0.5, rely=0.5, anchor='center')

        card = tk.Frame(container, bg=CARD_BG, bd=1, relief="flat")
        card.pack(ipadx=30, ipady=18)

        # header
        header = ttk.Label(card, text="Masuk — Sistem Perpustakaan", style="Header.TLabel")
        header.grid(row=0, column=0, columnspan=2, pady=(4,12))

        # form
        ttk.Label(card, text="Username:").grid(row=1, column=0, sticky='e', padx=(8,6), pady=6)
        self.username_var = tk.StringVar()
        ttk.Entry(card, textvariable=self.username_var, width=30).grid(row=1, column=1, sticky='w', padx=(6,10))

        ttk.Label(card, text="Password:").grid(row=2, column=0, sticky='e', padx=(8,6), pady=6)
        self.password_var = tk.StringVar()
        ttk.Entry(card, textvariable=self.password_var, show="*", width=30).grid(row=2, column=1, sticky='w', padx=(6,10))

        self.login_msg = ttk.Label(card, text="", foreground="red", background=CARD_BG)
        self.login_msg.grid(row=3, column=0, columnspan=2, pady=(6,0))

        btn_frame = ttk.Frame(card, style="TFrame")
        btn_frame.grid(row=4, column=0, columnspan=2, pady=(12,0))
        accent_btn = ttk.Button(btn_frame, text="Login", style="Accent.TButton", command=self.do_login)
        accent_btn.grid(row=0, column=0, padx=(0,8))
        ttk.Button(btn_frame, text="Keluar", command=self.quit).grid(row=0, column=1)

        # helper note at bottom
        note = ttk.Label(card, text="Gunakan akun admin", background=CARD_BG)
        note.grid(row=5, column=0, columnspan=2, pady=(12,0))

    def do_login(self):
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        if not username or not password:
            self.login_msg.config(text="Username dan password tidak boleh kosong.")
            return
        # test connection
        try:
            conn = db.connect()
        except Exception as e:
            messagebox.showerror("Koneksi Database", f"Gagal terhubung ke database. Periksa DB_CONFIG.\n{e}")
            return
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT id, username, role FROM users WHERE username=%s AND password=%s", (username, password))
            user = cursor.fetchone()
            cursor.close()
            conn.close()
            if user:
                self.current_user = user
                self.build_main()
            else:
                self.login_msg.config(text="Username atau password salah.")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi error saat autentikasi:\n{e}")

    # -------------------------
    # MAIN LAYOUT (sidebar + content)
    # -------------------------
    def build_main(self):
        for w in self.winfo_children():
            w.destroy()

        # top header
        header = tk.Frame(self, bg=CARD_BG, height=60)
        header.pack(side='top', fill='x')
        header.pack_propagate(False)
        title = tk.Label(header, text="Perpustakaan — Dashboard", bg=CARD_BG, fg=TEXT_COLOR, font=("Segoe UI", 14, "bold"))
        title.pack(side='left', padx=16)
        user_label = tk.Label(header, text=f"Signed in: {self.current_user['username']}", bg=CARD_BG, fg="#555555")
        user_label.pack(side='right', padx=16)
        logout_btn = ttk.Button(header, text="Logout", command=self.logout)
        logout_btn.pack(side='right', padx=(0,8))

        # main area
        main_area = tk.Frame(self, bg="#f6f9fc")
        main_area.pack(side='top', fill='both', expand=True)

        # sidebar
        sidebar = tk.Frame(main_area, bg="#ffffff", width=220, bd=0)
        sidebar.pack(side='left', fill='y')
        sidebar.pack_propagate(False)
        # logo area
        logo = tk.Frame(sidebar, bg=ACCENT, height=80)
        logo.pack(fill='x')
        logo_label = tk.Label(logo, text="PERPUSTAKAAN", bg=ACCENT, fg="white", font=("Segoe UI", 13, "bold"))
        logo_label.pack(padx=10, pady=18)

        # menu buttons
        menu_frame = tk.Frame(sidebar, bg="#ffffff")
        menu_frame.pack(fill='both', expand=True, pady=10)

        btn_dash = ttk.Button(menu_frame, text="Dashboard", width=24, command=self.show_dashboard)
        btn_book = ttk.Button(menu_frame, text="Manajemen Buku", width=24, command=self.show_buku)
        btn_member = ttk.Button(menu_frame, text="Manajemen Anggota", width=24, command=self.show_anggota)
        btn_dash.pack(pady=6, padx=12)
        btn_book.pack(pady=6, padx=12)
        btn_member.pack(pady=6, padx=12)

        # content area
        self.content = tk.Frame(main_area, bg="#f6f9fc")
        self.content.pack(side='left', fill='both', expand=True, padx=16, pady=12)

        self.show_dashboard()

    def logout(self):
        self.current_user = None
        self._build_login()

    # -------------------------
    # DASHBOARD (cards)
    # -------------------------
    def show_dashboard(self):
        for w in self.content.winfo_children():
            w.destroy()

        # top welcome + date
        header_frame = tk.Frame(self.content, bg="#f6f9fc")
        header_frame.pack(fill='x', pady=(4,12))
        welcome = tk.Label(header_frame, text=f"Selamat Datang, {self.current_user['username']}", bg="#f6f9fc", fg=TEXT_COLOR, font=("Segoe UI", 16, "bold"))
        welcome.pack(side='left')
        today = datetime.datetime.now().strftime("%A, %d %B %Y")
        date_label = tk.Label(header_frame, text=today, bg="#f6f9fc", fg="#666666")
        date_label.pack(side='right')

        # cards frame
        cards = tk.Frame(self.content, bg="#f6f9fc")
        cards.pack(fill='x', pady=(4,12))

        # Card helper
        def make_card(parent, icon, title, value):
            c = tk.Frame(parent, bg=CARD_BG, bd=1, relief="flat")
            c.pack(side='left', padx=8, ipadx=10, ipady=10, expand=True, fill='x')
            top = tk.Frame(c, bg=CARD_BG)
            top.pack(fill='x')
            icon_lbl = tk.Label(top, text=icon, bg=CARD_BG, font=("Segoe UI", 18))
            icon_lbl.pack(side='left')
            title_lbl = tk.Label(top, text=title, bg=CARD_BG, fg="#666666")
            title_lbl.pack(side='left', padx=8)
            val_lbl = tk.Label(c, text=value, bg=CARD_BG, fg=ACCENT, font=("Segoe UI", 20, "bold"))
            val_lbl.pack(anchor='w', padx=8, pady=(10,6))
            return c

        # fetch counts
        try:
            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM buku")
            total_buku = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM anggota")
            total_anggota = cursor.fetchone()[0]
            cursor.close()
            conn.close()
        except Exception:
            total_buku = "—"
            total_anggota = "—"

        make_card(cards, "📘", "Total Buku", total_buku)
        make_card(cards, "👥", "Total Anggota", total_anggota)
        make_card(cards, "🕒", "Waktu Sistem", datetime.datetime.now().strftime("%H:%M"))

        # quick actions
        qa = tk.Frame(self.content, bg="#f6f9fc")
        qa.pack(fill='x', pady=(10,0))
        ttk.Button(qa, text="Tambah Buku Baru", style="Accent.TButton", command=self.show_buku).pack(side='left', padx=6)
        ttk.Button(qa, text="Tambah Anggota Baru", style="Accent.TButton", command=self.show_anggota).pack(side='left', padx=6)

    # -------------------------
    # MANAGEMEN BUKU
    # -------------------------
    def show_buku(self):
        for w in self.content.winfo_children():
            w.destroy()

        top = tk.Frame(self.content, bg="#f6f9fc")
        top.pack(fill='x')
        title = tk.Label(top, text="Manajemen Buku", bg="#f6f9fc", fg=TEXT_COLOR, font=("Segoe UI", 14, "bold"))
        title.pack(side='left')

        container = tk.Frame(self.content, bg="#f6f9fc")
        container.pack(fill='both', expand=True, pady=(8,0))

        # left form
        form = tk.Frame(container, bg=CARD_BG, bd=1, relief="flat")
        form.pack(side='top', fill='x', padx=4, pady=4)

        # fields
        self.b_kode = tk.StringVar()
        self.b_judul = tk.StringVar()
        self.b_pengarang = tk.StringVar()
        self.b_penerbit = tk.StringVar()
        self.b_tahun = tk.StringVar()
        self.b_stok = tk.StringVar()

        lbl_opts = {'bg': CARD_BG}
        entry_w = 34
        r = 0
        tk.Label(form, text="Kode Buku:", **lbl_opts).grid(row=r, column=0, sticky='e', padx=8, pady=6)
        ttk.Entry(form, textvariable=self.b_kode, width=20).grid(row=r, column=1, sticky='w', padx=8)
        tk.Label(form, text="Judul:", **lbl_opts).grid(row=r, column=2, sticky='e', padx=8, pady=6)
        ttk.Entry(form, textvariable=self.b_judul, width=entry_w).grid(row=r, column=3, sticky='w', padx=8)
        r += 1
        tk.Label(form, text="Pengarang:", **lbl_opts).grid(row=r, column=0, sticky='e', padx=8, pady=6)
        ttk.Entry(form, textvariable=self.b_pengarang, width=30).grid(row=r, column=1, sticky='w', padx=8)
        tk.Label(form, text="Penerbit:", **lbl_opts).grid(row=r, column=2, sticky='e', padx=8, pady=6)
        ttk.Entry(form, textvariable=self.b_penerbit, width=30).grid(row=r, column=3, sticky='w', padx=8)
        r += 1
        tk.Label(form, text="Tahun Terbit:", **lbl_opts).grid(row=r, column=0, sticky='e', padx=8, pady=6)
        ttk.Entry(form, textvariable=self.b_tahun, width=12).grid(row=r, column=1, sticky='w', padx=8)
        tk.Label(form, text="Stok:", **lbl_opts).grid(row=r, column=2, sticky='e', padx=8, pady=6)
        ttk.Entry(form, textvariable=self.b_stok, width=10).grid(row=r, column=3, sticky='w', padx=8)
        r += 1

        btn_frame = tk.Frame(form, bg=CARD_BG)
        btn_frame.grid(row=r, column=0, columnspan=4, pady=(8,10))
        ttk.Button(btn_frame, text="Tambah", style="Accent.TButton", command=self.add_buku).grid(row=0, column=0, padx=6)
        ttk.Button(btn_frame, text="Update", command=self.update_buku).grid(row=0, column=1, padx=6)
        ttk.Button(btn_frame, text="Hapus", command=self.delete_buku).grid(row=0, column=2, padx=6)
        ttk.Button(btn_frame, text="Bersihkan", command=self.clear_buku_form).grid(row=0, column=3, padx=6)

        # search + treeview
        bottom = tk.Frame(container, bg="#f6f9fc")
        bottom.pack(fill='both', expand=True, padx=4, pady=(8,4))

        search_frame = tk.Frame(bottom, bg="#f6f9fc")
        search_frame.pack(fill='x')
        tk.Label(search_frame, text="Cari (judul / pengarang):", bg="#f6f9fc").pack(side='left')
        self.search_buku_var = tk.StringVar()
        ttk.Entry(search_frame, textvariable=self.search_buku_var, width=40).pack(side='left', padx=8)
        ttk.Button(search_frame, text="Cari", command=self.search_buku).pack(side='left', padx=6)
        ttk.Button(search_frame, text="Refresh", command=self.load_buku).pack(side='left', padx=6)

        cols = ("kode_buku","judul","pengarang","penerbit","tahun_terbit","stok")
        self.tree_buku = ttk.Treeview(bottom, columns=cols, show='headings', height=12)
        for c in cols:
            self.tree_buku.heading(c, text=c.replace('_',' ').title())
            self.tree_buku.column(c, anchor='w', width=150)
        vsb = ttk.Scrollbar(bottom, orient="vertical", command=self.tree_buku.yview)
        self.tree_buku.configure(yscrollcommand=vsb.set)
        vsb.pack(side='right', fill='y')
        self.tree_buku.pack(fill='both', expand=True, side='left')
        self.tree_buku.bind("<<TreeviewSelect>>", self.on_buku_select)

        self.load_buku()

    def load_buku(self):
        for i in self.tree_buku.get_children():
            self.tree_buku.delete(i)
        try:
            conn = db.connect()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT kode_buku, judul, pengarang, penerbit, tahun_terbit, stok FROM buku ORDER BY judul")
            rows = cursor.fetchall()
            for r in rows:
                self.tree_buku.insert('', 'end', values=(r['kode_buku'], r['judul'], r['pengarang'], r['penerbit'], r['tahun_terbit'], r['stok']))
            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Gagal memuat data buku:\n{e}")

    def on_buku_select(self, event):
        sel = self.tree_buku.selection()
        if not sel: return
        vals = self.tree_buku.item(sel[0])['values']
        self.b_kode.set(vals[0]); self.b_judul.set(vals[1])
        self.b_pengarang.set(vals[2]); self.b_penerbit.set(vals[3])
        self.b_tahun.set(vals[4]); self.b_stok.set(vals[5])

    def clear_buku_form(self):
        self.b_kode.set(''); self.b_judul.set(''); self.b_pengarang.set('')
        self.b_penerbit.set(''); self.b_tahun.set(''); self.b_stok.set('')

    def validate_buku(self, kode, judul, pengarang, penerbit, tahun, stok, check_unique=True):
        if not (kode and judul and pengarang and penerbit and tahun and stok):
            messagebox.showwarning("Validasi", "Semua field buku harus diisi.")
            return False
        if not tahun.isdigit():
            messagebox.showwarning("Validasi", "Tahun terbit harus angka.")
            return False
        if not stok.isdigit() or int(stok) < 0:
            messagebox.showwarning("Validasi", "Stok harus angka positif (>=0).")
            return False
        if check_unique:
            try:
                conn = db.connect()
                cursor = conn.cursor()
                cursor.execute("SELECT id FROM buku WHERE kode_buku=%s", (kode,))
                found = cursor.fetchone()
                cursor.close()
                conn.close()
                if found:
                    messagebox.showwarning("Validasi", "Kode buku sudah ada (harus unik).")
                    return False
            except Exception as e:
                messagebox.showerror("Error", f"Error saat validasi:\n{e}")
                return False
        return True

    def add_buku(self):
        kode = self.b_kode.get().strip()
        judul = self.b_judul.get().strip()
        pengarang = self.b_pengarang.get().strip()
        penerbit = self.b_penerbit.get().strip()
        tahun = self.b_tahun.get().strip()
        stok = self.b_stok.get().strip()
        if not self.validate_buku(kode, judul, pengarang, penerbit, tahun, stok, check_unique=True):
            return
        try:
            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO buku (kode_buku, judul, pengarang, penerbit, tahun_terbit, stok)
                              VALUES (%s,%s,%s,%s,%s,%s)""",
                           (kode, judul, pengarang, penerbit, int(tahun), int(stok)))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Sukses", "Data buku berhasil ditambahkan.")
            self.load_buku()
            self.clear_buku_form()
        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", "Kode buku harus unik.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menambahkan buku:\n{e}")

    def update_buku(self):
        kode = self.b_kode.get().strip()
        if not kode:
            messagebox.showwarning("Validasi", "Pilih atau masukkan Kode Buku untuk update.")
            return
        judul = self.b_judul.get().strip()
        pengarang = self.b_pengarang.get().strip()
        penerbit = self.b_penerbit.get().strip()
        tahun = self.b_tahun.get().strip()
        stok = self.b_stok.get().strip()
        if not self.validate_buku(kode, judul, pengarang, penerbit, tahun, stok, check_unique=False):
            return
        try:
            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute("""UPDATE buku SET judul=%s, pengarang=%s, penerbit=%s, tahun_terbit=%s, stok=%s
                              WHERE kode_buku=%s""",
                           (judul, pengarang, penerbit, int(tahun), int(stok), kode))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Sukses", "Data buku berhasil diupdate.")
            self.load_buku()
            self.clear_buku_form()
        except Exception as e:
            messagebox.showerror("Error", f"Gagal update buku:\n{e}")

    def delete_buku(self):
        kode = self.b_kode.get().strip()
        if not kode:
            messagebox.showwarning("Hapus", "Pilih buku untuk dihapus (masukkan kode).")
            return
        if not messagebox.askyesno("Konfirmasi", f"Hapus buku dengan kode {kode}?"):
            return
        try:
            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM buku WHERE kode_buku=%s", (kode,))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Sukses", "Data buku berhasil dihapus.")
            self.load_buku()
            self.clear_buku_form()
        except Exception as e:
            messagebox.showerror("Error", f"Gagal hapus buku:\n{e}")

    def search_buku(self):
        key = self.search_buku_var.get().strip()
        for i in self.tree_buku.get_children():
            self.tree_buku.delete(i)
        try:
            conn = db.connect()
            cursor = conn.cursor(dictionary=True)
            like = f"%{key}%"
            cursor.execute("""SELECT kode_buku, judul, pengarang, penerbit, tahun_terbit, stok
                              FROM buku WHERE judul LIKE %s OR pengarang LIKE %s ORDER BY judul""",
                           (like, like))
            rows = cursor.fetchall()
            for r in rows:
                self.tree_buku.insert('', 'end', values=(r['kode_buku'], r['judul'], r['pengarang'], r['penerbit'], r['tahun_terbit'], r['stok']))
            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mencari buku:\n{e}")

    # -------------------------
    # MANAGEMEN ANGGOTA
    # -------------------------
    def show_anggota(self):
        for w in self.content.winfo_children():
            w.destroy()

        top = tk.Frame(self.content, bg="#f6f9fc")
        top.pack(fill='x')
        title = tk.Label(top, text="Manajemen Anggota", bg="#f6f9fc", fg=TEXT_COLOR, font=("Segoe UI", 14, "bold"))
        title.pack(side='left')

        container = tk.Frame(self.content, bg="#f6f9fc")
        container.pack(fill='both', expand=True, pady=(8,0))

        form = tk.Frame(container, bg=CARD_BG, bd=1, relief="flat")
        form.pack(side='top', fill='x', padx=4, pady=4)

        self.a_kode = tk.StringVar()
        self.a_nama = tk.StringVar()
        self.a_alamat = tk.StringVar()
        self.a_telepon = tk.StringVar()
        self.a_email = tk.StringVar()

        lbl_opts = {'bg': CARD_BG}
        entry_w = 40
        r = 0
        tk.Label(form, text="Kode Anggota:", **lbl_opts).grid(row=r, column=0, sticky='e', padx=8, pady=6)
        ttk.Entry(form, textvariable=self.a_kode, width=20).grid(row=r, column=1, sticky='w', padx=8)
        tk.Label(form, text="Nama:", **lbl_opts).grid(row=r, column=2, sticky='e', padx=8, pady=6)
        ttk.Entry(form, textvariable=self.a_nama, width=entry_w).grid(row=r, column=3, sticky='w', padx=8)
        r += 1
        tk.Label(form, text="Alamat:", **lbl_opts).grid(row=r, column=0, sticky='e', padx=8, pady=6)
        ttk.Entry(form, textvariable=self.a_alamat, width=80).grid(row=r, column=1, columnspan=3, sticky='w', padx=8)
        r += 1
        tk.Label(form, text="Telepon:", **lbl_opts).grid(row=r, column=0, sticky='e', padx=8, pady=6)
        ttk.Entry(form, textvariable=self.a_telepon, width=20).grid(row=r, column=1, sticky='w', padx=8)
        tk.Label(form, text="Email:", **lbl_opts).grid(row=r, column=2, sticky='e', padx=8, pady=6)
        ttk.Entry(form, textvariable=self.a_email, width=entry_w).grid(row=r, column=3, sticky='w', padx=8)
        r += 1

        btn_frame = tk.Frame(form, bg=CARD_BG)
        btn_frame.grid(row=r, column=0, columnspan=4, pady=(8,10))
        ttk.Button(btn_frame, text="Tambah", style="Accent.TButton", command=self.add_anggota).grid(row=0, column=0, padx=6)
        ttk.Button(btn_frame, text="Update", command=self.update_anggota).grid(row=0, column=1, padx=6)
        ttk.Button(btn_frame, text="Hapus", command=self.delete_anggota).grid(row=0, column=2, padx=6)
        ttk.Button(btn_frame, text="Bersihkan", command=self.clear_anggota_form).grid(row=0, column=3, padx=6)

        bottom = tk.Frame(container, bg="#f6f9fc")
        bottom.pack(fill='both', expand=True, padx=4, pady=(8,4))

        cols = ("kode_anggota","nama","alamat","telepon","email")
        self.tree_anggota = ttk.Treeview(bottom, columns=cols, show='headings', height=12)
        for c in cols:
            self.tree_anggota.heading(c, text=c.replace('_',' ').title())
            self.tree_anggota.column(c, anchor='w', width=180)
        vsb = ttk.Scrollbar(bottom, orient="vertical", command=self.tree_anggota.yview)
        self.tree_anggota.configure(yscrollcommand=vsb.set)
        vsb.pack(side='right', fill='y')
        self.tree_anggota.pack(fill='both', expand=True, side='left')
        self.tree_anggota.bind("<<TreeviewSelect>>", self.on_anggota_select)

        self.load_anggota()

    def load_anggota(self):
        for i in self.tree_anggota.get_children():
            self.tree_anggota.delete(i)
        try:
            conn = db.connect()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT kode_anggota, nama, alamat, telepon, email FROM anggota ORDER BY nama")
            rows = cursor.fetchall()
            for r in rows:
                self.tree_anggota.insert('', 'end', values=(r['kode_anggota'], r['nama'], r['alamat'], r['telepon'], r['email']))
            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Gagal memuat data anggota:\n{e}")

    def on_anggota_select(self, event):
        sel = self.tree_anggota.selection()
        if not sel: return
        vals = self.tree_anggota.item(sel[0])['values']
        self.a_kode.set(vals[0]); self.a_nama.set(vals[1])
        self.a_alamat.set(vals[2]); self.a_telepon.set(vals[3]); self.a_email.set(vals[4])

    def clear_anggota_form(self):
        self.a_kode.set(''); self.a_nama.set(''); self.a_alamat.set(''); self.a_telepon.set(''); self.a_email.set('')

    def validate_email(self, email):
        return '@' in email and '.' in email.split('@')[-1]

    def validate_anggota(self, kode, nama, alamat, telepon, email, check_unique=True):
        if not (kode and nama and alamat and telepon):
            messagebox.showwarning("Validasi", "Field kode, nama, alamat, telepon harus diisi.")
            return False
        if not telepon.isdigit():
            messagebox.showwarning("Validasi", "Telepon harus berupa angka.")
            return False
        if email and not self.validate_email(email):
            messagebox.showwarning("Validasi", "Format email tidak valid.")
            return False
        if check_unique:
            try:
                conn = db.connect()
                cursor = conn.cursor()
                cursor.execute("SELECT id FROM anggota WHERE kode_anggota=%s", (kode,))
                found = cursor.fetchone()
                cursor.close()
                conn.close()
                if found:
                    messagebox.showwarning("Validasi", "Kode anggota sudah ada (harus unik).")
                    return False
            except Exception as e:
                messagebox.showerror("Error", f"Error saat validasi anggota:\n{e}")
                return False
        return True

    def add_anggota(self):
        kode = self.a_kode.get().strip()
        nama = self.a_nama.get().strip()
        alamat = self.a_alamat.get().strip()
        telepon = self.a_telepon.get().strip()
        email = self.a_email.get().strip()
        if not self.validate_anggota(kode, nama, alamat, telepon, email, check_unique=True):
            return
        try:
            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO anggota (kode_anggota, nama, alamat, telepon, email)
                              VALUES (%s,%s,%s,%s,%s)""",
                           (kode, nama, alamat, telepon, email if email else None))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Sukses", "Data anggota berhasil ditambahkan.")
            self.load_anggota()
            self.clear_anggota_form()
        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", "Kode anggota harus unik.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menambahkan anggota:\n{e}")

    def update_anggota(self):
        kode = self.a_kode.get().strip()
        if not kode:
            messagebox.showwarning("Validasi", "Pilih atau masukkan kode anggota untuk update.")
            return
        nama = self.a_nama.get().strip()
        alamat = self.a_alamat.get().strip()
        telepon = self.a_telepon.get().strip()
        email = self.a_email.get().strip()
        if not self.validate_anggota(kode, nama, alamat, telepon, email, check_unique=False):
            return
        try:
            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute("""UPDATE anggota SET nama=%s, alamat=%s, telepon=%s, email=%s
                              WHERE kode_anggota=%s""",
                           (nama, alamat, telepon, email if email else None, kode))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Sukses", "Data anggota berhasil diupdate.")
            self.load_anggota()
            self.clear_anggota_form()
        except Exception as e:
            messagebox.showerror("Error", f"Gagal update anggota:\n{e}")

    def delete_anggota(self):
        kode = self.a_kode.get().strip()
        if not kode:
            messagebox.showwarning("Hapus", "Pilih anggota untuk dihapus (masukkan kode).")
            return
        if not messagebox.askyesno("Konfirmasi", f"Hapus anggota dengan kode {kode}?"):
            return
        try:
            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM anggota WHERE kode_anggota=%s", (kode,))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Sukses", "Data anggota berhasil dihapus.")
            self.load_anggota()
            self.clear_anggota_form()
        except Exception as e:
            messagebox.showerror("Error", f"Gagal hapus anggota:\n{e}")

# -------------------------
# START APP
# -------------------------
if __name__ == "__main__":
    # quick connection check with informative error
    try:
        conn_test = db.connect()
        conn_test.close()
    except Exception as e:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Koneksi Database", f"Gagal terhubung ke database. Pastikan MySQL berjalan dan database 'perpustakaan_db' sudah dibuat.\n\nDetail error:\n{e}")
        raise SystemExit(1)

    app = App()
    app.mainloop()

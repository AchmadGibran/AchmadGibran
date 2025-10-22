# 📚 Sistem Manajemen Perpustakaan (GUI Python & MySQL)

[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Database Backend](https://img.shields.io/badge/Database-MySQL-orange.svg)](https://www.mysql.com/)
[![GUI Framework](https://img.shields.io/badge/GUI-Tkinter-green.svg)]()

## 📝 Overview

Aplikasi ini adalah **Sistem Informasi Manajemen Perpustakaan** berbasis *Desktop* yang dikembangkan menggunakan **Python (Tkinter)** untuk antarmuka pengguna grafis (GUI) dan **MySQL** sebagai sistem basis data.

Sistem ini dirancang untuk menyediakan alat yang efisien bagi administrator dan petugas untuk mengelola otentikasi pengguna, inventaris buku, dan data anggota secara terpusat.

---

## 🚀 Fitur Utama Aplikasi

### 1. Sistem Akses dan Otentikasi
* **Login Aman:** Memverifikasi kredensial pengguna terhadap data yang tersimpan dalam tabel `users`.
* **Manajemen Sesi:** Setelah *login* berhasil, aplikasi mempertahankan dan menampilkan identitas pengguna yang sedang aktif (contoh: "Signed in: admin").
* **Penanganan Error:** Menyediakan pesan *error* yang informatif jika terjadi kegagalan koneksi ke server database atau kegagalan otentikasi.

### 2. Dashboard
* **Tampilan Sesi:** Menyambut pengguna dengan nama akun yang aktif.
* **Statistik Real-time:** Menampilkan ringkasan cepat (jumlah total Buku dan Anggota) yang diperbarui secara *real-time*.

### 3. Manajemen Inventaris Buku (CRUD)
Modul lengkap untuk **Create, Read, Update, dan Delete (CRUD)** data buku.
* **Validasi Data Kritis:** Menerapkan validasi untuk memastikan Kode Buku unik, Tahun Terbit berupa angka, dan Stok bernilai positif.
* **Pencarian:** Mendukung pencarian data berdasarkan Judul atau Pengarang.
* **Tampilan:** Menggunakan komponen Treeview untuk visualisasi data tabular yang rapi.

### 4. Manajemen Data Anggota (CRUD)
Modul lengkap untuk mengelola data anggota perpustakaan.
* **Validasi Data Kritis:** Menerapkan validasi untuk memastikan Kode Anggota unik, Nomor Telepon hanya berisi angka, dan format Email valid.

---

## ⚙️ Persyaratan Teknis (Prerequisites)

Untuk menjalankan proyek ini, Anda membutuhkan:
1.  **Python 3.x**
2.  **MySQL Server** atau **MariaDB** (Harus aktif saat aplikasi dijalankan).
3.  **Library Python:** Instal konektor MySQL:
    ```bash
    pip install mysql-connector-python
    ```

---

## 💾 Setup Database

Aplikasi berinteraksi dengan database bernama **`perpustakaan_db`**.

### 1. Struktur Database
Database terdiri dari tabel `users`, `buku`, dan `anggota`. Detail struktur tabel (kolom, tipe data, dan kunci unik) terdapat di file **`database_setup.sql`**.

### 2. Eksekusi Skrip SQL
Untuk membuat database dan mengisi data awal:
* Pastikan MySQL Server Anda berjalan.
* Jalankan file **`database_setup.sql`** melalui MySQL CLI atau antarmuka GUI seperti phpMyAdmin.

#### 🔑 Kredensial Akses Awal
Setelah skrip SQL dijalankan, Anda dapat *login* menggunakan akun administrator awal:

| Username | Password |
| :---: | :---: |
| `admin` | `admin123` |

---

## ▶️ Panduan Penggunaan

1.  Pastikan semua persyaratan teknis dan *setup* database sudah lengkap.
2.  Jalankan aplikasi utama dari Terminal atau Command Prompt:
    ```bash
    python perpustakaan_app.py
    ```
3.  Aplikasi akan menampilkan jendela *login*. Gunakan kredensial di atas untuk memulai.
import tkinter as tk
from tkinter import messagebox

class WindowDasar:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Aplikasi GUI")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        label = tk.Label(self.root, text="Selamat Datang!", font=("Arial", 16), fg="blue")
        label.pack(pady=20)

        button = tk.Button(self.root, text="Klik Saya!", font=("Arial", 12), bg="lightgray", command=self.tombol_diklik)
        button.pack(pady=10)

    def tombol_diklik(self):
        messagebox.showinfo("Info", "Tombol telah diklik!")

    def jalankan(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = WindowDasar()
    app.jalankan()

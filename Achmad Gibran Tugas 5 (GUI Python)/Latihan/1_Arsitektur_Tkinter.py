import tkinter as tk
from tkinter import ttk

class AplikasiDasar:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Aplikasi Saya")
        self.root.geometry("400x300")
    
    def jalankan(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = AplikasiDasar()
    app.jalankan()

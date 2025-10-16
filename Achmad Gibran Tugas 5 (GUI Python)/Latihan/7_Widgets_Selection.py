import tkinter as tk
from tkinter import messagebox

class WidgetSeleksi:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Widget Seleksi")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.setup_widgets()

    def setup_widgets(self):
        self.var_check = tk.BooleanVar()
        self.check = tk.Checkbutton(self.root, text="Setuju dengan syarat", variable=self.var_check,
                                    command=self.check_changed, font=("Arial", 10))
        self.check.pack(pady=5, anchor=tk.W, padx=10)

        frame_radio = tk.LabelFrame(self.root, text="Pilih bahasa", padx=10, pady=5)
        frame_radio.pack(pady=10, fill=tk.X, padx=10)

        self.var_radio = tk.StringVar(value="python")
        for bahasa in ["Python", "Java", "JavaScript"]:
            rb = tk.Radiobutton(frame_radio, text=bahasa, variable=self.var_radio,
                                value=bahasa.lower(), font=("Arial", 10))
            rb.pack(anchor=tk.W)

        self.var_scale = tk.DoubleVar()
        self.scale = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL,
                              variable=self.var_scale, label="Volume", font=("Arial", 10))
        self.scale.pack(pady=10, fill=tk.X, padx=10)

        btn_submit = tk.Button(self.root, text="Tampilkan Pilihan", command=self.tampilkan_hasil,
                               font=("Arial", 10), bg="#d0e1f9")
        btn_submit.pack(pady=10)

    def check_changed(self):
        status = "Setuju" if self.var_check.get() else "Belum setuju"
        print(f"Checkbox: {status}")

    def tampilkan_hasil(self):
        if not self.var_check.get():
            messagebox.showwarning("Peringatan", "Anda harus menyetujui syarat terlebih dahulu.")
            return

        bahasa = self.var_radio.get().capitalize()
        volume = int(self.var_scale.get())
        messagebox.showinfo("Hasil Seleksi", f"Bahasa: {bahasa}\nVolume: {volume}")

    def jalankan(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = WidgetSeleksi()
    app.jalankan()

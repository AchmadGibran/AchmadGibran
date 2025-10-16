import tkinter as tk
from tkinter import messagebox

class WidgetDasar:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Widget Dasar")
        self.root.geometry("400x200")
        self.root.resizable(False, False)
        self.setup_widgets()

    def setup_widgets(self):
        self.label = tk.Label(self.root, text="Contoh Label", font=("Arial", 12, "bold"),
                              fg="blue", bg="lightyellow", relief=tk.RAISED, bd=2, padx=10, pady=5)
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root, width=30, font=("Arial", 10))
        self.entry.pack(pady=5)
        self.entry.insert(0, "Teks default")

        self.button = tk.Button(self.root, text="Update Label", font=("Arial", 10), bg="#d0e1f9", command=self.update_label)
        self.button.pack(pady=5)

    def update_label(self):
        teks_baru = self.entry.get().strip()
        if teks_baru:
            self.label.config(text=teks_baru)
        else:
            messagebox.showwarning("Peringatan", "Input tidak boleh kosong!")

    def jalankan(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = WidgetDasar()
    app.jalankan()

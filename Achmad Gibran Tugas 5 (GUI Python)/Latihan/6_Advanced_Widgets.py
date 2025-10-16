import tkinter as tk
from tkinter import ttk, messagebox

class WidgetLanjutan:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Widget Lanjutan")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.setup_widgets()

    def setup_widgets(self):
        frame_main = tk.Frame(self.root)
        frame_main.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        frame_text = tk.Frame(frame_main)
        frame_text.pack(fill=tk.BOTH, expand=True)

        self.text_area = tk.Text(frame_text, width=40, height=10, wrap=tk.WORD)
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame_text, command=self.text_area.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.config(yscrollcommand=scrollbar.set)

        self.listbox = tk.Listbox(frame_main, height=4)
        for item in ["Item 1", "Item 2", "Item 3", "Item 4"]:
            self.listbox.insert(tk.END, item)
        self.listbox.pack(pady=5, fill=tk.X)

        self.combo = ttk.Combobox(frame_main, values=["Pilihan 1", "Pilihan 2", "Pilihan 3"], state="readonly")
        self.combo.set("Pilih salah satu")
        self.combo.pack(pady=5, fill=tk.X)

        btn_show = tk.Button(frame_main, text="Tampilkan Pilihan", command=self.tampilkan_pilihan)
        btn_show.pack(pady=10)

    def tampilkan_pilihan(self):
        pilihan = self.combo.get()
        if pilihan == "Pilih salah satu":
            messagebox.showwarning("Peringatan", "Silakan pilih salah satu opsi!")
        else:
            messagebox.showinfo("Pilihan Anda", f"Anda memilih: {pilihan}")

    def jalankan(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = WidgetLanjutan()
    app.jalankan()

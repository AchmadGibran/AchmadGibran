import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog, colorchooser

class DialogContoh:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Contoh Dialog")
        self.root.geometry("300x350")
        self.root.resizable(False, False)
        self.setup_buttons()

    def setup_buttons(self):
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack(fill=tk.BOTH, expand=True)

        # Message boxes
        tk.Button(frame, text="Info", width=25, command=self.show_info).pack(pady=3)
        tk.Button(frame, text="Warning", width=25, command=self.show_warning).pack(pady=3)
        tk.Button(frame, text="Error", width=25, command=self.show_error).pack(pady=3)
        tk.Button(frame, text="Question", width=25, command=self.show_question).pack(pady=3)

        # File dialogs
        tk.Button(frame, text="Open File", width=25, command=self.open_file).pack(pady=3)
        tk.Button(frame, text="Save File", width=25, command=self.save_file).pack(pady=3)

        # Other dialogs
        tk.Button(frame, text="Input Dialog", width=25, command=self.input_dialog).pack(pady=3)
        tk.Button(frame, text="Color Chooser", width=25, command=self.choose_color).pack(pady=3)

    def show_info(self):
        messagebox.showinfo("Informasi", "Ini adalah pesan informasi.")

    def show_warning(self):
        messagebox.showwarning("Peringatan", "Ini adalah pesan peringatan.")

    def show_error(self):
        messagebox.showerror("Kesalahan", "Ini adalah pesan kesalahan.")

    def show_question(self):
        result = messagebox.askquestion("Pertanyaan", "Apakah Anda yakin?")
        if result == "yes":
            messagebox.showinfo("Jawaban", "Anda memilih: Ya")
        else:
            messagebox.showinfo("Jawaban", "Anda memilih: Tidak")

    def open_file(self):
        file_path = filedialog.askopenfilename(
            title="Pilih file",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            messagebox.showinfo("File Dipilih", f"Path: {file_path}")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            title="Simpan file",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            messagebox.showinfo("File Disimpan", f"Path: {file_path}")

    def input_dialog(self):
        result = simpledialog.askstring("Input", "Masukkan nama Anda:")
        if result:
            messagebox.showinfo("Nama Anda", f"Halo, {result}!")

    def choose_color(self):
        color = colorchooser.askcolor(title="Pilih warna")
        if color[1]:
            messagebox.showinfo("Warna Dipilih", f"Kode warna: {color[1]}")

    def jalankan(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = DialogContoh()
    app.jalankan()

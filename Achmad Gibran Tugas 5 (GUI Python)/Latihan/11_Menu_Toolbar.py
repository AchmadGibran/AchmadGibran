import tkinter as tk
from tkinter import messagebox

class MenuSistem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menu System")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.buat_menu()
        self.buat_toolbar()
        self.buat_area_kerja()

    def buat_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.file_new)
        file_menu.add_command(label="Open", command=self.file_open)
        file_menu.add_command(label="Save", command=self.file_save)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Copy", command=self.edit_copy)
        edit_menu.add_command(label="Paste", command=self.edit_paste)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.help_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

    def buat_toolbar(self):
        toolbar = tk.Frame(self.root, bg="lightgray", bd=1, relief=tk.RAISED)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        tk.Button(toolbar, text="New", command=self.file_new).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(toolbar, text="Open", command=self.file_open).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(toolbar, text="Save", command=self.file_save).pack(side=tk.LEFT, padx=2, pady=2)

    def buat_area_kerja(self):
        self.text_area = tk.Text(self.root, wrap=tk.WORD)
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def file_new(self):
        self.text_area.delete("1.0", tk.END)
        print("File -> New")

    def file_open(self):
        print("File -> Open")

    def file_save(self):
        print("File -> Save")

    def edit_copy(self):
        try:
            selected = self.text_area.selection_get()
            self.root.clipboard_clear()
            self.root.clipboard_append(selected)
        except tk.TclError:
            print("Tidak ada teks yang dipilih.")

    def edit_paste(self):
        try:
            pasted = self.root.clipboard_get()
            self.text_area.insert(tk.INSERT, pasted)
        except tk.TclError:
            print("Clipboard kosong.")

    def help_about(self):
        messagebox.showinfo("About", "Aplikasi Contoh Menu System")

    def jalankan(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = MenuSistem()
    app.jalankan()

import tkinter as tk

class LayoutPack:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pack Layout")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.buat_widget()

    def buat_widget(self):
        frame_utama = tk.Frame(self.root, bg="lightgray", bd=2, relief=tk.SUNKEN)
        frame_utama.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        btn1 = tk.Button(frame_utama, text="Button 1", font=("Arial", 12), bg="#d0e1f9")
        btn1.pack(side=tk.TOP, fill=tk.X, pady=5)

        btn2 = tk.Button(frame_utama, text="Button 2", font=("Arial", 12), bg="#f9d0d0")
        btn2.pack(side=tk.TOP, fill=tk.X, pady=5)

        btn3 = tk.Button(frame_utama, text="Button 3", font=("Arial", 12), bg="#d0f9d6")
        btn3.pack(side=tk.BOTTOM, fill=tk.X, pady=5)

    def jalankan(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = LayoutPack()
    app.jalankan()

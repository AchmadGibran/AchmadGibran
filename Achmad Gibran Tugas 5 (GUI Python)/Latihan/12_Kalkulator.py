import tkinter as tk

class AplikasiKalkulator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Kalkulator GUI")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        self.expression = ""
        self.buat_display_frame()
        self.buat_button_frame()

    def buat_display_frame(self):
        self.display_var = tk.StringVar()
        entry = tk.Entry(
            self.root,
            textvariable=self.display_var,
            font=("Arial", 18),
            bg="lightgray",
            bd=5,
            relief=tk.RIDGE,
            justify="right"
        )
        entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

    def buat_button_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")

        tombol = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C", "CE"]
        ]

        for baris in tombol:
            baris_frame = tk.Frame(frame)
            baris_frame.pack(expand=True, fill="both")
            for teks in baris:
                tk.Button(
                    baris_frame,
                    text=teks,
                    font=("Arial", 14),
                    command=lambda x=teks: self.tekan_tombol(x),
                    height=2,
                    width=6
                ).pack(side="left", expand=True, fill="both")

    def tekan_tombol(self, nilai):
        if nilai == "=":
            try:
                hasil = str(eval(self.expression))
                self.display_var.set(hasil)
                self.expression = hasil
            except Exception:
                self.display_var.set("Error")
                self.expression = ""
        elif nilai == "C":
            self.expression = ""
            self.display_var.set("")
        elif nilai == "CE":
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression)
        else:
            self.expression += nilai
            self.display_var.set(self.expression)

    def jalankan(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = AplikasiKalkulator()
    app.jalankan()

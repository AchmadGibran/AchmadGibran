import tkinter as tk

class EventLambda:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Event dengan Lambda")
        self.root.geometry("300x250")
        self.root.resizable(False, False)
        self.counter = 0
        self.setup_buttons()

    def setup_buttons(self):
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(pady=20)

        for i in range(5):
            btn = tk.Button(
                frame_buttons,
                text=f"Button {i+1}",
                width=20,
                command=lambda x=i: self.button_clicked(x)
            )
            btn.pack(pady=3)

        self.lbl_status = tk.Label(
            self.root,
            text="Belum ada button diklik",
            font=("Arial", 10),
            bg="white",
            relief=tk.SUNKEN,
            anchor="w"
        )
        self.lbl_status.pack(fill=tk.X, padx=20, pady=10)

    def button_clicked(self, button_num):
        self.counter += 1
        self.lbl_status.config(text=f"Button {button_num+1} diklik! Total klik: {self.counter}")

    def jalankan(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = EventLambda()
    app.jalankan()

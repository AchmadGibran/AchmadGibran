import tkinter as tk

class EventHandling:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Event Handling")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.setup_events()

    def setup_events(self):
        frame = tk.Frame(self.root, width=300, height=200, bg="lightblue", relief=tk.RIDGE, bd=2)
        frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        frame.pack_propagate(False)

        # Binding event mouse ke frame
        frame.bind("<Button-1>", self.mouse_click)
        frame.bind("<Double-Button-1>", self.mouse_double_click)
        frame.bind("<B1-Motion>", self.mouse_drag)
        frame.bind("<Enter>", self.mouse_enter)
        frame.bind("<Leave>", self.mouse_leave)

        # Binding event keyboard ke root
        self.root.bind("<KeyPress>", self.key_pressed)

        self.lbl_info = tk.Label(
            self.root,
            text="Event akan ditampilkan di sini",
            font=("Arial", 10),
            bg="white",
            relief=tk.SUNKEN,
            anchor="w"
        )
        self.lbl_info.pack(fill=tk.X, padx=20, pady=5)

    def mouse_click(self, event):
        self.lbl_info.config(text=f"Klik di koordinat: ({event.x}, {event.y})")

    def mouse_double_click(self, event):
        self.lbl_info.config(text=f"Double click di: ({event.x}, {event.y})")

    def mouse_drag(self, event):
        self.lbl_info.config(text=f"Drag ke: ({event.x}, {event.y})")

    def mouse_enter(self, event):
        self.lbl_info.config(text="Mouse masuk area biru")

    def mouse_leave(self, event):
        self.lbl_info.config(text="Mouse keluar dari area biru")

    def key_pressed(self, event):
        self.lbl_info.config(text=f"Tombol ditekan: {event.keysym}")

    def jalankan(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = EventHandling()
    app.jalankan()

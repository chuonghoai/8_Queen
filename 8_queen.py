import tkinter as tk

class eight_queen:
    def __init__(self, root):
        self.root = root
        self.root.title("8 queen")
        self.root.config(bg="lightgray")
        self.pos_queen = []

        frame_left = tk.Frame(self.root, bg="lightgray", relief="solid", borderwidth=1)
        frame_left.grid(row=0, column=0, padx=10, pady=10)

        frame_right = tk.Frame(self.root, bg="lightgray", relief="solid", borderwidth=1)
        frame_right.grid(row=0, column=1, padx=10, pady=10)

        self.buttons_left = self.create_widget(frame_left)
        self.buttons_right = self.create_widget(frame_right)
        
    def create_widget(self, frame):
        buttons = []
        for i in range(8):
            row = []
            for j in range(8):
                color = "white" if (i + j) % 2 == 0 else "black"
                btn = tk.Button(frame, width=4, height=2, bg=color,
                                relief="flat", borderwidth=0, highlightthickness=0,
                                text="👑")
                btn.grid(row = i, column = j, padx=1, pady=1)
                row.append(btn)
            buttons.append(row)
        return buttons

if __name__ == "__main__":
    root = tk.Tk()
    game = eight_queen(root)
    root.mainloop()
    
import tkinter as tk
from PIL import Image, ImageTk

class eight_queen:
    def __init__(self, root):
        self.root = root
        self.root.title("8 queen")
        self.root.config(bg="lightgray")
        self.pos_queen =   [[1, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 1, 0],
                            [0, 1, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1]]

        frame_left = tk.Frame(self.root, bg="lightgray", relief="solid", borderwidth=1)
        frame_left.grid(row=0, column=0, padx=10, pady=10)

        frame_right = tk.Frame(self.root, bg="lightgray", relief="solid", borderwidth=1)
        frame_right.grid(row=0, column=1, padx=10, pady=10)

        white_queen = Image.open("whiteQ.png").resize((60, 60))
        black_queen = Image.open("blackQ.png").resize((60, 60))
        self.whiteQ = ImageTk.PhotoImage(white_queen)   #phải có self mới load đc?? đặt ở __init__ thì vẽ đc 2 bàn, để ở create_widget() thì vẽ đc 1 bản bên phải
        self.blackQ = ImageTk.PhotoImage(black_queen)

        self.buttons_left = self.create_widget(frame_left, False)
        self.buttons_right = self.create_widget(frame_right, True)
        
        self.queen_pos = []
        
    def create_widget(self, frame, draw_queen):
        buttons = []
        img_null = tk.PhotoImage(width=1, height=1)
        for i in range(8):
            row = []
            for j in range(8):
                color = "white" if (i + j) % 2 == 0 else "black"
                queen = self.whiteQ if color == "black" else self.blackQ
                if draw_queen and self.pos_queen[i][j] == 1:
                    btn = tk.Button(frame, image=queen, width=60, height=60, bg=color,
                                relief="flat", borderwidth=0, highlightthickness=0)
                else:
                    btn = tk.Button(frame, image=img_null, width=60, height=60, bg = color,
                                    relief="flat", borderwidth=0, highlightthickness=0)
                btn.grid(row = i, column = j, padx=1, pady=1)
                row.append(btn)
            buttons.append(row)
        return buttons

if __name__ == "__main__":
    root = tk.Tk()
    game = eight_queen(root)
    root.mainloop()
    
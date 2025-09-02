import tkinter as tk
import random
from PIL import Image, ImageTk

class eight_queen:
    def __init__(self, root):
        self.root = root
        self.root.title("8 queen")
        self.root.config(bg="lightgray")
        self.n = 8

        frame_left = tk.Frame(self.root, bg="lightgray", relief="solid", borderwidth=1)
        frame_left.grid(row=0, column=0, padx=10, pady=10)

        frame_right = tk.Frame(self.root, bg="lightgray", relief="solid", borderwidth=1)
        frame_right.grid(row=0, column=1, padx=10, pady=10)

        white_queen = Image.open("whiteQ.png").resize((60, 60))
        black_queen = Image.open("blackQ.png").resize((60, 60))
        self.whiteQ = ImageTk.PhotoImage(white_queen)   #phải có self mới load đc?? đặt ở __init__ thì vẽ đc 2 bàn, để ở create_widget() thì vẽ đc 1 bản bên phải
        self.blackQ = ImageTk.PhotoImage(black_queen)

        while True:
            self.queen_pos = [[0] * self.n for _ in range(self.n)]
            if self.set_queen(self.queen_pos, 0):
                break

        self.buttons_left = self.create_widget(frame_left, False)
        self.buttons_right = self.create_widget(frame_right, True)
        
        self.queen_pos = []
        
    def create_widget(self, frame, draw_queen):
        buttons = []
        img_null = tk.PhotoImage(width=1, height=1)
        for i in range(self.n):
            row = []
            for j in range(self.n):
                color = "white" if (i + j) % 2 == 0 else "black"
                queen = self.whiteQ if color == "black" else self.blackQ
                if draw_queen and self.queen_pos[i][j] == 1:
                    btn = tk.Button(frame, image=queen, width=60, height=60, bg=color,
                                relief="flat", borderwidth=0, highlightthickness=0)
                else:
                    btn = tk.Button(frame, image=img_null, width=60, height=60, bg = color,
                                    relief="flat", borderwidth=0, highlightthickness=0)
                btn.grid(row = i, column = j, padx=1, pady=1)
                row.append(btn)
            buttons.append(row)
        return buttons

    def is_safe(self, queen_pos, row, col):
        #cột
        for i in range(row):
            if queen_pos[i][col] == 1:
                return False

        #hàng chéo lên bên trái
        i, j = row, col
        while i >= 0 and j >= 0:
            if queen_pos[i][j] == 1:
                return False
            i -= 1
            j -= 1
        
        #hàng chéo lên bên phải
        i, j = row, col
        while i >= 0 and j < self.n:
            if queen_pos[i][j] == 1:
                return False
            i -= 1
            j += 1
        return True

    def set_queen(self, queen_pos, row):
        if row == self.n:
            return True
        
        for col in random.sample(range(self.n), self.n):
            if self.is_safe(queen_pos, row, col):
                queen_pos[row][col] = 1
                if self.set_queen(queen_pos, row + 1):
                    return True
                queen_pos[row][col] = 0
        return False
    
if __name__ == "__main__":
    root = tk.Tk()
    game = eight_queen(root)
    root.mainloop()
    
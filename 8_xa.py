import tkinter as tk
import random
from PIL import Image, ImageTk
from collections import deque

class eight_queen:
    def __init__(self, root):
        self.root = root
        self.root.title("8 queen")
        self.root.config(bg="lightgray")
        self.n = 8

        self.frame_left = tk.Frame(self.root, bg="lightgray", relief="solid", borderwidth=1)
        self.frame_left.grid(row=0, column=0, padx=10, pady=10)

        self.frame_right = tk.Frame(self.root, bg="lightgray", relief="solid", borderwidth=1)
        self.frame_right.grid(row=0, column=1, padx=10, pady=10)

        white_xa = Image.open("./whiteX.png").resize((60, 60))
        black_xa = Image.open("./blackX.png").resize((60, 60))
        self.whiteX = ImageTk.PhotoImage(white_xa)
        self.blackX = ImageTk.PhotoImage(black_xa)
        
        self.img_null = tk.PhotoImage(width=1, height=1)

        self.xa_pos = [[0] * self.n for _ in range(self.n)]
        self.set_xa(self.xa_pos)
        
        self.buttons_left = self.create_widget(self.frame_left, False)
        self.buttons_right = self.create_widget(self.frame_right, True)

    def create_widget(self, frame, draw_xa):
        buttons = []
        for i in range(self.n):
            row = []
            for j in range(self.n):
                color = "white" if (i + j) % 2 == 0 else "black"
                
                if draw_xa and self.xa_pos[i][j] == 1:
                    img = self.whiteX if color == "black" else self.blackX
                else:
                    img = self.img_null
                
                btn = tk.Button(frame, image=img, width=60, height=60, bg=color,
                                relief="flat", borderwidth=0, highlightthickness=0)
                    
                btn.grid(row = i, column = j, padx=1, pady=1)
                row.append(btn)
            buttons.append(row)
        
        return buttons

    #Kiểm tra vị trí row, col có an toàn để đặt xe ko
    def x_is_safe(self, row, col):
        #Kiểm tra vị trí có ở trong ma trận bàn cờ ko
        if row < 0 or row >= self.n or col < 0 or col >= self.n:
            return False
        
        #Kiểm tra theo hàng ngang và dọc
        for i in range(self.n):
            if self.xa_pos[row][i] == 1:
                return False
            if self.xa_pos[i][col] == 1:
                return False
        return True
    
    #Hàm đặt xe lên bàn cờ
    def set_xa(self, xa_pos):
        #Sinh ra vị trí đầu tiên để đặt xe
        x_start = random.randint(0, self.n - 1)
        y_start = random.randint(0, self.n - 1)
        #Đánh dấu vị trí đã đặt xe
        xa_pos[x_start][y_start] = 1
        
        #Tạo queue để chạy bfs
        q = deque([(x_start, y_start)])
        #Các hướng có thể di chuyển để đặt xe
        near = [[-1, -1], [-1, 1], [1, -1], [1, 1]]     #[trên trái, trên phải, dưới trái, dưới phải]
        #Hàm đếm số xe dã đặt, ở đây là đã đặt 1 quân xe
        setted = 1
        
        #Bắt đầu bfs
        while q and setted < 8:
            #Lấy tọa độ của quân xe đầu tiên trong queue
            x, y = q.popleft()
            #Từ tọa độ đã lấy di chuyển xung quanh ra 4 phía 
            for move in near:
                #Tọa độ tiếp theo bằng cách lấy tọa độ hiện tại + hướng di chuyển
                x_next, y_next = x + move[0], y + move[1]
                #Mỗi lần sinh ra 1 tọa độ tiếp theo thì thêm vào queue để dự phòng cho các nước đi tiếp theo đặt xe
                q.append((x_next, y_next))
                #kiểm tra vị trí tiếp theo có an toàn ko
                if self.x_is_safe(x_next, y_next):
                    #nếu an toàn thì đánh dấu đặt xe và đánh dấu số quân xe đã đặt tăng lên 1
                    xa_pos[x_next][y_next] = 1
                    setted += 1
                    if setted == 8:
                        break
    
if __name__ == "__main__":
    root = tk.Tk()
    game = eight_queen(root)
    root.mainloop()
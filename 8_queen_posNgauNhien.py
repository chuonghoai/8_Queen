import tkinter as tk
import random
#thư viện này đc khai báo để chuyển đổi định dạng kích cỡ của tk.button từ mặc định ký tự sang pixel
from PIL import Image, ImageTk

class eight_queen:
    #hàm contructor khai báo root
    def __init__(self, root):
        self.root = root
        self.root.title("8 queen")
        self.root.config(bg="lightgray")
        #Kích thước của bàn cờ nxn
        self.n = 8

        frame_left = tk.Frame(self.root, bg="lightgray", relief="solid", borderwidth=1)
        frame_left.grid(row=0, column=0, padx=10, pady=10)

        frame_right = tk.Frame(self.root, bg="lightgray", relief="solid", borderwidth=1)
        frame_right.grid(row=0, column=1, padx=10, pady=10)

        white_queen = Image.open("whiteQ.png").resize((60, 60))
        black_queen = Image.open("blackQ.png").resize((60, 60))
        self.whiteQ = ImageTk.PhotoImage(white_queen)
        self.blackQ = ImageTk.PhotoImage(black_queen)

        #- Vòng lặp while này để đảm bảo rằng mỗi lần đặt hậu vào bàn cờ thì phải có nghiệm
        #   nếu ko có thì làm lại
        while True:
            self.queen_pos = [[0] * self.n for _ in range(self.n)]
            if self.set_queen(self.queen_pos, 0):
                break

        self.buttons_left = self.create_widget(frame_left, False)
        self.buttons_right = self.create_widget(frame_right, True)
        
        #Đây là ma trận lưu trữ các vị trí đặt hậu: 1 là hậu, 0 là trống, sẽ được đặt bằng hàm set_queen
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
        #kiểm tra trên cột đó có hậu ko
        for i in range(row):
            if queen_pos[i][col] == 1:
                return False

        #kiểm tra hàng chéo lên bên trái có hậu ko
        i, j = row, col
        while i >= 0 and j >= 0:
            if queen_pos[i][j] == 1:
                return False
            i -= 1
            j -= 1
        
        #kiểm tra hàng chéo lên bên phải có hậu ko
        i, j = row, col
        while i >= 0 and j < self.n:
            if queen_pos[i][j] == 1:
                return False
            i -= 1
            j += 1
        #nếu thỏa mã 3 điều kiện trên thì trả về true (vị trí này an toàn)
        return True

    def set_queen(self, queen_pos, row):
        #- điều kiện dừng: khi số hàng tăng lên bằng n,
        #   vì chỉ số tối đa trong mảng là n - 1, nếu row tăng lên bằng n tức là đã đặt xong hết hậu,
        #   return True để dừng đặt hậu
        if row == self.n:
            return True
        
        #- Bắt đầu vòng lặp đặt hậu:
        #   random.sample(range(self.n), self.n): ngẫu nhiên xáo trộn vị trí các con số từ 0 đến n - 1,
        #   mục đích để mỗi lần khởi chạy thì vị trí hậu là ngẫu nhiên

        #- Cơ chế đặt hậu: Với hàng row cho trước ở hàm __init__ (thường là số 0), vòng lặp sẽ đi qua ngẫu nhiên các vị trí của row 0,
        #   từ vị trí được chọn sẽ tăng row lên 1 để thử đặt ở các vị trí khác nhau trên row 1,
        #   nếu đặt được thì tiếp tục lên row 2...
        #   Giả sử đã đến được row 6, nếu gặp trường hợp mà cả 8 vị trí của row 6 đều ko đặt được thì sẽ chạy sang bước tiếp theo:
        #       bài toán này là đệ quy, khi cả 8 vị trí của row 6 ko đặt được (tức là return False), thì vòng for ở row 6 kết thúc,
        #       hàm quay về row 5, đặt lại queen_pos[row][col] = 0 vì từ vị trí này ko thể đặt tiếp cho row 6, đổi sang cột khác ở 
        #       row 5 rồi tiếp tục thử đặt lên row 6
        
        for col in random.sample(range(self.n), self.n):
            #trước khi đặt hậu, kiểm tra vị trí này có an toàn ko
            if self.is_safe(queen_pos, row, col):
                #đặt queen ở vị trí này
                queen_pos[row][col] = 1
                #thử đi lên row cao hơn
                if self.set_queen(queen_pos, row + 1):
                    #nếu trả về True thì vị trí này đã tạo ra 1 bàn cờ hoàn chỉnh
                    return True
                #nếu ko trả về True thì từ vị trí này ko thể tạo ra bàn cờ hoàn chỉnh, lấy quân hậu ra và đi sang cột khác để thử
                queen_pos[row][col] = 0

        #Nếu vòng for đi đến cuối cùng mà vẫn chưa trả về True chứng tỏ chương trình ko tìm thấy nghiệm 
        return False
    
#Phần main như bài trước
if __name__ == "__main__":
    root = tk.Tk()
    game = eight_queen(root)
    root.mainloop()
    
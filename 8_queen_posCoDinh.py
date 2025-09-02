import tkinter as tk
#thư viện này đc khai báo để chuyển đổi định dạng kích cỡ của tk.button từ mặc định ký tự sang pixel
from PIL import Image, ImageTk

class eight_queen:
    #hàm contructor khai báo root
    def __init__(self, root):
        self.root = root
        self.root.title("8 queen")
        self.root.config(bg="lightgray")
        #vị trí cố định xuất hiện các quân hậu, số 1 là vị trí hậu, số 0 là trống
        self.pos_queen =   [[1, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 1, 0],
                            [0, 1, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1]]

        #- iao diện có 2 bàn cờ nên sử dụng 2 khung frame
        #- khung frame này có công năng gần tương tự như root, để vẽ các đối tượng lên nó
        #   + self.root: frame này nằm trên root, 
        #   + relief="solid": đường viền bao bọc bên ngoài thuộc kiểu solid (solid giống kiểu 1 nét đen đơn giản bên ngoài)
        #   + borderwidth=1: độ dày của viền ngoài 
        frame_left = tk.Frame(self.root, bg="lightgray", relief="solid", borderwidth=1)
        #đặt frame ở vị trí row = 0, column = 0, giãn cách với frame khác là padx=10, pady=10
        frame_left.grid(row=0, column=0, padx=10, pady=10)

        frame_right = tk.Frame(self.root, bg="lightgray", relief="solid", borderwidth=1)
        #tương tự như trên, nhưng vị trí column = 1 để frame này nằm bên phải cái trên
        frame_right.grid(row=0, column=1, padx=10, pady=10)

        #- 4 biến này để gọi ra 2 hình ảnh quân hậu trắng và đen
        #- resize: định dạng lại kích cỡ 60x60 pixel
        #- LƯU Ý: khi có image thì đơn vị mặc định là pixel, ko có thì là kích cỡ ký tự như bài trước,
        #   ở đây có 2 hình ảnh quân hậu trắng đen nên mọi thứ trong button sắp tới sẽ có đơn vị là pixel
        #- white_queen và black_queen là biến tạm lưu ảnh gốc khi mở whiteQ.png  và blackQ.png bằng thư viện PIL,
        #   2 biến này có kiểu PIL.Image.Image, Tkinter ko thể hiểu được nên phải dùng ImageTk.PhotoImage để chuyển
        #   thành đối tượng của tkinter. việc gán vào self.whiteQ giúp giữ hình ảnh được tham chiếu lâu dài, giúp
        #   hiển thị hình ảnh xuyên suốt chương trình mà ko bị mất
        white_queen = Image.open("whiteQ.png").resize((60, 60)) 
        black_queen = Image.open("blackQ.png").resize((60, 60))
        self.whiteQ = ImageTk.PhotoImage(white_queen)
        self.blackQ = ImageTk.PhotoImage(black_queen)

        #- Bắt đầu tạo 2 bàn cờ bằng 2 frame. Vị trí đã được khai báo ở trên, 1 cái ở column = 0, cái kia ở column = 1
        #- vì yêu cầu bàn cờ bên trái trống, bên phải có quân hậu, nên đặt 2 biến bool vào để phân biệt cái nào chứa hậu
        #- 2 biến buttons_left và buttons_right để chứa các ô của 2 bàn cờ
        self.buttons_left = self.create_widget(frame_left, False)
        self.buttons_right = self.create_widget(frame_right, True)
        
    #Hàm tạo giao diện bàn cờ trên frame, với biến bool draw_queen để quyết định bàn cờ rộng hay có hậu 
    def create_widget(self, frame, draw_queen):
        #lưu giữ các ô đã được vẽ trên bàn cờ
        buttons = []
        #Tạo một hình ảnh trong suốt (null) với pixel là 1x1 để bỏ vào ô ko có quân hậu
        img_null = tk.PhotoImage(width=1, height=1)
        for i in range(8):
            #Tạo hàng chứa 8 ô chuẩn bị tạo
            row = []
            for j in range(8):
                #Lệnh điều kiện: nếu i + j chẵn thì ô màu trắng, ngược lại màu đen -> mục đích tạo màu sắc xen kẽ
                color = "white" if (i + j) % 2 == 0 else "black"
                #Lệnh điều kiện: Nếu nền ô màu đen thì hậu màu trắng, ngược lại màu đen -> tạo sự tương phản dễ nhìn
                queen = self.whiteQ if color == "black" else self.blackQ
                
                #Lệnh điều kiện: nếu bàn cờ được chỉ định là có vẽ hậu (draw_queen=True) và vị trí hiện tại đúng là quân hậu self.pos_queen[i][j] == 1
                if draw_queen and self.pos_queen[i][j] == 1:
                    #Tạo tk.button:
                    #+ frame: button sẽ nằm trên frame
                    #+ image=queen: hình ảnh đã được gọi ở dòng 66, chứa quân hậu
                    #+ width=60, height=60: vì có chứa hình ảnh nên 2 đơn vị này là pixel
                    #+ bg=color: màu nền của ô
                    #+ relief="flat": kiểu của đường viền bên ngoài, "flat" giống kiểu phẳng, nền trơn
                    #+ borderwidth=0: độ dày của viền = 0 --> tức là ko có viền
                    #+ highlightthickness=0:
                    btn = tk.Button(frame, image=queen, width=60, height=60, bg=color,
                                relief="flat", borderwidth=0)
                else:
                    #- Đây là trường hợp bàn cờ hiện ko được có hậu hoặc ko phải ô có hậu,
                    #   lúc này để đảm bảo kích cỡ các ô đều như nhau (60x60 pixel) thì cho hình ảnh là img_null 
                    #   (tức là vẫn có hình ảnh nhưng nó trong suốt)
                    btn = tk.Button(frame, image=img_null, width=60, height=60, bg=color,
                                    relief="flat", borderwidth=0)

                #Đã xong phần khởi tạo, giờ vẽ nó lên hàng i, cột j, giãn cách giữa các ô là 1
                btn.grid(row = i, column = j, padx=1, pady=1)
                
                #thêm từng ô được tạo vào row    
                row.append(btn)
            #thêm từng row (mỗi row chứa 8 ô) được tạo vào buttons
            buttons.append(row)
        #Trả về buttons để trả dữ liệu các ô cho 2 biến lưu trữ buttons_right và buttons_left
        return buttons

#Phần main như bài trước
if __name__ == "__main__":
    root = tk.Tk()
    game = eight_queen(root)
    root.mainloop()
    

#
# sử dụng thư viện tkinter



import random
import tkinter
import tkinter.messagebox
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

# Ghi dữ liệu vào bàn cờ
sign = 0

# Tạo bàn cờ trống
global board
board = [[" " for x in range(5)] for y in range(5)]

# Kiểm tra l(O/X) đã thắng trận đấu hay chưa
# theo quy tắc của trò chơi

def winner(b, l):
    d = 0
    for i in range(5):
        for j in range(5):
            if b[i][j] == l:
                d += 1
                if d == 3:
                    return True
            else:
                d = 0

    for j in range(5):
        for i in range(5):
            if b[i][j] == l:
                d += 1
                if d == 3:
                    return True
            else:
                d = 0
    for i in range(5):

        if b[i][i] == l:
            d += 1
            if d == 3:
                return True
        else:
            d = 0
    for i in range(5):
        if b[i][4 - i] == l:
            d += 1
            if d == 3:
                return True
        else:
            d = 0
    for i in range(4):
        if b[i][i + 1] == l:
            d += 1
            if d == 3:
                return True
        else:
            d = 0
    for i in range(3):
        if b[i][i + 2] == l:
            d += 1
            if d == 3:
                return True
        else:
            d = 0
    for i in range(2):
        if b[i][i + 3] == l:
            d += 1
            if d == 3:
                return True
        else:
            d = 0
    for i in range(4):
        if b[i + 1][i] == l:
            d += 1
            if d == 3:
                return True
        else:
            d = 0
    for i in range(3):
        if b[i + 2][i] == l:
            d += 1
            if d == 3:
                return True
        else:
            d = 0
    for i in range(2):
        if b[i + 3][i] == l:
            d += 1
            if d == 3:
                return True
        else:
            d = 0
    for i in range(4):
        if b[i][4 - i - 1] == l:
            d += 1
            if d == 3:
                return True
        else:
            d = 0
    for i in range(3):
        if b[i][4 - i - 2] == l:
            d += 1
            if d == 3:
                return True
        else:
            d = 0
    for i in range(2):
        if b[i][4 - i - 3] == l:
            d += 1
            if d == 3:
                return True
        else:
            d = 0

    for i in range(4):
        if b[i + 1][4 - i] == l:
            d += 1
            if d == 3:
                return True
        else:
            d = 0
    for i in range(3):
        if b[i + 2][4 - i] == l:
            d += 1
            if d == 3:
                return True
        else:
            d = 0
    for i in range(2):
        if b[i+3][4-i]==l:
            d+=1
            if d==3:
                return True
    return False
#Ghi dữ liệu vào bàn cờ
def get_text(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    if winner(board,"X"):
        box = tkinter.messagebox.askquestion("Chiến thắng", "X thắng! Đấu lại?")
        if box == "yes":
            emptyboard()
            gb.destroy()
            play()
        else:
            exit()
    elif winner(board,"O"):
        box = tkinter.messagebox.askquestion("Chiến thắng", "O thắng! Đấu lại?")
        if box == "yes":
            emptyboard()
            gb.destroy()
            play()
        else:
            exit()
    elif isfull():
        box = tkinter.messagebox.askquestion("Hòa", "Hòa! Đấu lại?")
        if box == "yes":
            emptyboard()
            gb.destroy()
            play()
        else:
            exit()
# Kiểm tra xem người chơi có thể nhấn nút hay không
def isfree(i, j):
    return board[i][j] == " "

def emptyboard():
    for i in range(5):
        for j in range(5):
            board[i][j] = " "
            button[i][j].config(text=" ")

# Kiểm tra bàn cờ đầy ha không
def isfull():
    flag = True
    for i in board:
        if i.count(' ') > 0:
            flag = False
    return flag

# Tạo giao diện bàn cờ cho chơi với người chơi khác
def gameboard_pl(game_board, l1, l2):
    global button
    button = []
    for i in range(5):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(5):
            n = j
            button[i].append(j)
            get_t = partial(get_text, i, j, game_board, l1, l2)
            button[i][j] = Button(game_board, bd=1, command=get_t, height=3, width=6)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()

def ai():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if not possiblemove:
        return
    else:
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy, let):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 4], [4, 0], [4, 4]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner) - 1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [0, 2], [2, 0], [0, 3], [3, 0], [1, 4], [4, 1], [2, 4], [4, 2], [3, 4], [4, 3]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge) - 1)
            return edge[move]
        center = []
        for i in possiblemove:
            if i in [[2, 2]]:
                center.append(i)
        if len(center) > 0:
            move = random.randint(0, len(center) - 1)
            return center[move]

# Định cấu hình văn bản trên nút khi chơi với hệ thống
def get_text_ai(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
        x=TRUE
    if winner(board, "X"):
        x= FALSE
        box = tkinter.messagebox.askquestion("Chiến thắng", "Bạn thắng! Đấu lại?")
        if box == "yes":
            emptyboard()
            gb.destroy()
            play()
        else:
            exit()
    elif winner(board, "O"):
        x = FALSE
        box = tkinter.messagebox.askquestion("Thất bại", "Máy thắng! Đấu lại?")
        if box == "yes":
            emptyboard()
            gb.destroy()
            play()
        else:
            exit()
    elif isfull():
        x = FALSE
        box = tkinter.messagebox.askquestion("Hòa", "Hòa! Đấu lại?")
        if box == "yes":
            emptyboard()
            gb.destroy()
            play()
        else:
            exit()

    if x:
        if sign % 2 != 0:
            move = ai()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_ai(move[0], move[1], gb, l1, l2)

# Tạo giao diện bàn cờ cho chơi với máy
def gameboard_ai(game_board, l1, l2):
    global button
    button = []
    for i in range(5):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(5):
            n = j
            button[i].append(j)
            get_t = partial(get_text_ai, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=1, command=get_t, height=3, width=6)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()


# Khởi tạo bảng trò chơi để chơi với máy
#
def withai(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Chơi với máy")
    game_board.geometry("480x480")
    l1 = Button(game_board, text="Lượt bạn", width=6)
    l1.grid(row=0, column=0)
    l2 = Button(game_board, text="Lượt máy",width=6, state=DISABLED)
    l2.grid(row=0, column=1)
    l3 = Button(game_board, text="Đấu lại", width=6, command=lambda: replay(game_board))
    l3.grid(row=0, column=2)
    gameboard_ai(game_board, l1, l2)

# Khởi tạo bảng trò chơi để chơi với người chơi khác
def withplayer(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.geometry("480x480")
    game_board.title("Chơi với nhau")
    l1 = Button(game_board, text="Lượt X", width=6)
    l1.grid(row=0, column=0)
    l2 = Button(game_board, text="Lượt O",width=6, state=DISABLED)
    l2.grid(row=0, column=1)
    l3 = Button(game_board, text="Đấu lại", width=6, command=lambda: replay(game_board))
    l3.grid(row=0, column=2)

    gameboard_pl(game_board, l1, l2)

def replay(gameboard):

    emptyboard()
    gameboard.destroy()
    play()

def guide():
    messagebox.showinfo("Hướng dẫn",
                        "Cách chơi: \n1. Người chơi chọn 1 ô trống để đánh dấu. \n2. Người chơi thắng khi đánh dấu 3 ô liên tiếp theo chiều ngang, dọc hoặc chéo. \n3. Nếu không có người chơi nào thắng, trò chơi kết thúc hòa.")


# Hàm main
def play():
    menu = Tk()
    menu.geometry("480x480")
    menu.title("Caro")
    wai = partial(withai, menu)
    wpl = partial(withplayer, menu)

    head = Button(menu, text="Chào mừng đến với Caro 5x5",
                  activeforeground='black',
                  activebackground="white",
                  fg="black", width=250, font='summer', bd=1)

    B1 = Button(menu, text="Chơi với máy", command=wai,
                activeforeground='red',
                activebackground="yellow", bg="white",
                fg="black", width=250, font='summer', bd=1)

    B2 = Button(menu, text="Chơi với người", command=wpl, activeforeground='red',
                activebackground="yellow", bg="white", fg="black",
                width=250, font='arial', bd=1)

    B3 = Button(menu, text="Thoát", command=menu.quit, activeforeground='red',
                activebackground="yellow", bg="white", fg="black",
                width=250, font='summer', bd=1)
    B4 = Label(menu, text="",
               activeforeground='red',
               activebackground="black", bg="white", fg="black",
               width=250, font='summer', bd=1)
    B5 = Button(menu, text="Hướng dẫn", command=guide, activeforeground='red',
                activebackground="yellow", bg="white", fg="black",
                width=250, font='summer', bd=1)
    head.pack()
    B1.pack()
    B2.pack()
    B3.pack()
    B5.pack()
    B4.pack()
    menu.mainloop()
    head.pack()
    B1.pack()
    B2.pack()
    B3.pack()
    B4.pack()
    menu.mainloop()
    head.pack(side='top')
    B1.pack(side='top')
    B2.pack(side='top')
    B3.pack(side='top')
    menu.mainloop()


# Gọi hàm main
if __name__ == '__main__':
    play()

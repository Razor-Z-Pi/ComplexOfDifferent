from tkinter import *
from tkinter import ttk, messagebox
from  random import choice
import time

frm = []; btn = []                              # Списки с фреймами и кнопками
xBtn = 16; yBtn = 16                            # Размеры поля (количество кнопок)
playTime = 0                                    # Время игры
mines = xBtn * yBtn * 10 // 64                  # Количество мин
imgMark = '\u2691'; imgMine = '\u2718'          # Символ маркера и мины
playArea = []; nMoves = 0; mrk=0                # Игровое поле, счётчик ходов и маркеров
tk = Tk()
tk.title('Сапёр!!!')
tk.geometry(str(44 * xBtn) + 'x' + str(44 * yBtn + 10))

def play(n):                                    # n - номер нажатой кнопки
    global xBtn, yBtn, mines, nMoves, mrk, playTime
    if len(playArea) < xBtn*yBtn:               # Если поле ещё не создано
        return()
    nMoves += 1
    if nMoves == 1:                             # Если это первый ход игрока,
        playTime = time.time()
        i = 0
        while i < mines:                         
            j = choice(range(0, xBtn * yBtn))
            if j != n and playArea[j] != -1:
                playArea[j] = -1
                i += 1
                
        for i in range(0, xBtn*yBtn):           # подсчитаем количесво мин вокруг каждой клетки
            if playArea[i] != -1:
                k = 0
                if i not in range(0, xBtn*yBtn, xBtn):
                    if playArea[i-1] == -1: k += 1              # слева

                    if i > xBtn-1:
                        if playArea[i-xBtn-1] == -1: k += 1     # слева сверху

                    if i < xBtn*yBtn-xBtn:
                        if playArea[i+xBtn-1] == -1: k += 1     # слева снизу

                if i not in range(-1, xBtn*yBtn, xBtn):
                    if playArea[i+1] == -1: k += 1              # справа

                    if i > xBtn-1:
                        if playArea[i-xBtn+1] == -1: k += 1     # справа сверху

                    if i < xBtn*yBtn-xBtn:
                        if playArea[i+xBtn+1] == -1: k += 1     # справа снизу

                if i > xBtn-1:
                    if playArea[i-xBtn] == -1: k += 1           # сверху
                    
                if i < xBtn * yBtn - xBtn:
                    if playArea[i+xBtn] == -1: k += 1           # снизу

                playArea[i] = k

    if btn[n].cget('text') == imgMark:                          # Если поле было промаркировано
        mrk -= 1
        tk.title('В сапёре, '+ str(mines-mrk) +' мины!')

    btn[n].config(text=playArea[n], state=DISABLED, bg='white') # Отображаем игровую ситуацию
    
    if playArea[n] == 0:                                        # Пустое поле без соседей
        btn[n].config(text=' ', bg='#ccb')
    elif playArea[n] == -1:                                     # Мина!
        btn[n].config(text=imgMine)
        if nMoves <= (xBtn * yBtn - mines) or mines >= mrk:       # Если игрок ещё не выиграл, то проиграл
            nMoves = 32000                                      # Если проиграл, то уже не выиграет
            chainReaction(0)                                    # Цепная реакция
            messagebox.showerror("Конец!", "Вы проиграли, начните новую игру!!!")

    if nMoves == (xBtn * yBtn - mines) and mines == mrk:          # Если все клетки открыты и мины помечены
        tk.title('Победа!!! время игры: '+ str(int(time.time() - playTime)) +' сек')
        winner(0)

def chainReaction(j):                               # Цепная реакция
    if j <= len(playArea):                          # Если не запустили новую игру
        for i in range(j, xBtn*yBtn):
            if playArea[i] == -1 and btn[i].cget('text') == ' ':
                btn[i].config(text=imgMine)
                btn[i].flash()
                tk.bell()
                tk.after(50, chainReaction, i + 1)
                break

def winner(j):                                      # Победа
    if j <= len(playArea):                          # Если не запустили новую игру
        for i in range(j, xBtn*yBtn):
            if playArea[i] == 0:
                btn[i].config(state=NORMAL, text='☺')
                btn[i].flash()
                tk.bell()
                btn[i].config(text=' ', state=DISABLED)
                tk.after(50, winner, i + 1)
                break

def marker(n):                                      # помечаем то, где возможно скрывается мина.
    global mrk, mines, playTime
    if (btn[n].cget('state')) != 'disabled':
        if btn[n].cget('text') == imgMark:
            btn[n].config(text=' ')
            mrk -= 1
        else:
            btn[n].config(text=imgMark, fg='red')
            mrk += 1
        tk.title('В сапёре, '+str(mines-mrk)+' маркера!')
    if nMoves == (xBtn*yBtn - mines) and mines == mrk:          # Если все клетки открыты и мины помечены
        tk.title('Победа!!! время игры: '+str(int(time.time() - playTime))+' сек')
        winner(0)

def newGame():
    global xBtn, yBtn, mines, nMoves, mrk
    mines = xBtn * yBtn * 10 // 64
    nMoves = 0; mrk=0
    playArea.clear()
    if len(btn) != 0:
        for i in range (0, len(btn)):
            btn[i].destroy()
        btn.clear()
        for i in range (0, len(frm)):
            frm[i].destroy()
        frm.clear()
    playground()
    tk.title('В сапёре, '+str(mines-mrk)+' мины!')

def set5x5():
    global xBtn, yBtn
    xBtn = 5; yBtn = 5
    newGame()

def set8x8():
    global xBtn, yBtn
    xBtn = 8; yBtn = 8
    newGame()

def set10x14():
    global xBtn, yBtn
    xBtn = 10; yBtn = 14
    newGame()

def set16x16():
    global xBtn, yBtn
    xBtn = 16; yBtn = 16
    newGame()

def set32x32():
    global xBtn, yBtn
    xBtn = 32; yBtn = 32
    newGame()

def playground():
    global xBtn, yBtn

    for i in range(0, yBtn):
        frm.append(Frame())
        frm[i].pack(expand=YES, fill=BOTH)
        for j in  range(0, xBtn):
            btn.append(Button(frm[i], text=' ',font=('mono', 16, 'bold'),
                              width=1, height=1, padx=0, pady=0))
            
    for i in  range(0, xBtn*yBtn):
        if xBtn * yBtn > 256:
            btn[i].config(font=('mono', 8, 'normal'))

        btn[i].config(command=lambda n=i: play(n))
        btn[i].bind('<Button-3>', lambda event, n=i: marker(n))
        btn[i].pack(side=LEFT, expand=YES, fill=BOTH, padx=0, pady=0)
        btn[i].update()
        playArea.append(0)                      # Создаём элементы списка playArea

frmTop = Frame()                                # Создаём кнопки "New game"
frmTop.pack(expand=YES, fill=BOTH)
Label(frmTop, text=' Новая игра:  ').pack(side=LEFT, expand=NO, fill=X, anchor=N)
Button(frmTop, text='5x5', font=(16),
       command=set5x5).pack(side=LEFT, expand=YES, fill=X, anchor=N)

Button(frmTop, text='8x8', font=(16),
       command=set8x8).pack(side=LEFT, expand=YES, fill=X, anchor=N)

Button(frmTop, text='10x14', font=(16),
       command=set10x14).pack(side=LEFT, expand=YES, fill=X, anchor=N)

Button(frmTop, text='16x16', font=(16),
       command=set16x16).pack(side=LEFT, expand=YES, fill=X, anchor=N)

Button(frmTop, text='32x32', font=(16),
       command=set32x32).pack(side=LEFT, expand=YES, fill=X, anchor=N)

mainloop()
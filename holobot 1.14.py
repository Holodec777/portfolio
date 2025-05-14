import pyautogui as pg
import pyperclip
import time
from tkinter import *
from tkinter import font
import random

def click1():
    pg.click(339, 295, 1)

def click2():
    pg.click(799, 295, 1)

def click3():
    pg.click(1519, 295, 1)

def click4():
    pg.click(239, 628, 1)

def click5():
    pg.click(784, 635, 1)

def click6():
    pg.click(1417, 624, 1)

def click7():
    pg.click(235, 973, 1)

def click8():
    pg.click(1512, 965, 1)

def click9():
    pg.click(1512, 965, 1)

def paste(text: str):
    buffer = pyperclip.paste()
    pyperclip.copy(text)
    pg.hotkey("ctrl", "shift", "v") # "shift",
    pyperclip.copy(buffer)

def spamming1():
    count = int(ent1.get())
    time1: float = float(ent2.get())
    text1 = phrase1.get()
    text2 = phrase2.get()
    text3 = phrase3.get()
    text4 = phrase4.get()
    text5 = phrase5.get()
    text6 = phrase6.get()
    text7 = phrase7.get()
    text8 = phrase8.get()
    text9 = phrase9.get()
    text10 = phrase10.get()
    for i in range(count):
        phrases = []
        phrases.append(text1)
        phrases.append(text2)
        phrases.append(text3)
        phrases.append(text4)
        phrases.append(text5)
        phrases.append(text6)
        phrases.append(text7)
        phrases.append(text8)
        phrases.append(text9)
        phrases.append(text10)

        clicks = [click1, click2, click3, click4, click4, click6, click7, click8, click9]
        random.shuffle(clicks)
        clicks[0]()
        paste(random.choice(phrases))
        pg.hotkey("enter")
        time.sleep(time1)

def testing():
    count = int(ent1.get())
    time1: float = float(ent2.get())
    text1 = phrase1.get()
    text2 = phrase2.get()
    text3 = phrase3.get()
    text4 = phrase4.get()
    text5 = phrase5.get()
    text6 = phrase6.get()
    text7 = phrase7.get()
    text8 = phrase8.get()
    text9 = phrase9.get()
    text10 = phrase10.get()
    for i in range(count):


        phrases = [ ]
        phrases.append(text1)
        phrases.append(text2)
        phrases.append(text3)
        phrases.append(text4)
        phrases.append(text5)
        phrases.append(text6)
        phrases.append(text7)
        phrases.append(text8)
        phrases.append(text9)
        phrases.append(text10)

        if phrases[0] == '':
            pass
        else:
            pg.click(1520, 840, 1)
            paste(phrases[0])
            pg.hotkey("enter")
            time.sleep(time1)

        if phrases[1] == '':
            pass
        else:
           pg.click(1520, 840, 1)
           paste(phrases[1])
           pg.hotkey("enter")
           time.sleep(time1)


        if phrases[2] == '':
            pass
        else:
            pg.click(1520, 840, 1)
            paste(phrases[2])
            pg.hotkey("enter")
            time.sleep(time1)

        if phrases[3] == '':
            pass
        else:
            pg.click(1520, 840, 1)
            paste(phrases[3])
            pg.hotkey("enter")
            time.sleep(time1)

        if phrases[4] == '':
            pass
        else:
            pg.click(1520, 840, 1)
            paste(phrases[4])
            pg.hotkey("enter")
            time.sleep(time1)

        if phrases[5] == '':
            pass
        else:
            pg.click(1520, 840, 1)
            paste(phrases[5])
            pg.hotkey("enter")
            time.sleep(time1)

        if phrases[6] == '':
            pass
        else:
            pg.click(1520, 840, 1)
            paste(phrases[6])
            pg.hotkey("enter")
            time.sleep(time1)

        if phrases[7] == '':
            pass
        else:
            pg.click(1520, 840, 1)
            paste(phrases[7])
            pg.hotkey("enter")
            time.sleep(time1)

        if phrases[8] == '':
            pass
        else:
            pg.click(1520, 840, 1)
            paste(phrases[8])
            pg.hotkey("enter")
            time.sleep(time1)

        if phrases[9] == '':
            pass
        else:
            pg.click(1520, 840, 1)
            paste(phrases[9])
            pg.hotkey("enter")
            time.sleep(time1)
def callibrate():

    pg.click(339, 295, 1)
    pg.click(799, 295, 1)
    pg.click(1519, 295, 1)

    pg.click(239, 628, 1)
    pg.click(784, 635, 1)
    pg.click(1417, 624, 1)

    pg.click(235, 973, 1)
    pg.click(798, 965, 1)
    pg.click(1512, 965, 1)

# НАСТРОЙКИ ОКНА
root = Tk()

root['bg'] = '#030303'
root.title('Holobot 1.14')
root.geometry('300x600')

root.resizable(width=False, height=False)

font1 = font.Font(family="Helvetica", size=25, weight=font.BOLD)
font2 = font.Font(family="Helvetica", size=15, weight=font.BOLD)

# НАСТРОЙКИ КАНВАСА
canvas = Canvas(root, height=300, width=600)
canvas.pack()

# НАСТРОЙКИ РАМКИ В КАНВАСЕ
frame = Frame(root, bg='#030303')
frame.place(relwidth=1, relheight=1)

# ОКНО С НАЗВАНИЕМ ПРОГРАММЫ
title = Label(frame, text='HOLOBOT 1.14', fg='#00FF00', bg='#030303', font=font1)
title.place(relwidth=1, relheight=0.09)

# КНОПКА НАЧАТЬ РАБОТУ В СТАНДАРТНОМ РЕЖИМЕ
btn = Button(frame, text='РАНДОМ', fg='#030303', bg='#7CFC00', activebackground='#ADFF2F', font=font2,
             command=spamming1)
btn.place(relwidth=1, relheight=0.07, rely=0.09)

# КНОПКА НАЧАТЬ РАБОТУ В РЕЖИМЕ RANDOM
btn1 = Button(frame, text='ОБЫЧНЫЙ', fg='#030303', bg='#7CFC00', activebackground='#ADFF2F', font=font2,
             command=testing)
btn1.place(relwidth=1, relheight=0.07, rely=0.16)

# КНОПКА НАЧАТЬ РАБОТУ В РЕЖИМЕ RANDOM.SHUFFLE
btn2 = Button(frame, text='КАЛЛИБРОВКА', fg='#030303', bg='#7CFC00', activebackground='#ADFF2F', font=font2,
             command=callibrate)
btn2.place(relwidth=1, relheight=0.07, rely=0.23)

# НАДПИСЬ НАД ОКОШКОМ ДЛЯ ВВОДА ТЕКСТА, КОТОРЫЙ ВЫВОДИТСЯ В ЧАТ
title2 = Label(frame, text='ФРАЗЫ:', fg='white', bg='#030303', font=font2)
title2.place(relwidth=1, relheight=0.07, rely=0.3)

# ОКНО ВВОДА ТЕКСТА ДЛЯ ВЫВОДА В ЧАТ №1
phrase1 = Entry(frame, bg="white")
phrase1.place(relwidth=1, relheight=0.035, rely=0.37)

# ОКНО ВВОДА ТЕКСТА ДЛЯ ВЫВОДА В ЧАТ №2
phrase2 = Entry(frame, bg="white")
phrase2.place(relwidth=1, relheight=0.035, rely=0.405)

# ОКНО ВВОДА ТЕКСТА ДЛЯ ВЫВОДА В ЧАТ №3
phrase3 = Entry(frame, bg="white")
phrase3.place(relwidth=1, relheight=0.035, rely=0.44)

# ОКНО ВВОДА ТЕКСТА ДЛЯ ВЫВОДА В ЧАТ №4
phrase4 = Entry(frame, bg="white")
phrase4.place(relwidth=1, relheight=0.035, rely=0.475)

# ОКНО ВВОДА ТЕКСТА ДЛЯ ВЫВОДА В ЧАТ №5
phrase5 = Entry(frame, bg="white")
phrase5.place(relwidth=1, relheight=0.035, rely=0.51)

# ОКНО ВВОДА ТЕКСТА ДЛЯ ВЫВОДА В ЧАТ №6
phrase6 = Entry(frame, bg="white")
phrase6.place(relwidth=1, relheight=0.035, rely=0.545)

# ОКНО ВВОДА ТЕКСТА ДЛЯ ВЫВОДА В ЧАТ №7
phrase7 = Entry(frame, bg="white")
phrase7.place(relwidth=1, relheight=0.035, rely=0.58)

# ОКНО ВВОДА ТЕКСТА ДЛЯ ВЫВОДА В ЧАТ №8
phrase8 = Entry(frame, bg="white")
phrase8.place(relwidth=1, relheight=0.035, rely=0.615)

# ОКНО ВВОДА ТЕКСТА ДЛЯ ВЫВОДА В ЧАТ №9
phrase9 = Entry(frame, bg="white")
phrase9.place(relwidth=1, relheight=0.035, rely=0.65)

# ОКНО ВВОДА ТЕКСТА ДЛЯ ВЫВОДА В ЧАТ №10
phrase10 = Entry(frame, bg="white")
phrase10.place(relwidth=1, relheight=0.035, rely=0.685)

# НАДПИСЬ НАД ОКОШКОМ ДЛЯ ВВОДА КОЛИЧЕСТВА РАЗ ВВОДА ТЕКСТА В ЧАТ
title3 = Label(frame, text='КАКОЕ КОЛИЧЕСТВО РАЗ:', fg='white', bg='#030303', font=font2)
title3.place(relwidth=1, relheight=0.07, rely=0.72)

# ОКНО ДЛЯ ВВОДА КОЛИЧЕСТВА РАЗ ВВОДА ТЕКСТА В ЧАТ
ent1 = Entry(frame, bg="white")
ent1.place(relwidth=1, relheight=0.07, rely=0.79)

# НАДПИСЬ НАД ОКОШКОМ ДЛЯ ВВОДА ВРЕМЕНИ ЗАДЕРЖКИ ОТПРАВКИ СООБЩЕНИЙ
title4 = Label(frame, text='ЗАДЕРЖКА (СЕК)', fg='white', bg='#030303', font=font2)
title4.place(relwidth=1, relheight=0.07, rely=0.86)

# ОКНО ДЛЯ ВВОДА ВРЕМЕНИ ЗАДЕРЖКИ ОТПРАВКИ СООБЩЕНИЙ
ent2 = Entry(frame, bg="white")
ent2.place(relwidth=1, relheight=0.07, rely=0.93)

#print(pg.position())
root.mainloop()
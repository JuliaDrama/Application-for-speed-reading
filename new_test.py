import tkinter as tk
from datetime import datetime
from random import choice, randrange
import pygame, time

pygame.init()
global root

global computer
f_temp = '00:00'
flag = False


def start_game():

    global computer

    def play():
        pygame.mixer.music.load("samyi-korotkiy-zvuk-sms.mp3")
        pygame.mixer.music.play(0)

    def play1():
        pygame.mixer.music.load("facebook-uvedomlenie_IWQFOPF1.mp3")
        pygame.mixer.music.play(0)

    def sound_victory():
        pygame.mixer.music.load("victorrry.mp3")
        pygame.mixer.music.play(0)

    def link_button(link):
        button = link
        button.config(state=tk.DISABLED)

    def check_button(button):
        global computer
        if button["text"] == str(computer):
            button.config(state=tk.DISABLED)
            computer += 1
            label["text"] = f"Далее {computer}"
            play1()
        else:
            play()
        if button["text"] == 'b':
            play()
        if computer == 9:
            sound_victory()
            time.sleep(2)
            game_win.destroy()
            stat()
            flag = True

    computer = 1
    list_numbers = list(range(1, 9))
    game_win = tk.Toplevel()
    temp = 0
    after_id = ''

    game_win.geometry("500x600")
    frame_top = tk.Frame(game_win, width=700, height=700)
    frame_top.place(x=100, y=150)
    our_image = tk.PhotoImage(file="rec (1).png")
    label = tk.Label(game_win, text=f"Далее {computer}", font=15)
    label.place(x=100, y=50)
    label2 = tk.Label(game_win, text=f"Время: 00:00 ", font=15)
    label2.place(x=300, y=50)
    for i in range(3):
        for j in range(3):
            if i == j == 1:

                lbl = tk.Label(frame_top, image=our_image)

                lbl.grid(row=i, column=j)

            else:
                number = choice(list_numbers)
                list_numbers.remove(number)
                but = tk.Button(frame_top, text=f"{number}", font=10)
                but.config(command=lambda b=but: check_button(b))
                but.grid(row=i, column=j, stick='wens')
        frame_top.grid_rowconfigure(i, minsize=80)
        frame_top.grid_columnconfigure(i, minsize=80)
    sec = 0
    if flag:
        temp = 0
    def tick():
        global f_temp
        nonlocal temp, after_id
        after_id = game_win.after(1000, tick)
        f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
        print(type(f_temp))
        label2.configure(text=f'Время: {f_temp}')
        temp += 1

    tick()

    game_win.mainloop()

def stat():
    global flag
    flag = True

    win_stat = tk.Tk()
    win_stat.geometry('300x300')
    label = tk.Label(win_stat, text="Статистика")
    label.place()
    label3 = tk.Label(win_stat, text=f'Текущее время: {f_temp}')
    label3.pack()
    button = tk.Button(win_stat, text="Начать заново", command=start_game)
    button.pack()
    win_stat.mainloop()


def main_win():
    global root
    root = tk.Tk()
    root.geometry('300x300')
    button = tk.Button(root, text="Начать игру!", command=start_game)
    button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    root.mainloop()


main_win()

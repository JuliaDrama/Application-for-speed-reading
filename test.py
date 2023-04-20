import tkinter as tk
from random import randrange, choice
import pygame
import time
pygame.init()

computer = 1


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


win = tk.Tk()
win.geometry(f"400x500+100+200")
win.title("Мое первое графическое приложение")

list_numbers = list(range(1, 9))

counter = 1
list_buttons = []

win0 = tk.Tk()
win0.title('Start game!')


def check_button(button):
    global computer
    if button["text"] == str(computer):
        button.config(state=tk.DISABLED)
        computer += 1
        play1()
    else:
        play()
    if button["text"] == 'b':
        play()
    if computer == 9:
        sound_victory()


frame_top = tk.Frame(win, width=700, height=700)
frame_top.place(x=100, y=150)

for i in range(3):
    for j in range(3):
        but = f'btn{counter}'
        if i == j == 1:
            our_image = tk.PhotoImage(file="rec (1).png")
            but = tk.Button(frame_top, font=10, image=our_image, border=1, text='b', foreground='white')
            but.config(command=lambda b=but: check_button(b))
            but.grid(row=i, column=j, stick='wens')
            counter += 1
            list_buttons.append(but)
        else:
            but = f'btn{counter}'
            number = choice(list_numbers)
            list_numbers.remove(number)
            but = tk.Button(frame_top, text=f"{number}", font=10)
            but.config(command=lambda b=but: check_button(b))
            but.grid(row=i, column=j, stick='wens')
            list_buttons.append(but)
    frame_top.grid_rowconfigure(i, minsize=80)
    frame_top.grid_columnconfigure(i, minsize=80)


win.mainloop()

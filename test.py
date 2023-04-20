import tkinter as tk
from random import randrange, choice
import pygame
from PIL import Image, ImageTk
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


# def destroy_game_win():
#     global game_win
#     game_win.destroy

list_numbers = list(range(1, 9))


list_buttons = []

win0 = tk.Tk()


def create_start_win():
    win0.geometry("450x560+500+200")
    win0.title('Start game!')
    photo = ImageTk.PhotoImage(Image.open("brain.jpg"))
    lbl = tk.Label(image=photo, width=400, height=200)
    lbl.place(x=30, y=50)
    btn = tk.Button(text='Начать', font="Arial 20", command=create_game_win)
    btn.place(x=180, y=270)
    mainloop_start_win()


def mainloop_start_win():
    global win0
    win0.mainloop()


def create_game_win():
    win0.destroy()
    global game_win
    game_win = tk.Tk()
    game_win.geometry(f"450x560+500+200")
    game_win.title("Мое первое графическое приложение")
    game()
    game_win.mainloop()
def game():
    counter = 1
    frame_top = tk.Frame(game_win, width=700, height=700)
    frame_top.place(x=100, y=150)
    our_image = tk.PhotoImage(file="rec (1).png")
    for i in range(3):
        for j in range(3):
            if i == j == 1:
                # but = tk.Button(frame_top, font=10, image=our_image)
                lbl = tk.Label(frame_top, image=our_image)
                # but.config(command=lambda b=but: check_button(b))
                # but.grid(row=i, column=j, stick='wens')
                lbl.grid(row=i, column=j)
                # counter += 1
                # btn = tk.Button(frame_top, image=our_image)
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
        time.sleep(2)
        game_win.destroy()


create_start_win()


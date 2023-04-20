import tkinter as tk

from random import choice, randrange
import pygame, time
pygame.init()

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
        label["text"]=f"Далее {computer}"
        play1()
    else:
        play()
    if button["text"] == 'b':
        play()
    if computer == 9:
        sound_victory()
        time.sleep(2)
        game_win.destroy()


computer = 1
list_numbers = list(range(1, 9))
game_win = tk.Tk()
game_win.geometry("500x600")
frame_top = tk.Frame(game_win, width=700, height=700)
frame_top.place(x=100, y=150)
our_image = tk.PhotoImage(file="rec (1).png")
label = tk.Label(game_win, text=f"Далее {computer}", font=15)
label.place(x=100, y=50)
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

game_win.mainloop()
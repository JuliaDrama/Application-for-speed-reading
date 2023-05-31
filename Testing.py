import tkinter as tk
from random import *
import pygame
import time
from datetime import datetime
from PIL import Image, ImageTk
pygame.init()
root = tk.Tk()
root.geometry('600x600')
root.resizable(width=False, height=False)
global counter
counter = 0
mistakes = 0
global lbl
global lbl1

#----------------
global computer
f_temp = '00:00'
flag = False
open = False
global win_stat


def stat():
    global open
    global flag
    global root

    global best_sec
    win_stat = tk.Toplevel()
    open = True
    win_stat.geometry('500x600+100+100')
    label = tk.Label(win_stat, text="Статистика")
    label.place()
    label3 = tk.Label(win_stat, text=f'Текущее время: {f_temp}')
    label3.pack()
    if int(f_temp[3:]) < best_sec:
        best_sec = int(f_temp[3:])

    label4 = tk.Label(win_stat, text=f'Лучшее время: 00:{best_sec:02}')
    label4.pack()
    button = tk.Button(win_stat, text="Начать заново", command=start_game)
    button.pack()
    win_stat.mainloop()


def start_game():
    global best_sec, f_temp
    global computer
    global root
    global win_stat
    global open
    global flag
    if 'win_stat' in globals():
        win_stat.destroy()
    if flag:
        root.destroy()
        flag = False

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
        global best_sec
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
            flag = True
            sound_victory()
            time.sleep(2)
            game_win.destroy()
            stat()

    computer = 1
    list_numbers = list(range(1, 9))
    game_win = tk.Toplevel()
    temp = 0
    after_id = ''

    game_win.geometry("500x600+100+100")
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
        global f_temp, best_sec
        nonlocal temp, after_id

        after_id = game_win.after(1000, tick)
        f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
        label2.configure(text=f'Время: {f_temp}')
        temp += 1

    tick()

    game_win.mainloop()


best_sec = 50


def main_win():
    global root

    root = tk.Tk()
    flag = True
    root.geometry('500x600+100+100')
    button = tk.Button(root, text="Начать игру!", command=start_game)
    button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    root.mainloop()
#--------------------
colors = [
    ('Красный', 'red'),
    ('Оранжевый', 'orange'),
    ('Желтый', 'yellow'),
    ('Зеленый', 'green'),
    ('Голубой', 'blue'),
    ('Синий', 'dark blue'),
    ('Розовый', 'violet'),
    ('Коричневый', 'brown')
]
dict_colors = {

'red': 'Красный',
'orange': 'Оранжевый',
'yellow': 'Желтый',
'green': 'Зеленый',
'blue': 'Голубой',
'dark blue': 'Синий',
'violet': 'Розовый',
'brown':'Коричневый'

}

#
# def start_game():
#     random_color = randrange(len(colors))
#     lbl.config(text=colors[random_color][0])
#     interface()


def play1():
    pygame.mixer.music.load("facebook-uvedomlenie_IWQFOPF1.mp3")
    pygame.mixer.music.play(0)


def play():
    pygame.mixer.music.load("samyi-korotkiy-zvuk-sms.mp3")
    pygame.mixer.music.play(0)


def change_color(button):
    global counter, mistakes

    global frame
    solve = False

    if lbl['text'] == dict_colors[button['background']]:
        counter += 1

        for obj in root.winfo_children():
            obj.destroy()

        game_color_easy()
        play1()
    else:
        play()
        mistakes += 1
    if counter ==10:
        stat()




    # random_color = randrange(len(colors))
    # lbl1.config(text=colors[random_color][0])

start_time = None
temp = 0
after_id = 0
lbl_time = tk.Label(root, text=f'Время: 00:00', font=12)

def game_color_easy():
    global flag
    global lbl
    global lbl1
    global frame

    global lbl

    for obj in root.winfo_children():
        # if obj != lbl_time:
            obj.destroy()

    frame = tk.Frame(root, padx=10)
    lbl = tk.Label(frame, font=('Arial', 14))
    random_color = randrange(len(colors))
    lbl.config(text=colors[random_color][0])
    lbl.grid(pady=50, row=0, column=0, columnspan=4, )
    four_random_colors = [i % len(colors) for i in range(random_color, random_color + 4)]
    shuffle(four_random_colors)
    btn1 = tk.Button(frame, background=colors[four_random_colors[0]][1], width=5)
    btn1.config(command=lambda b=btn1: change_color(b))
    btn1.grid(row=5, column=0, padx=15)

    btn2 = tk.Button(frame, background=colors[four_random_colors[1]][1], width=5)
    btn2.config(command=lambda b=btn2: change_color(b))
    btn2.grid(row=5, column=1, padx=15)

    btn3 = tk.Button(frame, background=colors[four_random_colors[2]][1], width=5)
    btn3.grid(row=5, column=2, padx=15)
    btn3.config(command=lambda b=btn3: change_color(b))

    btn4 = tk.Button(frame, background=colors[four_random_colors[3]][1], width=5)
    btn4.grid(row=5, column=3, padx=15)
    btn4.config(command=lambda b=btn4: change_color(b))

    lbl_time = tk.Label(root, text=f'Время: 00:00', font=12)
    lbl_time.pack(padx=100, pady=10)
    lbl1 = tk.Label(root, text=f'Счет: {counter}', font=12)
    lbl1.pack(padx=50)
    frame.pack()



# def tick():
#     global temp, after_id, lbl_time
#     if lbl_time in root.winfo_children():
#         after_id = root.after(1000, tick)
#     # f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
#     time_str = time.strftime("%M:%S", time.gmtime(temp))
#     lbl_time.configure(text=f'Время: {time_str}')
#     temp += 1


def start_game_color_easy():
    global flag
    flag = True
    for obj in root.winfo_children():
        obj.destroy()

    start_button = tk.Button(root, text="Начать игру", command=game_color_easy)
    start_button.place(relx=0.5, rely=0.5, anchor='center')


def stat():
    for obj in root.winfo_children():
        obj.destroy()
    tk.Label(root, text="Тренировка закончена!", font=('Ubunty', 14)).pack()
    tk.Label(root,text=f"Количество ошибок: {mistakes}", font=('Ubunty', 14)).pack()
    if mistakes > 0:
        tk.Label(root, text="Постарайтесь ещё раз пройти тренировку без ошибок", font=('Ubunty', 14)).pack()
# def start_timer():
#     global lbl_time
#     global start_time
#     start_time = time.time()
#     timer()
#     game_color_easy()


# def timer():
#     global lbl_time
#     global start_time
#     if start_time is not None:
#         seconds = time.time() - start_time
#         time_str = time.strftime("%M:%S", time.gmtime(seconds))
#         lbl_time.config(text=time_str)
#         if time_str != "01:00":
#             root.after(1000, timer)
#         else:
#             start_time = None



# def start_game():
#     #start_label = tk.Label(root, text='Упражнения\nдля cкорочтения', anchor='center')
#     #start_label.pack()
#     #button_Shulte = tk.Button(root, text='Таблица Шульте', width=20, height=2)
#     #button_Shulte.pack()
#     image_table = tk.PhotoImage(file='locator.png')
#     # image_Shulte = ImageTk.PhotoImage(image_table)
#     shulte_label = tk.Label(root, image=image_table, width=5, height=2)
#     shulte_label.pack()

# interface()

# start_game()


image_table = tk.PhotoImage(file='locator.png')
image_color = tk.PhotoImage(file='color-blindness-test (1).png')


def menu():
    # root['bg'] = '#F4EEE1'
    frame_for_menu = tk.Frame(root)
    # frame_for_menu['bg'] = '#F4EEE1'
    name_label = tk.Label(frame_for_menu, text='Упражнения\nдля скорочтения', font=('Comic Sans MS', 14),
                          # background='#F4EEE1'
                          )
    name_label.grid(row=0, column=0, sticky='we', columnspan=2, pady=50)
    shulte_label = tk.Label(frame_for_menu, image=image_table)
    shulte_label.grid(row=1, column=0)
    btn_shulte = tk.Button(frame_for_menu, text="Таблица Шульте", font=('Comic Sans MS', 12), command=main_win)
    btn_shulte.grid(row=1, column=1, sticky='ns', padx=7)
    color_label = tk.Label(frame_for_menu, image=image_color)
    color_label.grid(row=2, column=0, pady=30)
    btn_color = tk.Button(frame_for_menu, text="Назови цвет", font=('Comic Sans MS', 12), command=start_game_color_easy)
    btn_color.grid(row=2, column=1, sticky='we', padx=7)
    frame_for_menu.pack(anchor='nw', padx=170)


menu()




root.mainloop()
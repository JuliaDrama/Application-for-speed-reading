# import tkinter as tk
# import random
# from PIL import ImageTk
# h = 500
# w = 500
# win = tk.Tk()
# win.title('Мое первое графическое приложение')
# win.geometry(f"{h}x{w}+100+150")
#
# list_numbers = list(range(1, 9))
# # for i in range(3):
# #     for j in range(3):
# #
# x1, y1 = 100, 100
# for i in range(3):
#     for j in range(3):
#         txt = tk.Text(win, font='Courier 20', bg='black')
#         btn = f"btn{i}"
#         if i == j == 1:
#             img = tk.PhotoImage()
#             image = ImageTk.PhotoImage(file="rec (1).png")
#             btn = tk.Button(win, width=80, height=80, bd=5, relief=tk.GROOVE, image=image, state=tk.NORMAL, border=4)
#             btn.place(x=x1+2, y = y1)
#             x1 += 80
#         else:
#             number = random.choice(list_numbers)
#             list_numbers.remove(number)
#             btn = tk.Button(win, width=10, height=5, bd=5, fg='black', relief=tk.GROOVE, text=str(number), font=('Courier 15'))
#             btn.place(x=x1, y=y1)
#             x1 += 80
#     y1 += 80
#     x1 -= 80 * 3
# win.mainloop()

import tkinter as tk


win = tk.Tk()
win.geometry("400x500+500+200")
win.title('Start game!')
photo = tk.PhotoImage(file="rec (1).png")
btn = tk.Button(image=photo, width=100, height=100)
btn.pack()
win.mainloop()
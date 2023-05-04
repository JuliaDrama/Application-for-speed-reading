# import turtle
#
# colors = ['blue', 'black', 'red', 'yellow', 'green']
# turtle.pensize(5)
# x = 210
# turtle.speed(0)
# for i in range(len(colors)):
#     if i in (0, 1, 2):
#         turtle.pencolor(colors[i])
#         turtle.circle(100)
#         turtle.penup()
#         turtle.goto(x, 0)
#         turtle.pendown()
#         x += 210
#     else:
#         turtle
#
# turtle.done()
# import turtle
# turtle.speed(0)
# r = 50
# pensize = 10
# turtle.Screen().setup(1000, 600)
# turtle.pensize(pensize)
#
# points = {
#           1: {"pos": (0, 0), "color": "cyan"},
#           2: {"pos": (r * 2, 0), "color": "black"},
#           3: {"pos": (r * 4, 0), "color": "red"},
#           4: {"pos": (r, -r), "color": "orange"},
#           5: {"pos": (r * 3, -r), "color": "chartreuse"}
#           }
#
# for i in range(1, 6):
#     turtle.penup()
#     turtle.pencolor(points[i]["color"])
#     turtle.goto(points[i]["pos"])
#     turtle.pendown()
#     turtle.circle(r - pensize / 2)
# turtle.penup()
# turtle.goto(50, -50)
# turtle.pendown()
# turtle.pencolor('orange')
# turtle.speed(1)
# turtle.circle(45, 45)
# turtle.pencolor('black')
# turtle.circle(45, 10)
# turtle.pencolor('orange')
# turtle.circle(45, 45)
#
#
# turtle.done()
# объявление функции

# from __future__ import annotations
# from typing import List, Dict
#
#
# class Share:
#     def __init__(self, ticker: str, quantity: int, price: float) -> None:
#         self.ticker = ticker
#         self.quantity = quantity
#         self.price = price
#
#     def get_value(self, currency: str, rate: float) -> float:
#         if currency == "RUB":
#             return self.quantity * self.price * rate
#         elif currency == "CNY":
#             return self.quantity * self.price * rate
#         elif currency == "USD":
#             return self.quantity * self.price
#
#
# class Bond:
#     def __init__(self, ticker: str, face_value: float, coupon_rate: float, quantity: int, price: float) -> None:
#         self.ticker = ticker
#         self.face_value = face_value
#         self.coupon_rate = coupon_rate
#         self.quantity = quantity
#         self.price = price
#
#     def get_value(self, currency: str, rate: float) -> float:
#         try:
#             if currency == "RUB":
#                 return self.quantity * (self.face_value * self.coupon_rate / 100) * rate
#             elif currency == "CNY":
#                 return self.quantity * (self.face_value * self.coupon_rate / 100) * rate
#             elif currency == "USD":
#                 return self.quantity * self.face_value * self.coupon_rate / 100
#             else:
#                 raise ValueError("Unsupported currency")
#         except ValueError as e:
#             print(e)
#
#
# class InvestorPortfolio:
#     def __init__(self, shares: List[Share], bonds: List[Bond]) -> None:
#         self.shares = shares
#         self.bonds = bonds
#
#     def get_portfolio_value(self, currency: str, rate: float) -> Dict[str, float]:
#         total_value = 0
#         portfolio_value = {}
#
#         for share in self.shares:
#             total_value += share.get_value(currency, rate)
#             portfolio_value[share.ticker] = share.get_value(currency, rate)
#
#         for bond in self.bonds:
#             total_value += bond.get_value(currency, rate)
#             portfolio_value[bond.ticker] = bond.get_value(currency, rate)
#
#         portfolio_value["Total Value"] = total_value
#
#         return portfolio_value
#
#
# sberbank = Share("SBER", 100, 200)
# gazprom = Share("GAZP", 50, 300)
# lukoil = Share("LKOH", 25, 500)
# bond1 = Bond("MBT", 1000, 5, 10, 800)
# bond2 = Bond("VTB", 500, 3, 50, 400)
#
# portfolio = InvestorPortfolio([sberbank, gazprom, lukoil], [bond1, bond2])
# print(portfolio.get_portfolio_value("RUB", 70))
# print(portfolio.get_portfolio_value("CNY", 6))
# print(portfolio.get_portfolio_value("USD", 1))
# from typing import List, Dict
#
#
# class CurrencyMismatchError(Exception):
#     pass
#
#
# class Share:
#     def __init__(self, ticker: str, quantity: int, price: float) -> None:
#         if quantity < 0:
#             raise ValueError("Quantity of shares cannot be negative")
#         if price < 0:
#             raise ValueError("Price per share cannot be negative")
#         self.ticker = ticker
#         self.quantity = quantity
#         self.price = price
#
#     def get_value(self, currency: str, rate: float) -> float:
#         if currency == "RUB":
#             return self.quantity * self.price * rate
#         elif currency == "CNY":
#             return self.quantity * self.price * rate
#         elif currency == "USD":
#             return self.quantity * self.price
#         else:
#             raise ValueError("Unsupported currency")
#
#     def __str__(self):
#         return f"{self.ticker}: {self.quantity} shares at {self.price} per share"
#
#
# class Bond:
#     def __init__(self, ticker: str, face_value: float, coupon_rate: float, quantity: int, price: float) -> None:
#         if face_value < 0:
#             raise ValueError("Face value of bond cannot be negative")
#         if coupon_rate < 0:
#             raise ValueError("Coupon rate of bond cannot be negative")
#         if quantity < 0:
#             raise ValueError("Quantity of bonds cannot be negative")
#         if price < 0:
#             raise ValueError("Price per bond cannot be negative")
#         self.ticker = ticker
#         self.face_value = face_value
#         self.coupon_rate = coupon_rate
#         self.quantity = quantity
#         self.price = price
#
#     def get_value(self, currency: str, rate: float) -> float:
#         if currency == "RUB":
#             return self.quantity * (self.face_value * self.coupon_rate / 100) * rate
#         elif currency == "CNY":
#             return self.quantity * (self.face_value * self.coupon_rate / 100) * rate
#         elif currency == "USD":
#             return self.quantity * self.face_value * self.coupon_rate / 100
#         else:
#             raise ValueError("Unsupported currency")
#
#     def __str__(self):
#         return f"{self.ticker}: {self.quantity} bonds at {self.price} per bond"
#
#
# class InvestorPortfolio:
#     def __init__(self, shares: List[Share], bonds: List[Bond]) -> None:
#         self.shares = shares
#         self.bonds = bonds
#
#     def get_portfolio_value(self, currency: str, rate: float) -> Dict[str, float]:
#         if currency not in ['RUB', 'CNY', 'USD']:
#             raise ValueError(f"Unsupported currency {currency}")
#         total_value = 0
#         portfolio_value = {}
#
#         for share in self.shares:
#             if share.get_value(currency, rate) < 0:
#                 raise CurrencyMismatchError(f"Value of {share.ticker} shares is negative in {currency}")
#             total_value += share.get_value(currency, rate)
#             portfolio_value[share.ticker] = share.get_value(currency, rate)
#
#         for bond in self.bonds:
#             if bond.get_value(currency, rate) < 0:
#                 raise CurrencyMismatchError(f"Value of {bond.ticker} bonds is negative in {currency}")
#             total_value += bond.get_value(currency, rate)
#             portfolio_value[bond.ticker] = bond.get_value(currency, rate)
#
#         portfolio_value["Total Value"] = total_value
#
#         return portfolio_value
#
#     def __str__(self):
#         return f"Portfolio: \nShares: {[str(share) for share in self.shares]}\nBonds: {[str(bond) for bond in self.bonds]}"
#
# # Инициализируем акции и облигации
#
# sber = Share("SBER", 100, 200)
# gazprom = Share("GAZP", 50, 300)
# vtb = Bond("VTB", 500, 3, 50, 400)
# mbt = Bond("MBT", 1000, 5, 10, 800)
#
# # Получаем стоимость акций в USD при курсе 1 USD = 75 RUB
# sber_value = sber.get_value("USD", 75)
#
# # Получаем стоимость облигаций в CNY при курсе 1 CNY = 10 RUB
# vtb_value = vtb.get_value("CNY", 0.1)
#
# # Создаем инвестиционный портфель из акций и облигаций
# port = InvestorPortfolio([sber, gazprom], [vtb, mbt])
#
# # Получаем стоимость портфеля в USD при курсе 1 USD = 75 RUB
# portfolio_value = port.get_portfolio_value("USD", 75)
# print(portfolio_value)
#
# # Получаем стоимость портфеля в CNY при курсе 1 CNY = 10 RUB
# portfolio_value = port.get_portfolio_value("CNY", 0.1)
# print(portfolio_value)
import tkinter as tk

def open_new_window():
    root.destroy()
    new_window = tk.Tk()

root = tk.Tk()
button = tk.Button(root, text="Open new window", command=open_new_window)
button.pack()
root.mainloop()
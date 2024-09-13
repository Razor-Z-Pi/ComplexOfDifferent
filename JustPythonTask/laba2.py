import math
import random

# Task 1

x = int(input())
y = int(input())

if (x > 0) and (y > 0):
    print("1 четверть")
elif (x < 0) and (y > 0):
    print("2 четверть")
elif (x < 0) and (y < 0):
    print("3 четверть")
elif (x > 0) and (y < 0):
    print("4 четверть")
else:
    print("точка находиться на оси!!!")

# Task 2

n1 = int(input())
n2 = int(input())
n3 = int(input())

if ((n1 > n2) and (n1 > n3)):
    print("Максимальное число = { ", n1, " }")
elif ((n2 > n1) and (n2 > n3)):
    print("Максимальное число = { ", n2, " }")
else:
        print("Максимальное число = { ", n3, " }")

# Task 3 

n1 = int(input())
n2 = int(input())
n3 = int(input())

if (((n1 > n2) and (n1 < n3)) or ((n1 < n2) and (n1 > n3))):
    print("Среднее число = { ", n1, " }")
elif ((n2 > n1) and (n2 < n3) or ((n2 < n1) and (n2 > n3))):
    print("Среднее число = = { ", n2, " }")
else:
        print("Среднее число = = { ", n3, " }")

# Task 4 

a = int(input())
b = int(input())
c = int(input())

if (a == 0) or (b == 0) or (c == 0):
    print("Треуголик не существует!!!")
elif a > (b + c):
    print("Треуголик не существует!!!")
elif b > (a + c):
    print("Треуголик не существует!!!")
elif c > (a + b):
    print("Треуголик не существует!!!")
else:
    print("Треуголик существует!!!")    

# Task 5 

a = int(input())
b = int(input())

a = math.pow(a, 2)

if a == b:
    print("Являеться квадратом")
else:
    print("Не являеться квадратом")

# Task 6

n = int(input())

if (n > 0) and (n < 8):
    if n == 1:
        print("Понедельник")
    if n == 2:
        print("Вторник")
    if n == 3:
        print("Среда")
    if n == 4:
        print("Четверг")
    if n == 5:
        print("Пятница")
    if n == 6:
        print("Суббота")
    if n == 7:
        print("Воскресенье")
else:
    print("Вышли за границы")

# Task 7

n = input()

if int(n) > 99:
    n = n[2]
    print(n)
else:
    print("Третий цыфры нет")

# Task 8

n = int(input())

if n % 4 != 0:
    print(365)
elif n % 100 != 0:
    print(366)
elif n % 400 != 0:
    print(365)
else:
    print(366)

# Task 9

n = str(random.randint(1, 999))
print(n)
if int(n) % 2 == 0:
    print("Четное ", len(n), "-x значное число")
else:
    print("Нечетное ", len(n), "-x значное число")
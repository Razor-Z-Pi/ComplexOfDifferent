import random

# Task 1

str = input("Введи строку: ")

i = 0

while i == 0:
    print(str[::-1])
    i = 1

# Task 2

n = int(input())

factor = 1

for i in range(2, n + 1):
    factor *= i
    print(factor)

# Task 3

n = int(input())
result = 0

if n % 2 == 0:
    for i in range(1, n + 1):
        if i % 2 == 0:
            result += i
            print(result)
else:
    for i in range(1, n + 1):
        if i % 2 != 0:
            result += i
            print(result)

print(result)

# Task 4

n = str(random.randint(1, 999))
num = n[::-1]

while True:
    if (num == n):
        print(n," являеться палиндромом")
    else:
        print(n ,"не являеться палиндромом")
    break

# Task 5

for i in range(1, 101):
    k = 0
    j = i // 2
    while j > 0 and k < 2:
        k += (i % j == 0)
        j -= 1
    if k == 1:
        print(i)

# Task 6

n = int(input())
sum = 0

for i in range(1, n + 1):
    print(i)
    sum += i

print(sum)

# Task 7

i = 1
sum = 0

while i != 0:
    i = float(input()) 
    sum += i

print(sum)

# Task 8

n = int(input())
numb = 0

for i in range(1, int(n / 2) + 1):
    if n % i == 0:
        print(i)
        numb = n        
print(n)

# Task 9
t1 = float(input()) 
t2 = float(input()) 
dt = float(input()) 

print("_________________\n",
      "C", " " * 5, " F"
      "_________________\n")

for i in range(int(t1), int(t2) + 1, int(dt)):
    print(i, "  " * 5, (9/5) * i + 32)  

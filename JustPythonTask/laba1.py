import math

# Task №1
a = int(input())
b = int(input())

if (a > 0) and (b > 0):
    print(math.sqrt(a * b))
else:
    print("Вы ввели отрицательные числа")

# Task №2
x = int(input())

if (x > 9) and (x < 100):
    x1 = x % 10
    x2 = x / 10
    print(x1 + int(x2))
else:
    print("Введите двухзначное число!!!")

 
# Task №3
pr = int(input())
if (pr > 9) and (pr < 100):
    s1 = pr % 10
    s2 = pr / 10
    print(str(s1) + "  " + str(int(s2)))
else:
    print("Введите двухзначное число!!!")

# Task №4
f = int(input())

print((f - 32) * 5 / 9)

# Task №5
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

print(math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2)))

# Task №6
num = int(input())

if (num > 999) and (num < 10000):
    n1 =  num / 1000
    n2 =  num / 100 % 10
    n3 =  num / 10 % 10
    n4 =  num % 10
    print(int(n1) + int(n2) + int(n3) + int(n4))
else:
    print("Введите четырехзначное число!!!")

# Task №7
s = '123456789'
print(s[2], s[4], s[4], s[5], s[6])
print(s[-5], s[-3], s[-5], s[-4], s[-3])

# Task №8
st = 'AaBbCcDd'
xlow=[] 
msup=[] 
for i in st: 
	if i.islower(): 
		xlow.append(i) 
	if i.isupper(): 
		msup.append(i) 
		
print(*msup,sep="") 
print(*xlow,sep="")

# Task №9
print("." * 5 + " " + "! " + "! " + "! " + "." * 5)
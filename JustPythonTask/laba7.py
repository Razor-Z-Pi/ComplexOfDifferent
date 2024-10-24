import random

#Task 1

def sr_number_value(l):
    s = sum(l)
    leng = len(l)
    return s / leng

list = [random.randint(0, 10) for i in range(0, 10)]
print(list)
result = sr_number_value(list)
print(" Среднее арифметическое = ", result)

#Task 2

def number_value(n):
    if n % 2 == 0:
        return "четное"
    else:
        return "нечетное"

n = int(input("Введите число: "))
print("Число = ", number_value(n))

#Task 3

def number_value_pow(a, b):
    return a ** b

n = int(input("Введите число: "))
b = int(input("Введите степень: "))
print("Число = ", number_value_pow(n,b))

#Task 4

def number_value_pow(a, b):
    return a ** b

n = int(input("Введите число: "))
b = int(input("Введите степень: "))
print("Число = ", number_value_pow(n,b))

#Task 5

def rn_list():
    return [random.randint(0, 10) for i in range(0, 10)]

def display():
    print(rn_list())
    print("Среднее арифметическое = ", sr_number_value(rn_list()))

def sr_number_value(l):
    s = sum(l)
    leng = len(l)
    return s / leng

rn_list()
display()

#Task 6

def count_numbers():
    m = int(input("Введите количество чисел = "))
    count = 0

    for i in range(m):
        number = float(input(f"Введите число {i + 1} => "))
        if number > 0:
            count += 1

    return count

print(f"Количество чисел больше 0 = {count_numbers()}")

#Task 7

def cubes(n):
    for i in range(1, n + 1):
        print(f"{i} -> {i**3}")

n = int(input("Введите число = "))
cubes(n)

#Task 8

def bits(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b

n = int(input("Введите число = "))

print(bits(n))

#Task 9

def is_prime(n):
    if n <= 1:
        return "Нет"
    if n <= 3:
        return "Да"
    if n % 2 == 0 or n % 3 == 0:
        return "Нет"
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return "Нет"
        i += 6
    return "Да"


n = int(input("Введите число = "))

print("Число простое = ", is_prime(n))

#Task 10

def convert_temperature(value, from_scale, to_scale):

    if from_scale == to_scale:
        return value

    if from_scale == 'C':
        celsius = value
    elif from_scale == 'F':
        celsius = (5/9) * (value - 32)
    elif from_scale == 'K':
        celsius = value - 273.15
    else:
        return "Неизвестная исходная шкала"

    if to_scale == 'C':
        return celsius
    elif to_scale == 'F':
        return (9/5) * celsius + 32
    elif to_scale == 'K':
        return celsius + 273.15
    else:
        return "Неизвестная целевая шкала"


n = int(input("Введите число = "))

print("Число = ", convert_temperature(n, "C", "F"))

#Task 11

def Sum(K):
    digits = str(K)
    unique_digits = set(digits)
    C = len(unique_digits)
    S = sum(int(digit) for digit in digits)
    return C, S


K = int(input("Введите число = "))

C, S = Sum(K)
print(f"K = {K} => C = {C}, S = {S}")


#Task 12

def array(rows, cols):
    return [[0] * cols for _ in range(rows)]

def fill_array(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = random.randint(30, 60)

def max_element(array):
    _max = array[0][0]
    for row in array:
        for value in row:
            if value > _max:
                _max = value
    return _max

def min_element(array):
    _min = array[0][0]
    for row in array:
        for value in row:
            if value < _min:
                _min = value
    return _min

rows = int(input("Введите число строк = "))
cols = int(input("Введите число столбцов = "))

arraylist = array(rows, cols)
fill_array(arraylist)

for row in arraylist:
    print(row)

max_el = max_element(arraylist)
min_el = min_element(arraylist)

print(f"Максимальный элемент = {max_el}")
print(f"Минимальный элемент = {min_el}")
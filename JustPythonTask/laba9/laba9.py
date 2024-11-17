import random

# Task 1

list = [random.randint(1, 10) for i in range(0, 5)]

f = open('task1-1.txt', 'w')

for index in list:
    f.write(f"{index}\n")

f.close()

f = open('task1-1.txt')

sum = 1

for line in f:
    sum *= int(line.strip())

f.close()

r = open('task1-2.txt', 'w')
r.write(f"{sum}\n")
r.close()

# Task 2

with open('task2-1.txt', 'r') as file1:
    lines = file1.readlines()

with open('task2-2.txt', 'w') as file2:
    for line in reversed(lines):
        file2.write(f"{line}\n")

# Task 3

data = [
    "Иванов Иван 21 1 Программист",
    "Петров Петя 30 9 Программист",
    "Сидоров Алексей 25 5 Менеджер",
    "Кузнецова Мария 19 1.5 Программист",
    "Семенов Семен 22 1 Менеджер",
    "Сидорова Алина 32 10 Аналитик",
    "Лебедев Сергей 40 18 Программист",
    "Федоров Федор 27 6 Дизайнер",
    "Илон Маск 53 20 Директор",
    "Гейб Ньюил 62 22 Директор"
]

with open('task3-1.txt', 'w', encoding='utf-8') as f:
    for line in data:
        f.write(line + "\n")

data_result = []

with open('task3-1.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        parts = line.strip().split()
        surname = parts[0]
        name = parts[1]
        age = float(parts[2])
        experience = float(parts[3])

        if experience > 5:
            data_result.append(f"{surname} {experience}")

        if 25 < age < 70:
            data_result.append(f"{surname} {name} {age}")

with open('task3-2.txt.txt', 'w', encoding='utf-8') as f:
    for item in data_result:
        f.write(item + "\n")

# Task 4 (Нужно создать файл task4.txt)

def get_elements(filen, k):
    try:
        with open(filen, 'r') as file:
            
            numbers = [int(line.strip()) for line in file.readlines()]

            if k <= 0 or k > len(numbers):
                return 0
            return numbers[k - 1]
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0

    
file = 'task4.txt' 
listnum = []

for i in range(0, 5):
    listnum.append(int(input("Введите номер => ")))

print(listnum)

for i in listnum:
    result = get_elements(file, i)
    print(f"Элемент с номером {i}: {result}")

# Task 5 (нужно создать файлы для проверки, навзвание в коде)

def lines_in_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        return -1


file_names = ['name_1.txt', 'name_0.txt', 'name_2.txt'] # Можно поменять

for file_name in file_names:
    line_count = lines_in_file(file_name)
    if line_count == -1:
        print(f"{file_name}: {line_count}")
    else:
        print(f"{file_name}: {line_count} строк")

# Task 6 (нужно создать файлы для проверки, навзвание в коде)

def split_file_lines(name, name1, name2, k):
    try:
        with open(name, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

            with open(name1, 'w', encoding='utf-8') as outfile1:
                outfile1.writelines(lines[:k])

            with open(name2, 'w', encoding='utf-8') as outfile2:
                outfile2.writelines(lines[k:])

    except FileNotFoundError:
        print(f"Файл '{name}' не существует.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

k = int(input("Первые k = "))

split_file_lines('Name.txt', 'Name1.txt', 'Name2.txt', k) # Можно поменять

# Task 7 (нужно создать файл для проверки, навзвание в коде)

def shifr_file(file_name, k, encrypt=True):
    # Русский алфавит
    alphabet_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alphabet_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    # Определяем, какую функцию использовать
    if not encrypt:
        k = -k

    # Создаем словарь для замены
    def shift_char(c):
        if c in alphabet_upper:
            index = (alphabet_upper.index(c) + k) % len(alphabet_upper)
            return alphabet_upper[index]
        elif c in alphabet_lower:
            index = (alphabet_lower.index(c) + k) % len(alphabet_lower)
            return alphabet_lower[index]
        else:
            return c  # Не изменяем другие символы

    # Читаем файл
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()

    transformed_content = ''.join(shift_char(c) for c in content)

    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(transformed_content)

k = int(input("Значение для свдига = "))
sh = int(input("Выберите число (0 или 1) = "))
file_name = 'NameSh.txt' # Можно поменять

shifr_file(file_name, k, encrypt=sh)
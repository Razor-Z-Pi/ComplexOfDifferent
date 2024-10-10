#Task 1

n = int(input("Введите число n = "))
result = {x: x * x for x in range(1, n + 1)}
print(result)

#Task 2

n = int(input("Введите число n = "))
result = {x: x * x for x in range(1, n + 1)}
print(result)
sumer = sum(result.values())
print(sumer)

#Task 3

data = {
    "Товар1": 45.50,
    "Товар2": 35,
    "Товар3": 41.30,
    "Товар4": 35,
    "VТовар5": 35
}

unique_values = set()

for key, value in data.items():
    unique_values.add(value)
sorted_unique_values = sorted(unique_values)
print("Уникальные значения:", sorted_unique_values)

#Task 4

data = {
    "Товар1": 45.50,
    "Товар2": 35,
    "Товар3": 41.30,
    "Товар4": 35,
    "VТовар5": 35
}

print(data)

price = sorted(data.items(), key=lambda item: item[1], reverse=True)[:3]


print("3 Дорогих товара:", price)

#Task 5

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Введи число = ")) 
result = factorial_dict = {i: factorial(i) for i in range(1, n + 1)}
print(result)

#Task 6

st = input("Введите строку: ")

words = st.lower().split()

text = {}

for word in words:
    if word in text:
        text[word] += 1
    else:
        text[word] = 1

for word, count in text.items():
    print(f"{word} {count}")

#Task 7

n = int(input("Количество игр = "))

teams_stats = {}
for _ in range(n):
    game_result = input().strip().split(';')
    team1 = game_result[0]
    score1 = int(game_result[1])
    team2 = game_result[2]
    score2 = int(game_result[3])

    if team1 not in teams_stats:
        teams_stats[team1] = {
            'games': 0,
            'wins': 0,
            'draws': 0,
            'losses': 0,
            'points': 0
        }

    if team2 not in teams_stats:
        teams_stats[team2] = {
            'games': 0,
            'wins': 0,
            'draws': 0,
            'losses': 0,
            'points': 0
        }

    teams_stats[team1]['games'] += 1
    teams_stats[team2]['games'] += 1

    if score1 > score2:
        teams_stats[team1]['wins'] += 1
        teams_stats[team1]['points'] += 3
        teams_stats[team2]['losses'] += 1
    elif score1 < score2:
        teams_stats[team2]['wins'] += 1
        teams_stats[team2]['points'] += 3
        teams_stats[team1]['losses'] += 1
    else:
        teams_stats[team1]['draws'] += 1
        teams_stats[team2]['draws'] += 1
        teams_stats[team1]['points'] += 1
        teams_stats[team2]['points'] += 1

print("Команда:Всего-игр Побед Ничья Проигрешей Всего-очков")
for team, stats in teams_stats.items():
    print(f"{team}:{stats['games']} {stats['wins']} {stats['draws']} {stats['losses']} {stats['points']}")
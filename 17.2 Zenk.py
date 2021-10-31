dictionary = {}
for i in range(int(input("Введите количество номеров\n"))):
    val, key = input().split()
    if key in dictionary:
        dictionary[key].append(val)
    else:
        dictionary[key] = [val]

for i in range(int(input("Введите колчество человек для поиска\n"))):
    key = input("Введите имя\n")
    if key in dct:
        print(*dct[key])
    else:
        print("Нет в телефонной книге")
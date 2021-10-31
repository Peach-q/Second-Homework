output = []
for i in range(int(input("Введите количество строк\n"))):
    text = input("Введите строку\n").split(',')
    output.append(text)
for i in range(int(input("Введите колчество значений\n"))):
    pos = input("Значения таблицы:\n").split(',')
    x, y = int(pos[0]), int(pos[1])
    print(output[x][y])
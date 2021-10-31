list_of_sequence = []
n = int(input("Введите число\n"))
for i in range(n):
    b = 0
    for i in range(len(list_of_sequence)):
        if list_of_sequence[i] == list_of_sequence[-1 - i]:
            b += 1
    list_of_sequence.append(b)
del list_of_sequence[-1]
for i in list_of_sequence:
    print(i)
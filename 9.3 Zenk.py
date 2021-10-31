print('Введите количество работников в компании:')
counter = int(input())

workers_list = list()
result_sovpad = 0

for personal in range(counter):
    personal = input("Введите фамилию сотрудника\n")
    workers_list.append(personal)

for people in set(workers_list):
    count = 0

    for surname in workers_list:
        if people in surname:
            count += 1

    if count > 1:
        result_sovpad += count

print(result_sovpad)
print('Введите количество строк для обработки:')
count = int(input())

print('Введите строки для обработки:')
for i in range(count):

    user_message = input()
    if user_message[:4] == '####':
        continue

    if user_message[:2] == '%%':
        print(user_message[2:])
    else:
        print(user_message)

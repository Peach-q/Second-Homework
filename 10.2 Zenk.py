print('Введите шаг смещения:')
сoding_step = int(input())

print('Введите сообщение для шифрования:')
user_message = input()

for i in user_message:
    if ord(i) >= 1101:
        i = chr(ord(i) - (32 - сoding_step))
    else:
        i = chr(ord(i) + сoding_step)
    print('Результат шифрования:',i)
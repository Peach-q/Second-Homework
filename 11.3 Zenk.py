print('Введите слово:')
user_word = input()

print('Введите номер:')
user_index = int(input())

print('Введите символ:')
symbol = input()

if len(user_word) > user_index >= 1:
    if symbol == user_word[user_index-1]:
        print("Да")
    else:
        print("Ошибка")
else:
    print("Ошибка")
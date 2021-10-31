print('Введите слово:')
user_word = input()

print('Введи номер буквы в слове:')
word_index = int(input())

if len(user_word) > word_index >= 1:
    print(user_word[word_index-1])
else:
    print("ОШИБКА")
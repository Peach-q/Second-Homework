print('Введите слово:')

user_word = str(input())
print(user_word)
user_word = int(len(user_word))

while user_word >= 1:
    user_word = user_word[1:-1]
    print(user_word)
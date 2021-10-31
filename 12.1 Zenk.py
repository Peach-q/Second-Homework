print('Введите число слов белого списка:')
counter = int(input())
white_list = []

for i in range(counter):
    print('Введите слово:')
    user_word = input()
    white_list.append(user_word)

print('Введите количество запросов:')
requests_count = int(input())
filter = []

for i in range(requests_count):
    print('Введите слово запроса:')
    word = input()
    
    if word in white_list:
        filter.append(word)
print(*filter)
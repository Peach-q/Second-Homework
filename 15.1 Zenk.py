print('Введите символ, который надо найти:')
user_symbol = input()

print('Введите текст для поиска:')
user_text = input()
list_text = user_text.split()

for i in list_text:
    if user_symbol in i or user_symbol.upper() in i:
        print(i)
print('Введите текст:')

user_text = input()
user_len_text = len(user_text)
counter = 0

for i in range(user_len_text):
    if user_text.count(user_text[i]) > counter:
        counter = user_text.count(user_text[i])
        
print(counter)
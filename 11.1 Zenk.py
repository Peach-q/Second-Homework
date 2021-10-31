print('Введите результаты своих измерений:')
user_results = input()

user_results = user_results.lower()
result = 0
orel = 0


for i in user_results:
    if "о" in i:
        result += 1
        if result > orel:
            max_o = result
    else:
        result = 0

print(orel)
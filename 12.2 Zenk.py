print('Введите строку:')
stroka = input()
n = int(stroka[:4])
total = int(stroka[4:])
error = []
true = 0

for i in range(n):
    stroka = input()
    price = int(stroka[:7])
    amount = int(stroka[8:12])
    cost = int(stroka[13:])

    if price * amount != cost:
        error.append(i + 1)
    true += price * amount
    
print(total - true)
for x in error:
    print(x, end=' ')
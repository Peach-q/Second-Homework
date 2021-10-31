print('Введите число, на которое нужно разделить:')

nature = int(input())
numerator = 1

my_num = []
period = []

while numerator not in my_num:
    
    my_num.append(numerator)
    period.append(10*numerator//nature)

    numerator = 10 * numerator % nature

print(*period[my_num.index(numerator):])
print('Введите количество элементов:')
counter = int(input())

list_of_sort = []

for i in range(counter):
    print('Введите число:')
    user_vvod = int(input())
    list_of_sort.append(user_vvod)

for i in sorted(list_of_sort, reverse=True):
    print(i)
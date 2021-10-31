print('Введите длинну:')
lenght = int(input())

print('Введите ширину:')
breadth = int(input())
list_ = []

for i in range(lenght):
    list_.append(input("Введите псевдофигуру\n"))
list2=[]

for i in list_[::2]:
    list2.append(i[::2])

lenght = lenght // 2
breadth = breadth // 2
for i in list2:
    print(i)
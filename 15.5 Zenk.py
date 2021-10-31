n = int(input("Введите количество строк"))
que = []
for i in range(n):

    item = input().split()
    if "встал" in item[1]:

        que.append(item[0])
    elif item[0] == "Привет,":
        que.insert(que.index(item[1][:-1])+1, item[2])
        
    elif item[1] == "хватит":
        que.remove(item[0][:-1])

print(*que, sep='\n')
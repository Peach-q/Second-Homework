n = int(input("Количество станций\n"))
stations = [[]]

for i in range(n - 1):
    stations.append([int(j) for j in input().split()])

station = input("Введите пункты назначения\n").split()
a, a1 = int(station[0]), int(station[1])

len = stations[max(a, a1)][min(a, a1)]
b = -1

for i in range(n):
    if i != a and i != a1:
        if len > stations[max(a, i)][min(a, i)] + stations[max(i, a1)][min(i, a1)]:
            len = stations[max(i, a1)][min(i, a1)] + stations[max(i, a1)][min(i, a1)]
            b = i

if b != -1:
    print(b)
else:
    print(a)
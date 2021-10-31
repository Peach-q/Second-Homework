from collections import Counter

k = int(input())
surname = []

for i in range(k):
    for j in range(int(input())):
        people = input()
        surname.append(people)

first_list = dict(Counter(surname))
for who in first_list:

    if first_list.get(who) == k:
        print(who)
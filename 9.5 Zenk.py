planned_meals = set()
diff = set()


number_of_dishes = int(input('Введите количество блюд (за смену): '))

for i in range(number_of_dishes):
    planned_meals.add(input())

count = 0
count = int(input('Введите количество блюд: '))
for i in range(count):
    day = int(input('Введите количесвто дней: '))
    for a in range(day):
        diff.add(input())

result = list(planned_meals.difference(diff))

for item in result:
    print(item)

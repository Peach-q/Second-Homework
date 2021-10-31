components_in_fridge = set()
components_meal = set()
products = int(input())


for i in range(products):
    components_in_fridge.add(input())

name_recept_N = int(input())

for i in range(name_recept_N):
    name_recept = input()
    ingredient_eat_M = int(input())
    flag = True

    for j in range(ingredient_eat_M):
        components_meal.add(input())

    for i in components_meal:
        if not i in components_in_fridge:
            flag = False
    if flag:
        print(name_recept)

    components_meal = set()
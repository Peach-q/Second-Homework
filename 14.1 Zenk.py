print('Введите количество пунктов рецепта:')

recept_items = int(input())
items_list = []

for i in range(recept_items):
    my_item = input()
    if "лук" not in my_item:
        items_list.append(my_item)

print(*items_list, sep=', ')
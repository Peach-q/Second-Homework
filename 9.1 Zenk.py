print('Введи число книг в домашней библиотеке: ')
home_library = int(input())

print('Введи число книг, заданных на лето: ')
summer_library = int(input())

home_library_mnozhestvo = set()
summer_library_mnozhestvo = set()

for i in range(home_library):
    book = input()
    home_library_mnozhestvo = home_library_mnozhestvo.add(book)

for i in range(summer_library):
    book = input()
    summer_library_mnozhestvo = summer_library_mnozhestvo.add(book)

    if book in home_library_mnozhestvo:
        print('YES')
    else:
        print('NO')
    
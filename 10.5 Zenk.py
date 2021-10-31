while True:

    print('Введите какое-нибудь слово:')
    user_word = input()

    if user_word[0].lower() != chr(1072):
        break
        print('Вы ввели слово, которое не начинается на букву А')
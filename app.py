import random

from colorama import Fore, Back, Style

words = []
file = open("words.txt", "r", encoding="utf-8")

for i in file:
    words.append(i.replace("\n", ""))
file.close()


guess_word = random.choice(words).upper()
attempts = 6
used_words = []
user_word = ""

# Для теста выводим загаданное слово
print(guess_word)

# до тех пор пока попытки больше нуля
# и слово игрока не равно загаданному слову
# будет выполнятся код в теле цикла
while attempts > 0 and user_word != guess_word:

    user_word = input(Fore.BLACK + "Введите слово из 5 букв").upper().strip()

    # ПРОВЕРКА НА ТО ЧТО СЛОВО КОТОРОЕ ВВЁЛ ПОЛЬЗОВАТЕЛЬ СОСТОИТ ИЗ ПЯТИ БУКВ
    while len(user_word) != 5:
        print(Fore.BLACK + "Неправильный ввод")
        user_word = input("Введите слово из 5 букв").upper()

    # ПРОВЕРКА НА ТО СУЩЕСТВУЕТ ЛИ ТАКОЕ СЛОВО В СЛОВАРЕ РУССКОГО ЯЗЫКА


    user_color_word = ""
    for char in user_word:  # перебираем слово пользователя по буквам

        if char in guess_word and user_word.index(char) == guess_word.index(char):
            user_color_word = user_color_word + Fore.GREEN + char
        elif char in guess_word:
            user_color_word = user_color_word + Fore.YELLOW + char
        else:
            user_color_word = user_color_word + Fore.BLUE + char

    used_words.append(user_color_word)

    for used_color_word in used_words:
        print(used_color_word)

    attempts -= 1
    print(Fore.BLACK + "Осталось попыток:", attempts)

if attempts <= 0:
    print(Fore.RED + "Вы проиграли!")
else:
    print(Fore.GREEN + "Вы угадали!")
input("Нажмите Enter чтобы выйти...")

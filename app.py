from colorama import Fore, Back, Style

guess_word = "КОМАР"
attempts = 6
used_words = []
user_word = ""

while attempts > 0 and user_word != guess_word:

    user_word = input(Fore.BLACK + "Введите слово из 5 букв").upper()

    while len(user_word) != 5:
        print(Fore.BLACK + "Неправильный ввод")
        user_word = input("Введите слово из 5 букв").upper()

    user_color_word = ""
    for char in user_word:

        if char in guess_word and user_word.index(char) == guess_word.index(char):
            user_color_word = user_color_word + Fore.GREEN + char
        elif char in guess_word:
            user_color_word = user_color_word + Fore.YELLOW + char
        else:
            user_color_word = user_color_word + Fore.BLUE + char

    used_words.append(user_color_word)

    for i in used_words:
        print(i)

    attempts -= 1
    print(Fore.BLACK + "Осталось попыток:", attempts)

if attempts <= 0:
    print(Fore.RED + "Вы проиграли!")
else:
    print(Fore.GREEN + "Вы угадали!")

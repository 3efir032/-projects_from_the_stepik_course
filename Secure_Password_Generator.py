"""Программа для генерации паролей по выбранным параметрам пользователя."""

from random import choice
from string import digits, ascii_lowercase, ascii_uppercase, punctuation
import math

DIGITS = digits
LOWERCASE_LETTERS = ascii_lowercase
UPPERCASE_LETTERS = ascii_uppercase
PUNCTUATION = punctuation
AMBIGUOUS_CHARACTERS = 'il1Lo0O'


def pre_setting_passwords():
    """Функция для настройки паролей по выбранным параметрам пользователя."""
    password_setting_algorithm = []
    list_of_questions_for_setting_up_password = [
        'Количество паролей для генерации: ',
        'Длину одного пароля: ',
        '\n(Добавьте +, если да и - если нет)\n\nВключать ли цифры 0123456789? ',
        'Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? ',
        'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? ',
        'Включать ли символы !#$%&*+-=?@^_? ',
        'Исключать ли неоднозначные символы il1Lo0O? '
    ]

    count = 0
    while count < 7:
        input_text = input(list_of_questions_for_setting_up_password[count])
        if count <= 1 and not input_text.isdigit():
            print('Добавьте цифру от 1 до ...')
        elif count >= 2 and (input_text not in ('+', '-')):
            print('Добавьте + или -')
        else:
            password_setting_algorithm.append(input_text)
            count += 1

    return password_setting_algorithm


def setting_the_number_of_passwords_and_character_selection():
    """Функция генерации списка случайных символов по выбранным параметрам пользователя."""
    pre_setting_password = pre_setting_passwords()
    variables = [DIGITS, UPPERCASE_LETTERS, LOWERCASE_LETTERS, PUNCTUATION, AMBIGUOUS_CHARACTERS]
    characters_for_the_password = ''
    for index, passwords in enumerate(pre_setting_password[2:-1]):
        if int(pre_setting_password[1]) > len(variables[index]) and passwords == '+':
            num = math.ceil(int(pre_setting_password[1]) / len(variables[index]))
            characters_for_the_password += variables[index] * num

        elif passwords == '+':
            characters_for_the_password += variables[index]

    if pre_setting_password[-1] == '+':
        characters_for_the_password = characters_for_the_password.translate(
            {ord(i): None for i in AMBIGUOUS_CHARACTERS})

    return characters_for_the_password, int(pre_setting_password[0]), int(pre_setting_password[1])


def generation_passwords():
    """Функция выбирает случайные символы из генерируемого списка случайных символов и
    создает пароли из кол-ва указаной длины и кол-во паролей для генерации."""
    chars, quantity, length = setting_the_number_of_passwords_and_character_selection()
    passwords = []
    for i in range(quantity):
        passwords.append([choice(chars) for _ in range(length)])
    return [''.join(passwords[i]) for i in range(quantity)]


if __name__ == '__main__':
    print(*generation_passwords(), sep='\n')

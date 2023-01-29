import random
from string import *
import math

DIGITS = digits
LOWERCASE_LETTERS = ascii_lowercase
UPPERCASE_LETTERS = ascii_uppercase
PUNCTUATION = punctuation
AMBIGUOUS_CHARACTERS = 'il1Lo0O'


def pre_setting_passwords():
    password_setting_algorithm = []
    list_of_questions_for_setting_up_password = [
        'Количество паролей для генерации: ',
        'Длину одного пароля: ',
        'Включать ли цифры 0123456789? (Добавьте +, если да и - если нет): ',
        'Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (Добавьте +, если да и - если нет): ',
        'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (Добавьте +, если да и - если нет): ',
        'Включать ли символы !#$%&*+-=?@^_? (Добавьте +, если да и - если нет): ',
        'Исключать ли неоднозначные символы il1Lo0O? (Добавьте +, если да и - если нет): '
    ]

    count = 0
    while count < 7:
        input_text = input(list_of_questions_for_setting_up_password[count])
        if count <= 1 and not input_text.isdigit():
            print('Добавьте цифру от 1 до ...')
        elif count >= 2 and (input_text != '+' and input_text != '-'):
            print('Добавьте + или -')
        else:
            password_setting_algorithm.append(input_text)
            count += 1

    return password_setting_algorithm


def setting_the_number_of_passwords_and_character_selection():
    pre_setting_password = pre_setting_passwords()  # [3, 14, '+', '+', '+', '+', '+']
    list_variables = [DIGITS, UPPERCASE_LETTERS, LOWERCASE_LETTERS, PUNCTUATION, AMBIGUOUS_CHARACTERS]
    characters_for_the_password = ''
    for index, passwords in enumerate(pre_setting_password[2:-1]):
        if int(pre_setting_password[1]) > len(list_variables[index]) and passwords == '+':
            num = math.ceil(int(pre_setting_password[1]) / len(list_variables[index]))
            characters_for_the_password += list_variables[index] * num

        elif passwords == '+':
            characters_for_the_password += list_variables[index]

    if pre_setting_password[-1] == '+':
        characters_for_the_password = characters_for_the_password.translate(
            {ord(i): None for i in AMBIGUOUS_CHARACTERS})

    return characters_for_the_password, int(pre_setting_password[0]), int(pre_setting_password[1])


def generation_passwords():
    chars, quantity, length = setting_the_number_of_passwords_and_character_selection()
    passwords = []
    for i in range(quantity):
        passwords.append([random.choice(chars) for _ in range(length)])
    return [''.join(passwords[i]) for i in range(quantity)]


if __name__ == '__main__':
    print(*generation_passwords(), sep='\n')

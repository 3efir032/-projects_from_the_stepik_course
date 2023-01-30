"""Угадайка чисел"""
from random import randrange


def random_number():
    """Функция создает рандомное число от 1 до 100"""
    return randrange(100)


def start_game():
    """Функция запуска игры"""
    number = random_number()
    text = 'В этой игре, Вам необходимо угадать число от 1 до 100\nВведите число от 1 до 100: '
    count = 0
    flag = True
    while flag:

        user_number = input(text)
        if user_number.isdigit() and 1 <= int(user_number) <= 100:

            if number < int(user_number):
                count += 1
                text = 'Ваше число меньше загаданного, попробуйте еще разок\nВведите число от 1 до 100: '
            elif number > int(user_number):
                count += 1
                text = 'Ваше число больше загаданного, попробуйте еще разок\nВведите число от 1 до 100: '
            else:
                count += 1
                print(f'Вы угадали за {count} попыток, поздравляем!')
                if input('Продолжаем играть? да/нет: ').lower() == 'да':
                    number = random_number()
                    text = 'Посмотрим за сколько попыток ты угадаешь\nВведите число от 1 до 100: '
                    count = 0
                else:
                    flag = False

        else:
            print('Добавьте число от 1 до 100.')


if __name__ == '__main__':
    start_game()

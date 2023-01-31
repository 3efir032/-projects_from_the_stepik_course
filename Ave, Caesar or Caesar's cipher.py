"""Аве, Цезарь. Программа зашифровывает сообщения по принципу сдвига.
Каждая буква сдвигает вправо по алфавиту на длину слова в котором она находится."""
from re import findall


def encrypted_message(message):
    """Encrypt a message"""
    text = findall(r'[0-9]+|[A-z]+|,| |"|!|.', message)
    encrypted_text = ''

    for _, word in enumerate(text):
        step = len(word)
        for _, value in enumerate(word):
            if 97 <= ord(value) <= 122 or 65 <= ord(value) <= 90:
                len_alphabet = 26
                if 97 <= ord(value) <= 122:
                    encrypted = (ord(value) - 97 + step) % len_alphabet + 97
                else:
                    encrypted = (ord(value) - 65 + step) % len_alphabet + 65
            elif 1048 <= ord(value) <= 1103:
                len_alphabet = 32
                if ord(value) < 1072:
                    encrypted = (ord(value) - 1040 + step) % len_alphabet + 1040
                else:
                    encrypted = (ord(value) - 1072 + step) % len_alphabet + 1072
            else:
                encrypted = ord(value)
            encrypted_text += chr(encrypted)

    print(encrypted_text)


if __name__ == '__main__':
    encrypted_message(input('Введите сообщение: '))
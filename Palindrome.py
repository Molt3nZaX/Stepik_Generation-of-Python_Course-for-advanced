'''Задача: Палиндром 🌶️

Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение True
если указанный текст является палиндромом и False в противном случае.

Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях
Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы,
а также символы , . ! ? -.
Примечание 3. Следующий программный код:

print(is_palindrome('А роза упала на лапу Азора.'))
print(is_palindrome('Gabler Ruby - burrel bag!'))
print(is_palindrome('BEEGEEK'))
должен выводить:
True
True
False
'''


def is_palindrome(text):
    total = [i for i in text.split()]  # формирование списка из слов введенного предложения(текста)
    invert_string = ''  # обратная строка
    string = ''  # строка
    for word in total:
        for s in range(len(word)):
            if word[s].isalpha():  # проверка каждого элемента. Если это буква, то плюсуем к строке
                string += word[s]
    for i in range(len(string) - 1, -1, -1):  # обратная строка
        invert_string += string[i]
    if invert_string.lower() == string.lower():  # сравнение перевернутой строки и обычной
        return True
    else:
        return False
    pass


# считываем данные
print(is_palindrome('Gabler Ruby - burrel bag!'))

# https://www.codewars.com/kata/5659c6d896bc135c4c00021e/train/python

def next_smaller(n):
    digits = list(str(n))
    length = len(digits)

    # Найти первую позицию, где цифра больше предыдущей (идём справа налево)
    i = length - 2
    while i >= 0 and digits[i] <= digits[i + 1]:
        i -= 1

    # Если нет такой позиции, значит следующее меньшее число не существует
    if i == -1:
        return -1

    # Найти наименьшую цифру слева от позиции i, которая меньше digits[i]
    j = length - 1
    while digits[j] >= digits[i]:
        j -= 1

    # Поменять местами цифры в позициях i и j
    digits[i], digits[j] = digits[j], digits[i]

    # Перевернуть часть цифр после позиции i для получения наибольшего возможного числа
    result = digits[:i + 1] + digits[i + 1:][::-1]

    # Преобразовать результат в число
    result_number = int(''.join(result))

    # Проверить, начинается ли результат с нуля или является ли он меньше исходного числа
    if str(result_number)[0] == '0' or result_number >= n:
        return -1

    return result_number


# Примеры использования
print(next_smaller(21))  # 12
print(next_smaller(531))  # 513
print(next_smaller(2071))  # 2017
print(next_smaller(9))  # -1
print(next_smaller(135))  # -1
print(next_smaller(1027))  # -1

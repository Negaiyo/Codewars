# https://www.codewars.com/kata/55a5bfaa756cfede78000026

def process_value(value):
    if isinstance(value, str):
        return "Error"
    try:
        number = float(value)  # Пробуем преобразовать значение в число
    except (ValueError, TypeError):
        return "Error"  # Если преобразование не удалось, возвращаем ошибку

    result = (number * 50) + 6
    return result
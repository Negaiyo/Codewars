# https://www.codewars.com/kata/56a4872cbb65f3a610000026/train/python

def max_rot(n):
    s = str(n)
    max_num = n
    for i in range(len(s)):
        s = s[:i] + s[i+1:] + s[i]  # Перемещаем i-ю цифру в конец
        max_num = max(max_num, int(s))
    return max_num
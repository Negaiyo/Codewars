# https://www.codewars.com/kata/5a8bcd980025e99381000099

def square_up(n):
    return [j if j <= i else 0 for i in range(1, n+1) for j in range(n, 0, -1)]
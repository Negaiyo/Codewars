# https://www.codewars.com/kata/52ec24228a515e620b0005ef/train/python

def exp_sum(n):
    # Создаем массив для хранения количества разбиений
    dp = [0] * (n + 1)
    dp[0] = 1

    # Заполняем массив dp
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]

    return dp[n]
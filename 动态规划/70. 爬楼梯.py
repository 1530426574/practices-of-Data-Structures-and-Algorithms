# top down
def climbstairs(n):
    if n <= 2:
        return n
    return climbstairs(n - 1) + climbstairs(n - 2)


# bottom up  最好理解
def climbstairs1(n):
    """
    关键在哪呢？？？
    dp[i] 表示啥，到达i这个位置的最优解
    """
    if n == 1:
        return 1

    dp = [0 for _ in range(n)]
    dp[0], dp[1] = 0, 1
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]


# bottom up
def climbstairs2(n):
    if n == 1:
        return 1
    a, b = 1, 2
    for i in range(2, n):
        a, b = b, a + b
    return b


# top down
d = {1: 1, 2: 2}


def climbstairs3(n):
    if n == 1:
        return 1
    if n not in d:
        d[n] = climbstairs3(n - 1) + climbstairs3(n - 2)  # 最后只要计算一个分支
    return d[n]

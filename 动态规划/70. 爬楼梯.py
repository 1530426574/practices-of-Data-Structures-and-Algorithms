#top down
def climbstairs(n):
    if n<=2:
        return n
    return climbstairs(n-1)+climbstairs(n-2)


#bottom up  最好理解
def climbstairs1(n):
    if n ==1:
        return 1

    res = [0 for _ in range(n)]
    res[0],res[1] = 0,1
    for i in range(2,n):
        res[i] = res[i-1]+res[i-2]
    return res[-1]




#bottom up
def climbstairs2(n):
    if n == 1:
        return 1
    a,b = 1,2
    for i in range(2,n):
        a, b = b, a+b
    return b


# top down
d = {1:1,2:2}
def climbstairs3(n):
    if  n== 1:
        return 1
    if n not in d:
        d[n] = climbstairs3(n-1)+climbstairs3(n-2)      #最后只要计算一个分支
    return d[n]




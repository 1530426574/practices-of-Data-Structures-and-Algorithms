# 递归,自动实现循环
# 咋感觉没有理解程序世界里的函数与数学里的函数，
# 没有实现这两者之间的联系呢？？？
# 没有实现无缝对接，可能是一回事
# y = f(*args,**kwargs)=???

# 数学里的函数，是根据定义域（1<x<100)来划分，定义域优先。
# 当1<x<100, f(x) = 3x+1
# 当x>=100, f(x) = 4x+5
# 当x <= 1,   f(x) = f(x-1)+1

# 程序里的函数，是要加点语言逻辑来划分
# def f(x)
# if 1<x<100, return  3x+1
# if x>=100,reurn     4x+5
# if x<= 1,return     f(x+1)+1

def f(n):  #
    """
    递归到底应该如何理解呢？？？
    先一层层进去，然后再一层层出来。
    f(n) = f(n-1) +1
    f(n-1) = f(n-2) +1
    f(n-2) = f(n-3)+1
    f(i-1) = f(i-2) +1
    f(2) = f(1) +1
    f(1) = f(0) +1
    f(0) = 0
    """
    if n == 0:
        return 0
    return f(n - 1) + 1


# 超时，哈哈哈
class Solution1:
    def climbStairs(self, n: int) -> int:
        """
        001 斐波那契数列
        f(1) = 1
        f(2) = 2
        f(n) = f(n-1) + f(n-2), f(n-1) = f(n-2)+f(n-3)???
        通项公式么？

        002 函数的本质：封装，复用，减少冗余代码
        003 递归的本质：自动实现循环
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)  # 自顶向下


# 44ms
class Solution2:
    def climbStairs(self, n: int) -> int:
        """
        f(n) = f(n-1)+f(n-2)
        这种方法很好理解，也更符合我们的思维，用数组存起来。
        按照公式填空就好，明确的知道什么位置，填什么。。。
        """
        if n == 1:
            return 1
        res = [0 for i in range(n)]  # 0 0 0 0 0 0 0 0 0
        res[0], res[1] = 1, 2
        for i in range(2, n):  # 自底向上
            res[i] = res[i - 1] + res[i - 2]
        return res[-1]


# 28ms ,内存都是13.7m
class Solution3:
    def climbStairs(self, n: int) -> int:
        """
        用一个变量就搞定了 。
        f(n) = f(n-1)+f(n-2)
        有点像链表的pre 与cur,然后不断往前移动。
        关键在哪呢？？？
        对于每个节点来说，比如n = i
        f(i) = f(i-1)+f(i-2)
        自底向上的方式，还不是很习惯。

        """
        if n == 1:  # 001 terminator
            return 1
        if n == 2:
            return 2
        a, b = 1, 2
        for i in range(2, n):  # 自底向下
            temp = a + b  # 002 处理当前逻辑层
            a = b  # 003 dril down ,为下一层做好准备
            b = temp
        return temp  # 004 返回当前逻辑层的status


# 36 ms
class Solution4:
    def __init__(self):
        self.d = {1: 1, 2: 2}  # 001 terminator 边界条件

    def climbStairs(self, n: int) -> int:
        """
        001 有就直接返回，没有就创造并添加到字典中，并且保存下来。这种思想用的特别多
        002 递归到底应该如何理解呢？？？
        先一层层进去，然后再一层层出来。
        f(n) = f(n-1) +1
        f(n-1) = f(n-2) +1
        f(n-2) = f(n-3)+1
        f(i-1) = f(i-2) +1
        f(2) = f(1) +1
        f(1) = f(0) +1
        f(0) = 0
        """
        if n not in self.d:  # 自顶向下，然后自底向上。
            self.d[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)  # 002 处理当前层逻辑，003 并dril down
        return self.d[n]  # 004  返回当前层状态（返回啥好呢？？？哈哈哈）


class Solution5:
    def climbStairs4(self, n):
        if n == 1:
            return 1
        dic = [-1 for i in range(n)]
        dic[0], dic[1] = 1, 2
        return self.helper(n - 1, dic)

    def helper(self, n, dic):
        if dic[n] < 0:
            dic[n] = self.helper(n - 1, dic) + self.helper(n - 2, dic)
        return dic[n]

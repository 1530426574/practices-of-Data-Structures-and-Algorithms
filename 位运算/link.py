"""
参考链接
N 皇后位运算代码示例
实战题目 / 课后作业
https://leetcode-cn.com/problems/number-of-1-bits/
https://leetcode-cn.com/problems/power-of-two/
https://leetcode-cn.com/problems/reverse-bits/
https://leetcode-cn.com/problems/n-queens/description/
https://leetcode-cn.com/problems/n-queens-ii/description/
https://leetcode-cn.com/problems/counting-bits/description/
https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/
https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
"""


class Solution:
    def countBits(self, num: int) -> List[int]:
        l = []
        l.append(0)
        for i in range(1, num + 1):
            l.append(l[i & (i - 1)] + 1)

        return l


class Solution:
    def countBits(self, num):
        dp = [0] * (num + 1)
        for pow in range(0, 32):
            start, end = 1 << pow, 1 << (pow + 1)
            if start > num: break

            for j in range(start, min(num + 1, end)):
                dp[j] = dp[j - start] + 1
        return dp


def countBits(self, num: int) -> List[int]:
    counter = [0]
    for i in range(1, num + 1):
        counter.append(counter[i >> 1] + i % 2)
    return counter

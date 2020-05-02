class Solution1:
    def climbStairs(self, n: int) -> int:
        """
        关键在哪呢，到第i层可以分为：
        001 从第i-1层跨一步到
        002 从第i-2层跨2步到
        003 di = di-1 +di-2
        https://leetcode-cn.com/problems/climbing-stairs/
        """
        a = 1
        b = 2
        res = 0
        if n == 0:
            return 0
        elif n == 1:
            return a
        elif n == 2:
            return b
        else:
            for i in range(3, n + 1):
                res = a + b
                a = b
                b = res  # a,b = b,res
            return res

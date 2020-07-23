class Solution1:  # 32ms
    def myPow(self, x: float, n: int) -> float:
        return x ** n


class Solution2:  # 40ms
    myPow = pow


class Solution3:  # 40ms
    def myPow(self, x, n):
        """
        关键在于n为偶数的情况  f(x，n) = f(x*x,n/2)
        """
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)


class Solution4:  # 36ms
    def myPow(self, x, n):
        """
        if n & 1 was same as: if n % 2
        n >> 1 was same as : n //= 2
        """
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow


class Solution5:  # 36ms
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


class Solution6:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


class Solution7:  # 32ms
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:  # 需要提前
            return 1.0 / self.myPow(x, -n)
        if n % 2 == 0:
            y = self.myPow(x, n // 2)
            return y * y
        if n % 2 == 1:
            y = self.myPow(x, n // 2)  # x**11= x * (x**5)**2
            return x * y * y

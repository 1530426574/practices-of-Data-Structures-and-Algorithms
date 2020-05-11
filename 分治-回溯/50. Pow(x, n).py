class Solution1:#32ms
    def myPow(self, x: float, n: int) -> float:
        return x ** n

class Solution2:#40ms
    myPow = pow

class Solution3:
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)

class Solution4:
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
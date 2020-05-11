class Solution5:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
#//取的是结果的最小整数，而/取得是实际的除法结果
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n<0:         #需要提前
            return 1.0 /self.myPow(x,-n)
        if n%2 ==0:
            y = self.myPow(x,n//2)
            return y*y
        if n%2==1:
            y = self.myPow(x,n//2)   #x**11= x * (x**5)**2
            return x*y*y

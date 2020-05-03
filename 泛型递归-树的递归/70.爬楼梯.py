#递归
class Solution1:
    def climbStairs(self, n: int) -> int:
        if  n==1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

class Solution2:
    def climbStairs(self, n: int) -> int:
        if n ==1:
            return 1
        res = [0 for i in range(n)]
        res[0],res[1] = 1,2
        for i in range(2,n):
            res[i] = res[i-1]+res[i-2]
        return res[-1]

class Solution3:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        a,b = 1,2
        for i in range(2,n):
            #a,b=b,a+b
            temp = a+b
            a = b
            b =temp
        return b

class Solution4:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        a,b = 1,2
        for i in range(2,n):
            #a,b=b,a+b
            temp = a+b
            a = b
            b =temp
        return b


class Solution5:
    def climbStairs(self, n: int) -> int:
        d = {1:1,2:2}
        if n not in d:
            d[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        return d[n]
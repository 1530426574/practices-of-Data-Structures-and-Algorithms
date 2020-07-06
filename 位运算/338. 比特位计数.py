from typing import List
class Solution: #0 1 2 3 4 5 6 7
    def countBits(self, num: int) -> List[int]:
        a = [0] * num
        for i in range(1,num):
            a[i] = self.pop_count(i)
        return a

    def pop_count(self,n):
        sum = 0
        while n:
            sum += 1
            n &= (n-1)
        return sum

class Solution1: #0 1 2 3 4 5 6 7
    def countBits(self, num: int) -> List[int]:
        """
        关键在于：
    一个数乘以2之后，只是在位数最右边添加一个0,1个位数并没有改变，
    一个数乘以2然后+1 后，先在最右边添加一个0，然后把0变为1，所以1的个数加+1
        count_bits[2n] = count_bits[n]
        count_bits[2n+1]  = count_bits[n] + 1

        """

        counter = [0] * (num + 1)
        for i in range(1, num + 1):
            counter[i] = counter[i >> 1] + i % 2
        return counter

class Solution2:
    def countBits(self, num):
        counters = [0] * (num + 1)
        for i in range(1, num + 1):
            counters[i] = counters[i & (i-1)] +1
        return counters

# class Solution:
#     def countBits(self, num):
#         dp = [0] * (num + 1)
#         for pow in range(0, 32):
#             start, end = 1<<pow, 1<<(pow + 1)
#             if start > num: break
#
#             for j in range(start, min(num+1,end)):
#                 dp[j] = dp[j-start] + 1
#         return dp


# def countBits(self, num: int) -> List[int]:
    # counter = [0]
    # for i in range(1, num+1):
    #     counter.append(counter[i >> 1] + i % 2)
    # return counter
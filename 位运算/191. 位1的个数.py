class Solution:#36ms
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")   #查找字符串

class Solution1: #比较好理解
    def hammingWeight(self, n: int) -> int:
        bits = 0
        mask = 1
        for  i in range(32):
            if n & mask != 0:
                bits += 1
            mask = mask  << 1    # n的每位与mask进行比较，这里对mask进行左移。
        return bits

class Solution2: #1ms
    def hammingWeight(self, n: int) -> int:
        sum = 0
        while n != 0:
            sum += 1
            n  = n & (n-1)     #清零 最低位1，得到一个新的数，然后继续清零最低位，依次，直到全部清掉，每次清count，最后统计
        return sum


class Solution3: # 偏移n
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n :
            count += n & 1  #比较n的最后一位，是1就 + 1，是0就 + 0一直遍历
            n  = n >> 1     #右移
        return count

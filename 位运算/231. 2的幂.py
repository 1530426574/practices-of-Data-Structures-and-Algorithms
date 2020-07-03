# 在补码表示法中，−x=~x+1。换句话说，要计算 -x，则要将 x 所有位取反再加 1。
#https://leetcode-cn.com/problems/power-of-two/solution/2de-mi-by-leetcode/
# x & (-x)可以获取到二进制中最右边的1，且其它位设置为0。
# 在二进制表示中，数字 n中最低位的 1 总是对应 n - 1 中的 0 。
# 因此，将 n 和 n - 1 与运算总是能把 n 中最低位的 1 变成 0 ，
# 并保持其他位不变。
# 111 1 0000
# 111 0 1111
#若 x 为 2 的幂，则它的二进制表示中只包含一个 1
# 首先讨论为什么 x & (x - 1) 可以将最右边的 1 设置为 0。
#
# (x - 1) 代表了将 x 最右边的 1 设置为 0，并且将较低位设置为 1。
#
# 再使用与运算：则 x 最右边的 1 和就会被设置为 0，因为 1 & 0 = 0。

class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:    # 关键还是在与2的幂次方，二进制表示只有1个 1
        return n&(-n) == n if n else False     # n&(-n)获取最低位为1的值      关键在于按位取反，得到最低位1的值
class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        return n &(n-1) == 0 if n else False   # n(n-1)清除最低位1  关键在于最低位为1的位置已经由 1 -> 0

#00001000
#11110111
#11111000
#00001000
#00010000
#00001111
#0000000
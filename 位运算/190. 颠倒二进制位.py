class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31

        while n:
            ret = ret + (n & 1) << 31   #依次取位，并放入合适的位置，先是
            n = n >> 1
            power -= 1
        return ret

class Solution1:
    def reverseBits(self, n: int) -> int:
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n



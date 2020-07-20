# 用位运算的技巧就行了。。。
#
# 大写变小写、小写变大写 : 字符 ^= 32;
# chr(ord('A')^32)
# 'a'
#
# 大写变小写、小写变小写 : 字符 |= 32;
#
# 小写变大写、大写变大写 : 字符 &= -33;
# chr(ord('A')&-33)
# 'A'
# chr(ord('a')&-33)
# 'A'
# o 懂了，ASCII码表中大写的A是65，小写的a是97，它们的差是32
#
# 65 | 32 转为二进制（按8位来算）可以得到
# 0100 0001 | 0010 0000 = 0110 0001 = 97 = a
#0100 0001
#0010 0000
#0110 0001
#0110 0001
#0010 0000
#0110 0001

class Solution:

    def to_lower_case(self,str:str):
        ret = ''
        # for char in s:
        #     char = chr(ord(char)| 32)
        #     ret += char
        ret = ''.join([chr(ord(char) | 32 ) for char in str])
        return ret

class Solution1(object):
    def toLowerCase(self, str):
            return ''.join([chr(ord(c) ^ 32) if (c < 'a') and c.isalpha() else c for c in str])

class Solution3:
    def toLowerCase(self, str_1: str) -> str:
        S1 = ""
        for s in str_1:
            if s >= 'A' and s <= 'Z':
                s = chr(ord(s) + 32)
            else:
                pass
            S1 += s
        return S1

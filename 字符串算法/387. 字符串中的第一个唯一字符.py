"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

示例：
s = "leetcode"
返回 0

s = "loveleetcode"
返回 2

"""
from collections import Counter
count = Counter("leetcode")
print(count)
#Counter({'e': 3, 'l': 1, 't': 1, 'c': 1, 'o': 1, 'd': 1})
print(count['e'])
class Solution:

    def first_uniq_char(self, s: str):

        #build hash map :
        #charracter ans how often it happend

        count = Counter(s)
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        return -1


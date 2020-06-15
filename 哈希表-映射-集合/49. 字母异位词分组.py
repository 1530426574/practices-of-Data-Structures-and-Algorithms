from collections import defaultdict
import string


class Solution1:
    def groupAnagrams(self, strs: list):
        """
        关键在哪呢？ 如果是异位词，排序后他们是一米一样的 ，就可以作为
        key
        将排序后的字符串，作为key
       [ abc  cab bbc bcb cbb cba ]
        ('a','b','c')->   [abc  cab  cba]
        ('b','b','c')->   [bbc  cbb  bcb ]
        :param strs:
        :return:
        """
        d = defaultdict(list)
        for s in strs:
            d[tuple(sorted(s))].append(s)
        return d.values()

print(tuple(sorted('abc')))
print(tuple(sorted('bac')))

class Solution2:
    def groupAnagrams(self, strs: list):
        """
        关键在哪呢？ 如果是异位词，那么他们在26位字符计数是一米一一样的。
        #抓住那些不变的。
        abc  cab bbc bcb cbb cba
        (1,1,1,0,0,0.....)->abc bac cba
        (0,2,1,0,0,0,0,0) -> bbc bcb cbb
        """
        d = defaultdict(list)
        for s in strs:
            d[self.counter(s)].append(s)
        return d.values()

    # count = [0] * 26  统计字母出现的频率
    # for i in s: #abcdeab  k
    #    count[ord(i) - ord('a')] += 1
    def counter(self, s: str):   # 26 * k
        return (s.count(i) for i in string.ascii_lowercase)

    def counter2(self, s: str):   # k
        count = 26 * [0]
        for i in s:      #abcb
            count[ord(i) - ord('a')] += 1  #找到各自的位置。
        return count

#[0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#填空

print(ord('a'))
print(ord('b'))
s = 'bbc'

a = []
for i in 'abcdefghijklmnopqrstuvwxyz':
    print(i)
    a.append(s.count(i))
print(a)







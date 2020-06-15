import string
# 字母异位词指字母相同，但排列不同的字符串。
# 异位词，相当于把同一串字符串，重新排列组合。有序排列只是其中一种。关键在于总个数，各字母出现的个数是否一致。
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        关键在哪呢？？？                个数是否相等
        s  aaa
        遍历26个字母，各个字符串所包含的个数是否相等呢？
        s  aaa
        t  aaaa
        此方法也不用考虑两字符串是否长度一致了。
        如果同一个字母一个字符串有a个，另外一个有b个，判断a ==b
        执行用时 :36 ms, 在所有 Python3 提交中击败了98.53%的用户
        """
        return all((s.count(i) == t.count(i) for i in string.ascii_lowercase)) #判断 'a' 出现分次数是否相等。
        # a = (s.count(i)==t.count(i) for i in string.ascii_lowercase)
        # a =[]
        # for c in ascii_lowercase:
        #     a.append(s.count(c)==t.count(c)) #遍历26*n
        # return all(a)
from collections import defaultdict


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        关键在哪呢？？？ 关键在于字母的个数是否相等。
        如果value值小于0，意味着什么呢？说明了什么么？什么情况下会出现value<0？
        000 大前提 长度一致。排序。。。。
        001 某一字母s不存在，但t 存在
        002 某一字母s存在，个数为x,t也存在，个数为y,但y>x,这种情况意味着，有一种字母在s中的个数多余在t中的个数
        """

        if len(s) != len(t):
            return False
        d = defaultdict(int)
        for c in s:  # aaaa
            d[c] += 1
        for c in t:  # aaaaaab
            d[c] -= 1
            if d[c] < 0:  # 这一步意味着什么呢？多了be
                return False
        return True


class Solution3:
    def isAnagram3(self, s, t):
        """
        排序
        :param s:
        :param t:
        :return:
        """
        return sorted(s) == sorted(t)

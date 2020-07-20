from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        g=[2, 3], s=[1, 2, 3]
        g=[2, 3, 5,6 ], s=[2, 3,4,5,6]
        g=[4，7], s=[2,3,4,5,6]
        关键在哪呢？？？
        想像情景？？？
        先用小饼干满足贪心指数小的，如果饼干不能满足贪心最小的，就放弃。
        """
        g.sort()
        s.sort()
        i = 0
        j = 0
        res = 0
        while i < len(g) and j < len(s):  # 同时遍历但不一定同步遍孩子和饼干
            if s[j] >= g[i]:  # 如果当前饼干能够满足当前孩子胃口，则判断下个饼干和下个孩子
                j += 1
                i += 1
                res += 1
            else:  # 如果当前饼干不能满足当前孩子的胃口，就开始遍历下一个饼干
                j += 1
        return res

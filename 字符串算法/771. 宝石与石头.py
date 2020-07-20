class Solution:
    def num_jewe_is_in_stones(self, J, S):
        return sum( s in J for s in S)


class Solution1:
    def num_jewe_is_in_stones(self, J, S):
        Jset = set(J)
        return sum(s in Jset for s in S )

"""
 给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。

J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。

输入: J = "aA", S = "aAAbbbb"
输出: 3
示例 2:

输入: J = "z", S = "ZZ"
输出: 0
"""
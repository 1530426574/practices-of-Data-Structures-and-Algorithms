"""
给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。

如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
 

示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"
 

提示：

该字符串只包含小写英文字母。
给定字符串的长度和 k 在 [1, 10000] 范围内。
通过次数18,136提交次数33,426

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-string-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def reverseStr(self, s, k):
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)

class Solution1:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        return s[:k][::-1] + s[k:2*k] + self.reverseStr(s[2*k:], k) if s else ""

class Solution2:
    def reverseStr(self, s, k):
        """
             # Divide s into an array of substrings length k
             # Reverse every other substring, beginning with s[0]
             # Join array of substrings into one string and return
        """
        s = [s[i:i+k] for i in range(0, len(s), k)]
        for i in range(0, len(s), 2):
            s[i] = s[i][::-1]
        return
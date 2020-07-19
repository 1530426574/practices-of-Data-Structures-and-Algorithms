def lengthOfLastWord(self, s):
    ls = len(s)
    # slow and fast pointers
    slow = -1
    # iterate over trailing spaces
    while slow >= -ls and s[slow] == ' ':
        slow-=1
    fast = slow
    # iterate over last word
    while fast >= -ls and s[fast] != ' ':
        fast-=1
    return slow - fast

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        wordlist = s.split()
        if wordlist:
            return len(wordlist[-1])
        return 0

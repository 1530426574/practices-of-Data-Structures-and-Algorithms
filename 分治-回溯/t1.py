"""
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution1:
    def letterCombinations(self, digits):
        if not digits:
            return []
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        self.dfs(digits, dic, 0, "", res)
        return res

    def dfs(self, digits, dic, index, path, res):
        if len(path) == len(digits):
            res.append(path)
            return
        for i in range(index, len(digits)):
            for j in dic[digits[i]]:
                self.dfs(digits, dic, i + 1, path + j, res)


def leetter(digits):
    if not digits:
        return []
    dic = {"2": 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    length = len(digits)

    def traceback(path, index):
        if len(path) == length:
            res.append(path[:])
            return
        for i in dic[str(digits[index])]:
            traceback(path + i, index + 1)

    path = ""
    res = []
    traceback(path, 0)
    return res


def letterCombinations(self, digits: str) -> list:
    if not digits:
        return []
    d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    def traceback(index, path):
        if len(path) == len(digits):
            res.append(path)
            return  # 为啥有return，要在这里结束？？？？？
        for c in d[digits[index]]:  # index的作用是为了确定新的选择列表。
            path += c
            traceback(index + 1, path)
            path = path[0:-1]

    res = []
    path = ""
    traceback(0, path)
    return res

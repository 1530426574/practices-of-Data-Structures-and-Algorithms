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

class Solution:#28ms
    def letterCombinations(self, digits: str) -> list:
        if not digits:
            return []
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def traceback(index, path):
            if len(path) == len(digits):
                res.append(path)
                return                   #为啥有return，要在这里结束？？？？？
            for c in d[digits[index]]:   #index的作用是为了确定新的选择列表。
                path+=c
                traceback(index+1,path)
                path=path[0:-1]

        res = []
        path = ""
        traceback(0, path)
        return res
class Solution2:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits: return []
        digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
                     '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = ['']
        for idx in range(len(digits)):
            result = [prev + l for prev in result for l in digit_map[digits[idx]]]
        return result


class Solution3(object):#队列思想
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		if not digits:
			return []
		# 一个映射表，第二个位置是"abc“,第三个位置是"def"。。。
		# 这里也可以用map，用数组可以更节省点内存
		d = [" ","*","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
		# 先往队列中加入一个空字符
		res = [""]
		for i in digits:
			size = len(res)
			# 由当前遍历到的字符，取字典表中查找对应的字符串
			letters = d[ord(i)-48]
			# 计算出队列长度后，将队列中的每个元素挨个拿出来
			for _ in range(size):
				# 每次都从队列中拿出第一个元素
				tmp = res.pop(0)
				# 然后跟"def"这样的字符串拼接，并再次放到队列中
				for j in letters:
					res.append(tmp+j)
		return res


class Solution4:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])

        output = []
        if digits:
            backtrack("", digits)
        return output


class Solution6:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
                return   #可加可不加，因为 if else
            # if there are still digits to check
            else:
                # iterate over all letters which map
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])

        output = []
        if digits:
            backtrack("", digits)
        return output

def leetter(digits):
        if not digits:
            return []
        dic = {"2": 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        length = len(digits)

        def traceback(path, index):
            if len(path) == length:
                res.append(path)
                return
            for i in dic[str(digits[index])]:
                traceback(path + i, index + 1)

        path = ""
        res = []
        traceback(path, 0)
        return res

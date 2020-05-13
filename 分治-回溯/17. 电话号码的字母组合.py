class Solution1:
    def letterCombinations(self, digits: str) -> list:
        if not digits:
            return []
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def traceback(index,path):
            if len(path)==len(digits):
                res.append(path)
            for i in range(index,len(digits[index])):
                for j in d[digits[i]]:
                    path+=j
                    traceback(i+1,path)
                    # path=path[:]
        res = []
        path=""
        traceback(0,path)
        return res

class Solution:#44ms
    def letterCombinations(self, digits: str) -> list:
        if not digits:
            return []
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def traceback(index, path):
            if len(path) == len(digits):
                res.append(path)
                return                   #为啥有return，要在这里结束？？？？？
            for c in d[digits[index]]:
                path+=c
                traceback(index+1,path)
                path=path[0:-1]

        res = []
        path = ""
        traceback(0, path)
        return res
class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
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


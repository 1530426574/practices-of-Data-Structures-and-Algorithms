"""
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def generateParenthesis(self, n: int) -> list:
        ans = []
        l = ['(',')']

        def generate(path, l):             #组合 000000 6个位置填空['(',')']
            if len(path) == 2*n:
                if valid(path):
                    ans.append(''.join(path))
            for i in l:
                path.append(i)
                generate(path, l)   #当前选择列表不变。
                path.pop()

        def valid(path):                   #判断是否有效 以‘(’开头，并且'('的数量=")"的数量
            bal = 0
            for s in path:
                if s == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0
        generate([],l)
        return ans



class Solution1:
    def generateParenthesis(self, n: int) -> list:
        def generate(A):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                for i in ('(',")"):
                    A.append(i)
                    generate(A)
                    A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0

        ans = []
        generate([])
        return ans
ans = []
l = ['(', ')']


def generate(s, l):
    if len(s) == 6:
        print('++++',s)
        ans.append(''.join(s))
        print(ans)
        return
    for i in l:
        s.append(i)
        generate(s, l)
        s.pop()

# print(generate([],l))
# print(ans)

def valid(s):
    bal = 0
    for c in s:
        if c =='(':
            bal+=1
        else:
            bal-=1
        if bal<0:
            return False
    return bal == 0

print(valid(')))((('))


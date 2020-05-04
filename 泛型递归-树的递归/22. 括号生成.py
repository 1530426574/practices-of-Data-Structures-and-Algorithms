class Solution:
    def generateParenthesis(self, n: int) -> list:
        ans = []
        l = ['(',')']
        def generate(s,l):
            if len(s) == 2*n:
                if valid(s):
                    ans.append(''.join(s))
            for i in l:
                s.append(i)
                generate(s,l)
                s.pop()

        def valid(s):
            bal = 0
            for c in s:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0

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


res = []


def generate(s, l, n):
    if len(s) == 6:
        print('++++', s)
        ans.append(''.join(s))
        print(ans)
        return
    for i in l:
        s.append(i)
        generate(s, l)
        s.pop()


l = ('(', ')')
path = ''


def generate1(path, l, n):
    if len(path) == 2 * n:
        res.append(path)
        return
    for i in l:
        generate(path + i, l)


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


def valid1(s):
    bal = 0
    for char in s:
        if char == '(':
            bal += 1
        else:
            bal -= 1
        if bal < 0:
            return False
    return bal == 0

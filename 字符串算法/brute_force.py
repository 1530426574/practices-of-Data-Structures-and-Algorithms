# Python
def forceSearch(txt, pat):
    n, m = len(txt), len(pat)
    for i in range(n - m + 1):
        for j in range(m):
            if txt[i + j] != pat[j]:
                break
        if j == m:
            return i
    return -1


# abcdefg
# HERE IS A SIMPLE EXAMPLE
#                        EXAMPLE
def force_search(txt, pat):
    n, m = len(txt), len(pat)
    for i in range(n - m + 1):
        for j in range(m):
            if txt[i + j] != pat[j]:
                break
        if j == m:
            return i
    return -1

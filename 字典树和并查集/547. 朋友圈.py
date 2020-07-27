class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N, visited, res = len(M), set(), 0
        for i in range(N):
            if i not in visited:
                queue = [i]
                while queue:
                    p = queue.pop(0)
                    if p not in visited:
                        visited.add(p)
                        queue += [k for k, num in enumerate(M[p]) if num and k not in visited]
                res += 1
        return res




class Solution:

    def find_circle_num(self, M):
        length, visited, res = len(M), set(), 0
        for i in range(length):
            if i not in visited:
                queue = [i]
                while queue:
                    p = queue.pop(0)
                    if i not in visited:
                        visited.add(i)
                        queue += [j for j, num in enumerate(M[p]) if num and j not in visited]
                res += 1
        return res












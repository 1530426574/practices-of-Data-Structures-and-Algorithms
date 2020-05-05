from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < 0 or k <=0 or k>n:
            return []
        res = []
        self.dfs(1,k,n,[])


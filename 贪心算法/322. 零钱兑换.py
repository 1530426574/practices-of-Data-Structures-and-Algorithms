from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        输入: coins = [1, 2, 5], amount = 11
        输出: 3
        解释: 11 = 5 + 5 + 1

        """

        if amount == 0:
            return 0
        value1 = [0]
        value2 = []
        nc = 0
        visited = [False] * (amount + 1)
        visited[0] = True
        while value1:
            nc += 1
            for v in value1:
                for coin in coins:          # 1 2 5
                    newval = v + coin       # 0 + 1
                    if newval == amount:
                        return nc
                    elif newval > amount:
                        continue
                    elif not visited[newval]:
                        visited[newval] = True
                        value2.append(newval)
            value1, value2 = value2, []
        return -1

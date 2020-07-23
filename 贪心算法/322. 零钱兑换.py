from typing import List
from collections import deque

"""
这个问题其实有点像「组合问题」，具体在纸上画一下，就知道这其实是一个在「图」上的「最短路径问题」。
很显然，「广度优先遍历」是求这个问题的算法，广度优先遍历借助「队列」实现。

因为是「图」，有回路，所以要设计一个 visited 数组。
注意：在添加到队列的时候，就得将 visited 数组对应的值设置为 true，否则可能会出现同一个元素多次入队的情况。
广度优先遍历的代码是很常见的，大家多写几遍也就会了
"""


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
            for v in value1:  # 遍历这一层的每个节点，然后对每个节点选择不同面值的硬币进行判断。
                for coin in coins:  # 1 2 5
                    newval = v + coin  # 0 + 1
                    if newval == amount:
                        return nc
                    elif newval > amount:
                        continue
                    elif not visited[newval]:
                        visited[newval] = True
                        value2.append(newval)  # 收集每一层走过的节点
            value1, value2 = value2, []  # 最后让value1记录这一层节点对象
        return -1

    # def  coinChange1(self, coins: List[int], amount: int) -> int:
    #     if amount == 0 :
    #         return 0
    #     queue = deque([0])
    #     count = 0
    #     visited = [False]*(amount+1)
    #     visited[0]=True
    #     while queue:
    #         val = deque.popleft()
    #         for  coin in coins:
    #             newval = val+coin
    #             if newval == amount:
    #                 return count
    #             elif newval >amount:
    #                 continue
    #             elif not visited[newval]:
    #                 visited[newval]=True
    #                 deque.append(newval)

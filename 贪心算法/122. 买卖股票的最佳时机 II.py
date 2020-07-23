from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0: profit += tmp
        return profit


"""
每相邻两天分别进行买卖，看差值
1 2 3 4 5
连续上涨时，5-1 = (2-1) +(3-2)+(4-3)+(5-4)       2-1 3-2 4-3 5-4  买卖
4 3 2 1  
连续下降时： 3-4 2-3 1-2  <0      啥也不做
 
7 1 5 3 6 4  1-7 5-1 3-5 6-3  4-6 
"""

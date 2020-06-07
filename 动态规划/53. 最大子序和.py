#动态规划会保存以前的运算结果，
#并根据以前的结果对当前进行选择，
# 有回退功能。
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        关键在哪呢？？？   用 f(i) 代表以第 i 个数nums[i]结尾的   ***连续子数组的最大和***
以 nums[i]结尾的连续子数组的最大值
        以第 i 个数结尾的 连续子数组(要么是自己，要么包含 以第 i-1 个数结尾的 连续子数组) 且和最大（目的是的d[i]位置和最大）

        dp[i]表示啥，表示以nums[i]结尾的 连续子数组 的最优解(最大和)。
        连续子数组的最大和

        f(i)   以第i个数结尾的      连续子数组 的最大和
        f(i-1) 以第i-1个数结尾的    连续子数组 的最大和

        """

        length = len(nums)
        if length == 0:
            return 0

        dp = [0 for _ in range(length)]

        dp[0] = nums[0]
        for i in range(1,length):
            if dp[i-1] >=0 :
                dp[i] = dp[i-1]+nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)




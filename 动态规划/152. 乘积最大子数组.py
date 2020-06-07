from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        d[i] -> 以nums[i]结尾的 连续子数组 乘积的最大值
        """
        if not nums:
            return
        dmax = [0] * len(nums)
        dmin = [0] * len(nums)
        dmax[0] = dmin[0] = nums[0]
        for i in range(1, len(nums)):
            dmax[i] = max(dmax[i - 1] * nums[i], dmin[i - 1] * nums[i], nums[i])
            dmin[i] = min(dmax[i - 1] * nums[i], dmin[i - 1] * nums[i], nums[i])
        return max(dmax)




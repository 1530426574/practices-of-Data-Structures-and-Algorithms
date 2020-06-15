class Solution:
    def twoSum(self, nums: list, target: int):
        """
        关键在哪呢？本质是什么呢？nums[j] = target -nums[i]
        001 本质判断两个数是否相等，a = b 或者字典找索引
        002 把其中一个数和对应的下标用字典存起来
        003 等找到相等的数，我也能通过索引找到其下标。
        004 一边遍历存储，一边查找比较。
        https://leetcode-cn.com/problems/two-sum/
        [1,3,4,5]
        """
        length = len(nums)
        if length <= 1:
            return False
        d = {}
        for i in range(10):
            if nums[i] not in d:  # O(1)nums[i] ！=target-nums[j]
                d[target - nums[i]] = i
            else:# 等价于nums[i] =target-nums[j]
                return [i, d[nums[i]]]


class Solution3:
    def twoSum(self, nums: list, target: int) -> list:
        length = len(nums)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]


print(Solution().twoSum([2, 7, 11, 15], 9))

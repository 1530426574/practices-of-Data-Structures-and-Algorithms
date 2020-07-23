class Solution:  # 60ms 在所有 Python3 提交中击败了57.63%的用户
    def permuteUnique(self, nums: list) -> list:
        def traceback(nums, path):
            if not nums:
                res.append(path[:])
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:  # 遇到重复的就跳过。
                    continue
                path.append(nums[i])  # nums[i] ,not i
                traceback(nums[:i] + nums[i + 1:], path)
                path.pop()

        res = []
        path = []
        nums.sort()  # [1,1,1,2,3,4,]
        traceback(nums, path)
        return res

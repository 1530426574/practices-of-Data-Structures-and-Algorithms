from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, setp = 0, 0, 0
        for i in range(n - 1):
            if i <= maxPos:
                maxPos = max(maxPos, i + nums[i])
                if i == end:  # 在可选范围内，都会走一步的，并确定下一个可选范围
                    end = maxPos
                    setp += 1
        return setp


from typing import List


class Solution11:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, setp, res, imax = 0, 0, 0, [], 0
        for i in range(n - 1):
            if i <= maxPos:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    setp += 1
        return setp


class Solution1:
    def jump(self, nums: List[int]) -> List[int]:
        length, rightmost, res = len(nums), 0, []
        for i in range(length - 1):
            l = i + nums[i]
            if i <= rightmost:  # 先判断当前位置是否可达到
                rightmost = max(rightmost, l)  # 若是能够到达，最远到达的位置
                if l >= (length - 1):  # 最远到达的位置是不是最后一个位置
                    res.append(i + 1)
                    # 若是就返回True
        return res


s = Solution()
print(s.jump([2, 1, 1, 0, 4]))


# 例如，对于数组 [2,3,1,2,4,2,3]

class Solution2(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = end = step = 0
        while end < len(nums) - 1:
            start, end = end + 1, max([i + nums[i] for i in range(start, end + 1)])
            step += 1
        return step


class Solution3:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step

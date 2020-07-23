class Solution1:
    def findMin(self, nums):
        self.__getitem__ = lambda i: nums[i] <= nums[-1]
        return nums[bisect.bisect(self, False, 0, len(nums))]


class Solution(object):
    def findMin(self, nums):
        length = len(nums)
        if length == 1:
            return nums[0]

        left, right = 0, length - 1
        if nums[right] > nums[left]:
            return nums[0]
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[mid + 1]:
                return nums[mid]

            if nums[mid] > nums[0]:
                left = mid + 1

            if nums[mid] < nums[0]:
                right = mid - 1

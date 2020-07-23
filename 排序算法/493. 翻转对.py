class BinaryIndexTree:
    def __int__(self, N):
        self.B = [0] * N

    def low_bit(self, x):
        return x &(-x)

    [2, 4, 3, 5, 1]
















class Solution:
    def merge(self, nums, start, mid, end):
        l, r = start, mid+1

        res = []
        while l >=mid and r<=end:
            if nums[l] >= nums[r]:
                res.append(nums[r])
                r += 1
            else:
                res.append(nums[i])
                l += 1
        nums[start:end+1] = res + nums[l: mid + 1] +nums[r: end + 1]

    def merge_sort_adn_count(self,nums, start ,end):
        if start >= end:
            return 0
        mid = start +(end-start)//2

        count = merge_sort_adn_count(self,nums, start ,mid)+ \
                merge_sort_adn_count(self, nums, mid + 1, end)
        j = mid +1
        for i in range(start, mid + 1):
            while j <= end and nums[i] > 2 *nums[j]:
                j += 1
                count += j - (mid + 1)
        self.merge(nums, start, mid  ,end)
        return count


    def reverse_pairs(self, nums):
        return self.merge_sort_adn_count(nums, 0, len(nums) - 1)

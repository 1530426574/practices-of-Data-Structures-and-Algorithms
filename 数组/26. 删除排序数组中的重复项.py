class Solution:
    def removeDuplicates(self, nums: list) -> int:
        # 1 2 3 4 5 5 5 5 6
        # 1 1 1 1 1 1 2 2 2 2 2 3 4 5
        """
        关键在哪呢？
        把不同的从a[1]开始依次按顺序排到前面？位置排好的跳过 用一个变量（指针）i 记录已经排好位置的。
        001 若是遇到相等的怎么办，不相等的怎么办？
        002 遇到相等的continue
        003 遇到不相等的，在赋值给a[1]，然后依次累加，a[2]
        004 用一个指针（变量）记录
        """
        length = len(nums)
        j = 0
        for i in range(1, length):
            if nums[i] == nums[j]:
                continue
            j += 1
            nums[j] = nums[i]
            # a[j],a[i] = a[i],a[j]
        return j + 1

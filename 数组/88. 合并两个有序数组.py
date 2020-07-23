class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
            本质和关键在哪呢？？？ 本质是如何按照要求摆放一个个int对象。
        001 本质是最后我的数据要如何存放呢？ 本质就是填空，填入一个个int对象，填入要求尾部为最大的那个数。
        002 最后一位该填哪个对象
        003 关键在最后一位填什么，填完之后，又从剩下的数据找到最大值，填入倒数第二个位置
        https://leetcode-cn.com/problems/merge-sorted-array/solution/he-bing-liang-ge-you-xu-shu-zu-by-leetcode/
        """
        r1 = m - 1
        r2 = n - 1
        r = m + n - 1
        while r1 >= 0 and r2 >= 0:
            # 4 5 6
            # 0 1 2
            if nums1[r1] < nums2[r2]:
                nums1[r] = nums2[r2]
                r2 -= 1
                r -= 1
            else:
                nums1[r] = nums1[r1]
                r1 -= 1
                r -= 1
        if r2 < 0:
            pass
        if r1 < 0:
            nums1[:r2 + 1] = nums2[:r2 + 1]
        return nums1


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # Make a copy of nums1.
        nums1_copy = nums1[:m]
        nums1[:] = []

        # Two get pointers for nums1_copy and nums2.
        p1 = 0
        p2 = 0

        # Compare elements from nums1_copy and nums2
        # and add the smallest one into nums1.
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        # if there are still elements to add
        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]


 # i = j = k = 0
#
#         # Copy data to temp arrays L[] and R[]
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
#
#         # Checking if any element was left
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
#
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1
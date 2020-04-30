class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        本质和关键在哪呢？？？ 本质是如何按照要求摆放一个个int对象。
        001 本质是最后我的数据要如何存放呢？ 本质就是填空，填入一个个int对象，填入要求尾部为最大的那个数。
        002 最后一位该填哪个对象
        003 关键在最后一位填什么，填完之后，又从剩下的数据找到最大值，填入倒数第二个位置

        https://leetcode-cn.com/problems/merge-sorted-array/solution/he-bing-liang-ge-you-xu-shu-zu-by-leetcode/
        """
        p1 = m-1
        p2 = n-1
        p = m+n-1
        while p1 >= 0 and p2 >= 0:
            # 4 5 6 0 0 0
            # 0 1 2
            if nums1[p1]<nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
                p -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
                p -= 1
        nums1[:p2+1] = nums2[:p2+1]
        return nums1




class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        关键在哪呢？？？
        找到区间的中间点，并根据某些条件决定去区间左半部分还是右半部分搜索
        二分查找的本质是什么，
        为什么可以二分查找，
        什么是二分查找
        又是怎么查找的，       跟中间元素对比，将待查找的区间缩小为之前的一半  ->>> 直到为0
        查找的关键在哪呢？？   有序单调
        """
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])

        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            row, col = mid // n, mid % n
            ret = matrix[row][col]

            if ret == target:
                return True
            elif ret <= target:
                left = mid + 1
            else:
                right = mid - 1
        return False

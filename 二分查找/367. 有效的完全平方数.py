class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        二分查找的关键在哪呢 ？？？
        不断缩小查找范围，
        每次减半，单调，有边界
        """
        left, right = 0, num  # 边界

        while left <= right:

            mid = left + (right - left) >> 1  # mid

            s = mid * mid

            if num == s:  # 与mid比较，看在哪一边
                return True

            elif num > s:
                left = mid + 1

            else:
                right = mid - 1

        return False


class Solution1:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        x = num  # 初始值
        while x * x > num:
            x = (x + num // x) / 2
        return x * x == num

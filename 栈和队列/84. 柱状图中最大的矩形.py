# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-1-7/

class Solution:
    def largestRectangleArea(self, heights: list) -> int:
        """
        关键在哪呢？
        先求每根柱子的包含的最大面积，先获取这个柱子左边第一个小于它的值的下标，然后获取右边第一个小于他的值的下标。
        然后再求他们的最大值。
        """
        heights.append(0)
        stack = [-1]
        ans = 0
        length = len(heights)
        for i in range(length):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        print(ans)
        return ans


s = Solution()
s.largestRectangleArea([1, 2, 3, 4, 5])

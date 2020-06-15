# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-1-7/
#60ms
class Solution:
    def largestRectangleArea(self, heights: list) -> int:
        """
        关键在哪呢？利用单调递增栈确定每块板的左右边界。哈哈哈哈。
        先求每根柱子的包含的最大面积，先获取这个柱子左边第一个小于它的值的下标，然后获取右边第一个小于他的值的下标。
        然后再求面积的最大值。
        关键在哪呢？？？
        面积什么时候能够确定下来。
        """
        #[2, 1, 5, 6, 2, 3, 0]

        heights.append(0)
        stack = [-1]
        ans = 0
        length = len(heights)
        for i in range(length):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                l = stack[-1]
                w = i - l - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        print(ans)
        return ans


s = Solution()
s.largestRectangleArea([1, 2, 3, 4, 5])
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        res = 0

        stack = []

        for i in range(size):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]

                while len(stack) > 0 and cur_height == heights[stack[-1]]:
                    stack.pop()

                if len(stack) > 0:
                    cur_width = i - stack[-1] - 1
                else:
                    cur_width = i

                res = max(res, cur_height * cur_width)
            stack.append(i)

        while len(stack) > 0 is not None:
            cur_height = heights[stack.pop()]
            while len(stack) > 0 and cur_height == heights[stack[-1]]:
                stack.pop()

            if len(stack) > 0:
                cur_width = size - stack[-1] - 1
            else:
                cur_width = size
            res = max(res, cur_height * cur_width)

        return res

#72ms
class Solution2:
    def largestRectangleArea(self, heights: list) -> int:
        """
        关键在哪呢？
        先求每根柱子的包含的最大面积，先获取这个柱子左边第一个小于它的值的下标，然后获取右边第一个小于他的值的下标。
        然后再求他们的最大值。
        单调递增栈已经确定了左边界，左边界其实就是自己，之所以要确定左边界，是为了计算宽度，
        关键还是在于题目的意图，最大矩形面积。
        """
        # [2, 1, 5, 6, 2, 3, 0]

        heights.append(0)
        stack = [(-1, -1)]
        ans = 0
        length = len(heights)
        for i in range(length):
            while heights[i] < stack[-1][1]:
                _, cur_h = stack.pop()
                l, _ = stack[-1]
                w = i - l - 1
                ans = max(ans, cur_h * w)
            stack.append((i, heights[i]))
        heights.pop()
        print(ans)
        return ans

#64ms
class Solution4:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [(-1, -1)]
        ans = 0
        length = len(heights)
        for i in range(length):
            while heights[i] < stack[-1][1]:
                ans = max(ans, (stack.pop()[1]) * (i -  stack[-1][0] - 1))
            stack.append((i, heights[i]))
        return ans



















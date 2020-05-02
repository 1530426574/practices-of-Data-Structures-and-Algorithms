from collections import deque
class Solution:
    def maxSlidingWindow(self, nums:list, k: int) -> list:
        """
        ****单调递减队列*****
        双向队列添加什么，索引还是元素，
        头部保存什么，尾部添加什么
        ****当前元素
        001 处理前K个元素，初始化双向队列
        002 遍历整个数组，在每一步，清理双向队列
        003 保留当前滑动窗口元素的索引
        004 移除比当前元素的所有元素的索引，他们不可能是最大的
        005 将当前元素加入到双向队列中
        006 将deque[0]添加到输出中
        007 返回输出数组
         9 7 8 6 5 4 3 2 1
         1  3  -1 -3  5  3  6  7
         滑动窗口的位置                最大值
            ---------------               -----
            [1  3  -1] -3  5  3  6  7       3
             1 [3  -1  -3] 5  3  6  7       3
             1  3 [-1  -3  5] 3  6  7       5
             1  3  -1 [-3  5  3] 6  7       5
             1  3  -1  -3 [5  3  6] 7       6
             1  3  -1  -3  5 [3  6  7]      7
        首先想到的是使用堆，因为在最大堆中 heap[0] 永远是最大的元素
        """
        res = []
        bigger = deque()
        for i ,n in enumerate(nums):
            while bigger and nums[bigger[-1]] <= n:
                bigger.pop()
            bigger += [i]
            if  i - bigger[0] >=k: #9  8 7 6 5 4 3 2 1
                bigger.popleft()
            if i+1 >= k:
                res.append(nums[bigger[0]])
        return  res



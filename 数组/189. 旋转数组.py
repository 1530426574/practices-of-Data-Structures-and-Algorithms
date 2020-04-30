class Solution:
    def rotate(self, nums, k):
        """
        length = 3
        (i+k)%len(nums)
        # k = 6 ,9 ->i
        #k = 4  ->i+1
        1, 2, 3
        001 3 1 2
        002 2 3 1
        003 1 2 3
        暴力求解法：有点像替换，先用事先准备好的数据pre，替换当前第一个cur，然后保留被替换的pre1，去替换下一个cur1,
        这里的关键是遍历会帮我们一个个按顺序轮询
        输入: [1,2,3,4,5,6,7] 和 k = 3
        输出: [5,6,7,1,2,3,4]

        解释:
        向右旋转 1 步: [7,1,2,3,4,5,6]
        向右旋转 2 步: [6,7,1,2,3,4,5]
        向右旋转 3 步: [5,6,7,1,2,3,4]
        """
        length = len(nums)
        for i in range(k):
            pre = nums[-1]    #每次遍历从新设置初始值          ## [1,2,3,4,5,6,7]
            for j in  range(length): # [7,2,3,4,5,6,7] # [7,1,3,4,5,6,7]
                cur = nums[j]
                nums[j]= pre
                pre = cur #有点像替换，然后保留被替换的，去替换下一个
class Solution1:
    def rotate(self, nums, k):
        """
        关键在哪呢？
        001 原来下标为 i 的我们把它放到 (i+k)%length 的位置
        """
        length = len(nums)
        a = [0]*length
        k = k%length #k>length
        for i in  range(length):
#       输入: [1,2,3,4,5,6,7] 和 k = 3
#       向右旋转 3 步: [5,6,7,1,2,3,4]
            a[(i+k)%length]=nums[i]
        for i in range(length):
            nums[i] = a[i]

class Solution4:
    def rotate(self, nums, k) -> None:
        """
        这个方法基于这个事实：当我们旋转数组 k 次， k\%nk%n 个尾部元素会被移动到头部，剩下的元素会被向后移动。

        在这个方法中，我们首先将所有元素反转。然后反转前 k 个元素，再反转后面 n-kn−k 个元素，就能得到想要的结果。

                假设 n=7n=7 且 k=3k=3 。

                原始数组                  : 1 2 3 4 5 6 7
                反转所有数字后             : 7 6 5 4 3 2 1
                反转前 k 个数字后          : 5 6 7 4 3 2 1
                反转后 n-k 个数字后        : 5 6 7 1 2 3 4 --> 结果
        """
        k %= len(nums)
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0, k-1)
        self.reverse(nums,k, len(nums)-1)

    def reverse(self, nums, start, end) -> None:
        """
        注释：咋觉得算法题的关键是，最后结果是什么样子的。
        关键在哪呢：数组元素翻转，等价于首尾元素互换位置，然后向里逐渐逼近。
        """
        # 4 5 6 7 8  -> 8 7 6 5 4
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1 # 用的很多额，有木有笑
            end -= 1 #
        # while start < end: #
        #     temp = nums[start]
        #     nums[start] = nums[end]
        #     nums[end] = temp
        #     start += 1
        #     end -= 1

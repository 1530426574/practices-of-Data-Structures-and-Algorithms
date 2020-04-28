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


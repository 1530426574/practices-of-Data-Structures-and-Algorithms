from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        关键在哪呢？？？               比较位置，即比较索引
        001 位置                  -> 索引
        002 跳跃最远距离           -> 元素的值
        003 判断下个节点是否能够达到
        004 当前位置能够到达的最远位置= i+nums[i]  i为索引
        输入: [2,3,1,1,4]
        [1,0,0,0,4]
        """

        length,rightmost=len(nums),0
        for i in range(length):
            if i <= rightmost:                       #先判断当前位置是否可达到
                rightmost = max(rightmost,i+nums[i]) #若是能够到达，最远到达的位置
                if rightmost >= (length-1):          #最远到达的位置是不是最后一个位置
                    return True                      #若是就返回True
        return  False


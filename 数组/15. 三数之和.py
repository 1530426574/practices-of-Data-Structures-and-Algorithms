class Solution:
    def threeSum(self, nums: list):
        """
        #[-4,-1, -1, 0,1, 2,] 有点像排列组合，先固定nums[0]，然后从从后面的元素当中选2个，然后进行条件判断。
        #关键在哪呢？  total = a[i] + a[l] +a[r] ,l与r，一个从左，一个从右开始逐渐逼近（为啥要这样？？？二分查找？？？）
        本质是什么，本质是我要把后面的元素遍历一遍，是两头开始遍历（更快）自增自减，还是一头遍历）
        001 先排序，然后进行遍历。
        002 然后进行遍历。
        003 a[i]>0 :break
        004 a[i]=a[i-1] :continue
        005 #[-4,-1, 0,0,0,4,4,4,4] #[-4,-1, 0,0,0,4] #[-4,-1, 0,4,4,4,4]
        006 total<0 : l += 1
        007 total>0 : r -= 1
        008 total = 0: 先保存当前的，重复的，就自增（自减）。

https://leetcode-cn.com/problems/3sum/
        """
        length = len(nums)
        res = []
        if not nums or length < 3:
            return []
        nums.sort()
        for i in range(length - 2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i - 1]: continue
            l, r = i + 1, length - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:  # [-4,-1,0,0,0,4]
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:  # [-4,-1, 0,0,0,0,1，2，3，4,4,4,4]
                        r -= 1
                    l += 1
                    r -= 1
        return res


def test_threeSum(nums: list):
    """
    #[-4,-1, -1, 0,1, 2,]


    """
    length = len(nums)
    res = []
    if not nums or length < 3:
        return []
    nums.sort()
    for i in range(length - 2):
        if nums[i] > 0: break
        if i > 0 and nums[i] == nums[i - 1]: continue
        l, r = i + 1, length - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                print(1, nums[i], nums[l], nums[r])
                res.append([nums[i], nums[l], nums[r]])
                while nums[l + 1] == nums[l] and l < r:
                    l += 1
                while nums[r - 1] == nums[r] and l < r:
                    r -= 1
                l += 1
                r -= 1
    return res


test_threeSum([-4, -1, 0, 0, 0, 4, 4, 4, 4])


class Solution3:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        l = []
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        l.append([nums[i], nums[j], nums[k]])
        return l

class Solution1(object):
    def moveZeroes(self, nums):
        """
        001 核心关键：还是 if a[i]!=0 : a[j] = a[i],j+=1
        002 关键在于j ,以及后面的 j+=1
        """
        length = len(nums)
        if length == 0:  # 如果数组为空，则返会0
            return 0
        j = 0
        for i in range(length):
            if nums[i]:  # 如果是非0元素，就把它赋值到数组第1个位置，然后依次累加，第2个，第3个，第4个 第j个
                nums[j] = nums[i]
                j += 1
        for i in range(j, length):
            nums[i] = 0


###2
class Solution2(object):
    def moveZeroes(self, nums):
        """
        核心关键：还是 if a[i]!=0 : a[j] = a[i],j+=1
        *** nums[j] = 0
        """
        length = len(nums)
        if length == 0:  # 如果数组为空，则返会0
            return 0
        j = 0
        for i in range(length):
            if nums[i] == 0:
                continue
            else:
                print(nums[i], nums[j])
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


def test_moveZeroes(nums):
    """
    001 核心关键：还是 if a[i]!=0 : a[j] = a[i],j+=1
    002 关键在于j ,以及后面的 j+=1
    """
    length = len(nums)
    if length == 0:  # 如果数组为空，则返会0
        return 0
    j = 0
    for i in range(length):
        if nums[i] == 0:
            continue
        else:
            print('+++', nums[i], nums[j])
            nums[j], nums[i] = nums[i], nums[j]
            print('---', nums[i], nums[j])
            j += 1
    print(nums)
    return nums


test_moveZeroes([1, 2, 3, 4, 0, 5])

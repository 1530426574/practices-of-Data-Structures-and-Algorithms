#  输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# 输出：[2,2,2,1,4,3,3,9,6,7,19]
# count 的索引i =array[i]
class Solution:

    def relative_sort_array(self, arr1: list, arr2: list) -> list:
        count = [0 for i in range(1001)]  # k
        output = []
        for i in range(len(arr1)):  # O(n)
            count[arr1[i]] += 1
        # count= [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],

        for i in range(len(arr2)): # firt access first in
            while count[arr2[i]] > 0:  # 2有几个，就填几次。
                output.append(arr2[i])  # [2,2,2,1 ,4,2,2,9,6,]
                count[arr2[i]] -= 1

        for i in range(len(count)):  # O(K)
            while count[i] > 0:
                output.append(i)
                count[i] -= 1
# 给你两个数组，arr1 和 arr2，
#
#
#  arr2 中的元素各不相同
#  arr2 中的每个元素都出现在 arr1 中
#
#
#  对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末
# 尾。
#
#
#
#  示例：
#
#  输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# 输出：[2,2,2,1,4,3,3,9,6,7,19]
#
#
#
#
#  提示：
#
#
#  arr1.length, arr2.length <= 1000
#  0 <= arr1[i], arr2[i] <= 1000
#  arr2 中的元素 arr2[i] 各不相同
#  arr2 中的每个元素 arr2[i] 都出现在 arr1 中
#
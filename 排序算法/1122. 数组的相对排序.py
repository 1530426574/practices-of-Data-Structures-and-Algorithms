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

        for i in range(len(arr2)):
            while count[arr2[i]] > 0:  # 2有几个，就填几次。
                output.append(arr2[i])  # [2,2,2,1 ,4,2,2,9,6,]
                count[arr2[i]] -= 1
        for i in range(len(count)):  # O(K)
            while count[i] > 0:
                output.append(i)
                count[i] -= 1

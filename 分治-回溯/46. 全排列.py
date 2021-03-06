"""
输入: [1,2,3]
输出:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:  # 44ms
    def permute(self, nums: list) -> list:
        """ [1 2 3 4] 4 2   隐含条件，不重复选择 n! ，所以选择列表会逐渐变小。
        关键在哪呢？？？关键在于选择列表，接下来是怎么变化的。
         排列组合，C(n,k) ，C(n,n) 从n个里面选k个，for循环里面，做选择，C在{\displaystyle C_{k}^{n}}C_k^n
        """

        def traceback(nums, path):
            if not nums:  # 选择列表为空了，哈哈哈
                res.append(path[:])
            for i in range(len(nums)):  # 用了索引，而不是直接遍历元素。
                path.append(nums[i])  # 做选择 选择i ，路径path添加i
                traceback(nums[:i] + nums[i + 1:], path)  # 选择列表nums除去i ->nums.pop(i)=nums[:i]+nums[i+1:] ,记录新的路径
                path.pop()  # 撤销选择

        res = []
        path = []
        traceback(nums, path)
        return res


# 还真不能用nums.pop(i),这样在遍历nums的时候，nums的长度还在发生变化。


class Solution1:  # 44ms
    def permute(self, nums: list) -> list:
        """"""

        def traceback(nums, path):
            if len(path) == length:  # 路径满了
                res.append(path[:])
            for i in range(len(nums)):  # 一定是len（nums),不是固定的length,因为每次进入下一个回溯函数，选择列表在不断的变化（变小），哈哈哈
                path.append(nums[i])
                traceback(nums[:i] + nums[i + 1:], path)
                path.pop()

        length = len(nums)
        res = []
        path = []
        traceback(nums, path)
        return res

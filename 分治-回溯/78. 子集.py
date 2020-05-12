class Solution:#36ms
    def subsets(self, nums: list) :
        length = len(nums)
        res = [[]]
        for i in nums: #1 2 3              #为什么不是cur.append(i),因为cur.append(i)返回的None
            res+=[cur +[i] for cur in res] #[1]    -?res=[[],[1]]
                                        # [[2],[1,2]] ->[[],[1],[2],[1,2]]
                                        #[[3],[1,3],[2,3],[1,2,3]]->[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        return res

"""
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
幂集是所有长度从 0 到 n 所有子集的组合。
说明：解集不能包含重复的子集。
"""
class Solution1:
    def subsets(self, nums:list) -> list:
        def backtrack(index, path, k):
            # if the combination is done
            if len(path) == k:
                res.append(path[:])
            for i in range(index, n):   #啊啊啊，我忘了，回溯最关键的点是选择列表。为什么不是len(nums)
                # add nums[i] into the current combination
                path.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, path, k)  #这里新的选择列表为什么不是nums[:i]+nums[i+1:]???这个表达式的意思是，选择了后面的，还可以选择前面的，
                # backtrack                #比如k=2时，i = 1 ->path [1,2][1,3]; i=2 ->path[2,1],[2,3]
                path.pop()                 #现在的情况是k=2时，i =1 ->path[1,2][1,3] ;i =2 ->path[2,3],不重复前面的选择。

        res = []
        n = len(nums)
        for k in range(n + 1):
            index = 0
            path = []
            backtrack(index, path, k)
        return res


class Solution1:
    def subsets(self, nums: list) :
        def backtrace(nums,path,k):
            if len(path) ==k:
                res.append(path[:])
            for i in range(index,length):
                path.append(i)
                backtrace(index+1,path,k)
                path.pop(i)
        res = []  #1 2 3 4
        length=len(nums)
        for k in range(length+1):
            path =[]
            index =0
            backtrace(index,path,k)
        return res


class Solution3:
    def subsets(self, nums: list) -> list:
        def backtrack(first=0, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output


# DFS recursively
def subsets1(self, nums):
    res = []
    self.dfs(sorted(nums), 0, [], res)
    return res


def dfs(self, nums, index, path, res):
    res.append(path)
    for i in xrange(index, len(nums)):
        self.dfs(nums, i + 1, path + [nums[i]], res)


# Bit Manipulation
def subsets2(self, nums):
    res = []
    nums.sort()
    for i in range(1 << len(nums)):
        tmp = []
        for j in xrange(len(nums)):
            if i & 1 << j:  # if i >> j & 1:
                tmp.append(nums[j])
        res.append(tmp)
    return res


# Iteratively
def subsets(self, nums):
    res = [[]]
    for num in sorted(nums):
        res += [item + [num] for item in res]
    return res
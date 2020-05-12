from typing import List
class Solution:#496ms  61.58% 1 2 3 4 -> n=4 ,k =2  当len(path) =2 时，就终止，已经选完了。
    def combine(self, n: int, k: int) -> List[List[int]]: #隐含条件，选了前面的，选择列表只能是后面的。
        def backtrack(index=1, path=[]):
            # if the combination is done
            if len(path) == k: # path = [1,2]
                res.append(path[:])  # 为什么不是加path,而是加path[:],如果加入path,相当于加入一个变量，变量名称不会变，但它引用的对象会发生变化。# 而加入path[:]，加入的是一个对象。
            for i in range(index, n + 1): #按顺序遍历选择列表来实现选择，而不是随机选择。
                # 做选择 -> 路径添加             add i into the current combination
                path.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, path) #backtrack(路径, 选择列表) 进入下一层决策树
                # backtrack
                path.pop()  # 撤销选择 路径.remove(选择)

        res = []
        backtrack()
        return res


class Solution1: # 488ms 1 2 3 4
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
            # 做选择
            将该选择从选择列表移除
            路径.add(选择)
            backtrack(路径, 选择列表) #进入下一层决策树
            # 撤销选择
            路径.remove(选择)
            将该选择再加入选择列表
        """


        res = []
        self.backtrack(n, k, res, [], 1)
        return res

    def backtrack(self, n, k, res, path, index):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(index, n + 1):
                # 做选择
                # 将该选择从选择列表移除 选择列表 i = i+1 i 加完1 之后，自然选择列表就变了，index变了
                # 路径.add(选择)  路径 path ,  path.append(i)

                path.append(i)
                #backtrack(路径, 选择列表) #进入下一层决策树
                self.backtrack(n, k, res, path , i +1)
                # 撤销选择
                # 路径.remove(选择)
                path.pop()
                # 将该选择再加入选择列表


"""
输入: n = 4, k = 2
输出:                       
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

#选了2之后，就没有[2,1]都是从后面开始选择，越遍历到后面，选择列表是变小的，
1 -> 2 3 4 
2 -> 3 4
3 -> 4  
i ->  i+1 .....n
"""



    #     res = []
    #     def backtrack( n, k, res, path, index):
    #         if len(path) == k: #[1,2]
    #             res.append(path)
    #             return
    #
    #         for i in range(index, n + 1):
    #             #做出选择
    #              #将该选择从选择列表移除
    #             i+=1
    #             path.append(1)  #路径.add(选择)
    #             backtrack(n, k, res, path, i)
    #     backtrack(n, k, res, [], 1)
    #     return res
    #
    # def backtrack(self, n, k, res, path, index):
    #     if len(path) == k:
    #         res.append(path)
    #         return
    #     for i in range(index, n + 1):
    #         self.backtrack(n, k, res, path + [i], i + 1)
    #
    #
    #
    # def combine(self, n: int, k: int) -> List[List[int]]:
    #     def traceback(n,k,res,path,index):
    #         if  k == 0 :
    #             res.append(path)
    #         for i in range(index,n):
    #             traceback(n,)
    #
    #
    #
    #
    #     if n < 0 or k <=0 or k>n:
    #         return []
    #     res = []
    #     self.dfs(1,k,n,[])


from typing import List
from pprint import pprint

class Solution1:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1:return []
        self.result = []
        self.dfs(n,0,[],set(),set(),set())
        return [["." * j + "Q" + "." * (n - j - 1) for j in path] for path in self.result]

    def dfs(self,n,row,path:list,cols:set,pie:set,na:set):
        if row >= n:
            self.result.append(path)
            return
        for col in range(n):
            if col in cols or row+col in pie or row-col in na:
                continue
            self.dfs(n,row+1,path+[col],cols.union({col}),pie.union({row+col}),na.union({row-col}))










class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        if n < 1:return []
        self.result = []
        self.cols, self.pie, self.na = set(), set(), set()
        self.dfs(n,0,[])
        return self.generate_result(self.result,n)

    def dfs(self,n,row,path):
        if row >= n:
            self.result.append(path)
            return
        for col in range(n):
            if col in self.cols or row+col in self.pie or row-col in self.na:
                continue
            self.cols.add(col)
            self.pie.add(row+col)
            self.na.add(row-col)
            self.dfs(n,row+1,path+[col])
            self.cols.remove(col)
            self.pie.remove(row+col)
            self.na.remove(row-col)

    def generate_result(self,result,n):
        print(1,result)
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]
        # return ["." * result[i] + "Q" + "." * (n - result[i] - 1) for i in range(n)]





class Solution1s:
    def solveNQueens(self, n: int) :
        if  n < 1 :return []
        self.result = []
        self.cols, self.pie, self.na = set(), set(), set()
        row = 0
        path = []
        self.dfs(row,path,n)
        return self.generate_result(self.result,n)

    def dfs(self,i,path:list,n:int):
        if i >= n  :
            # print('i={},path ={}'.format(i,path))
            self.result.append(path[:])
            return

        for j in range(n):
            if j in self.cols or  i+j in self.pie or i-j in self.na:
                continue
            self.cols.add(j)
            self.pie.add(i+j)
            self.na.add(i-j)
            path.append(j)         #路径选择
            self.dfs(i+1,path,n)   #选择列表 0 -> 1
            path.pop()              #撤销路径

            self.cols.remove(j)
            self.pie.remove(i+j)
            self.na.remove(i-j)

    def generate_result(self,result,n):
        print(1,result)
        return [["." * col + "Q" + "." * (n - col - 1) for col in path] for path in result]
        # return ["." * result[i] + "Q" + "." * (n - result[i] - 1) for i in range(n)]


if __name__ == '__main__':
    n = 8
    solution = Solution1s()
    res = solution.solveNQueens(n)
    pprint(res)

# from pprint import pprint
#
# a = [1, 3, 0, 2]
# b = [['*' for j in range(4)] for i in range(4)]
# pprint(b)
# for i, j in enumerate(a):
#     b[i][j] = 'Q'
# pprint(b)
#
#
# def result(result, n):
#     return [['.' * col + 'Q' + (n - col - 1) * '.' for col in path] for path in result]

#     '.' * col  + Q + (n - 1 - col) *'.'
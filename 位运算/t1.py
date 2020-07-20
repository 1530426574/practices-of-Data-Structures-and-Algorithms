# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         if n < 1:return []
#         self.result = []
#         self.dfs(n,0,[],[],[],[])
#         return self.generate_result(self.result,n)
#     def dfs(self,n,i,path,cols,pie,na):
#         if i == n :
#             self.result.append(path[:])
#         for j in range(n):
#             if j not in cols or i + j not in pie or j - i not in na:
#                 self.dfs(i+1,n,path + [j], cols + [j], pie + [i + j], na +[j - i])
#
#
#
#
#
#     def generate_result(self,result,n):
#         print(1,result)
#         return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]
#         # return ["." * result[i] + "Q" + "." * (n - result[i] - 1) for i in range(n)]
result = [[1, 2, 3, 0], [2, 3, 0, 1]]
n = 4
for sol in result:
    for j in sol:
        print('.' * j + 'Q' + (n - j - 1) * '.')
    print('++++++++++++++++++')

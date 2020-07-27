# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
# 示例:
# X X X X
# X O O X
# X X O X
# X O X X

# 运行你的函数后，矩阵变为：
# X X X X
# X X X X
# X X X X
# X O X X
#
# 解释:
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被
# 填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
# Related Topics 深度优先搜索 广度优先搜索 并查集
# 由于并查集我们一般用一维数组来记录，方便查找 parants，所以我们将二维坐标用 node 函数转化为一维坐标。


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List
class UnionFind:

    def __init__(self, length: int):
        self.parents = [i for i in range(length)]

    # 连通：有共同的root节点
    def union(self, node1: int, node2: int):
        root1 = self.find_root(node1)
        root2 = self.find_root(node2)
        self.parents[root1] = root2

    def find_root(self, node: int) -> int:
        root = node
        while self.parents[root] != node:
            root = self.parents[root]

        while self.parents[node] != node:
            x = node
            node = self.parents[x]
            self.parents[x] = root
        return root

    def is_connected(self, node1: int, node2: int):
        return self.find_root(node1) == self.find_root(node2)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        if not board or len(board[0]) == 0:
            return
            # X X X X           X X X X             X X X X
            # X X O X  ->       X O O X    ->       X X X X
            # X O X X           X 1 O X             X O X X
            # X O X X           X 1 X X             X O X X
        rows = len(board)
        cols = len(board[0])
        uf = UnionFind(rows * cols + 1)
        dumynode = rows * cols
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and board[i][j] not  in visited:
                    visited.add(board[i][j])
                    if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                        uf.union(self.two_to_one(i, j), dumynode)
                    else:
                        for _i, _j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            di, dj = i + _i, j + _j
                            if board[di][dj] == 'O' and board[di][dj] not in visited and di > 0 and dj > 0 and di < rows - 1 and dj < cols - 1:
                                uf.union(self.two_to_one(di, dj), self.two_to_one(i, j))

        for i in range(rows):
            for j in range(cols):
                if uf.is_connected(self.two_to_one(i, j), dumynode):
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

    # 二维 -> 一维
    def two_to_one(self, i, j, cols=3):
        return i * cols + j

    # 一维 -> 二维
    def one_to_two(self, index, cols=3):
        return index // cols, index % cols

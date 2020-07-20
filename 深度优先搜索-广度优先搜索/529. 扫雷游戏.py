"""
点击后，先判断自己，然后判断相邻节点
001 如果点击点是M（地雷）把改点赋值为X,gameover
002 如果不是地雷，则：
如果E与M不相邻，则把E改为B,并且递归所有相邻模块
如果E与M相邻，则把E改为str(mine_count)
003 最后返回面板
"""


class Solution:

    def updateBoard(self, board: list, click: list) -> list:
        """
        [["E","E","E","E","E"],
        ["E","E","M","E","E"],
        ["E","E","E","E","E"],
        ["E","E","E","E","E"]]
            [3,0]
            输出: 1以后不在进行遍历
        [['B', '1', 'E', '1', 'B'],
         ['B', '1', 'M', '1', 'B'],
         ['B', '1', '1', '1', 'B'],
         ['B', 'B', 'B', 'B', 'B']]
        """
        if not board or not board[0]:
            return []
        i, j = click[0], click[1]
        if board[i][j] == "M":
            board[i][j] = "X"
            return board
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        self.dfs(i, j, m, n, board, directions)
        return board

    def dfs(self, i, j, m, n, board, directions):
        if board[i][j] != "E":
            return
        mine_count = 0
        for d in directions:
            di, dj = i + d[0], j + d[1]
            if 0 <= di < m and 0 <= dj < n and board[di][dj] == "M":
                mine_count += 1
        if mine_count == 0:
            board[i][j] = "B"
        else:
            board[i][j] = str(mine_count)
            return
        for d in directions:
            di, dj = i + d[0], j + d[1]
            if 0 <= di < m and 0 <= dj < n:
                self.dfs(di, dj, m, n, board, directions)


def dfs1(i, j, m, n, board, directions):
    if board[i][j] != 'E':
        return
    t = [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1), (i, j + 1), (i + 1, j + 1), (i - 1, j - 1), (i - 1, j + 1)]
    count = 0
    for k, v in t:
        if 0 < k < m and 0 < v < n and board[k, v] == 'M':
            count += 1
    if count == 0:
        board[i][j] = 'B'
    else:
        board[i][j] = str(count)
        return
    for k, v in t:
        if 0 < k < m and 0 < v < n:
            dfs1(k, v, m, n, board, directions)

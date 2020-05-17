class Solution:

    def updateBoard(self, board: list, click: list) -> list:
        """
        [["E","E","E","E","E"],
        ["E","E","M","E","E"],
        ["E","E","E","E","E"],
        ["E","E","E","E","E"]]
            [3,0]
        """
        if not board:
            return []

        m,n = len(board), len(board[0])
        i , j = click[0],click[1]

        if board[i][j] =='M':
            board[i][j]='X'
            return board
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        self.dfs(self,i,j,m,n,board,directions)
        return board

    def dfs(self,i,j,m,n,board,directions):
        if board[i][j]!= 'E':
            return

        count = 0
        for d in directions:
            i ,j = i+d[0],j+d[1]
            if 0<=i<m and 0<j<n and board[i][j]=='M':
                count+=1
        if count==0:
            board[i][j]='B'
        else:
            board[i][j]=str(count)
            return
        for d in directions:
            i, j = i + d[0], j + d[1]
            if 0 <= i < m and 0 < j < n and board[i][j] == 'M':
                self.dfs(i,j,m,n,board,directions)




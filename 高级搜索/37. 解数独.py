from collections import defaultdict
class Solution1:
    def solve_soduko(self,board):
        """
        # if sudoku is solved, there is no need to backtrack
        # since the single unique solution is promised
        """
        rows = [set(range(9)) for _ in range(9)] #初始化每行需要填的数字（1-9）
        cols = [set(range(9)) for _ in range(9)]
        boxes = [set(range(9)) for _ in range(9)]
        empty = []                #收集需要填数的位置
        for i in range(9):
            for j in range(9):
                box_index = (i // 3)*3 + j // 3
                if board[i][j] != '.':
                    val = int(board[i][j])
                    rows[i].remove(val)
                    cols[j].remove(val)
                    boxes[box_index].remove(val)
                else:
                    empty.append((i,j))         #i,j 为空，需要填数
        #这样就得到需要填数的坐标，以及每行还剩哪些数字可供选择
        index = 0
        self.traceback(index, empty,rows,cols,boxes)

    def traceback(self,index,empty,rows,cols,boxes):
        if index == len(empty):
            return  True
        i, j = empty[index]
        box_index = (i // 3)*3 + j // 3
        for val in (rows[i] & cols[j] & boxes[box_index] ):
            rows[i].remove(val)
            cols[j].remove(val)
            boxes[box_index](val)
            board[i][j] = str(val)
            if tracebacke(index + 1): # find one solution ,stop .
                return  True
            rows[i].add(val)
            cols[j].add(val)
            boxes[box_index].add(val)
        return False













        rows = [{} for _ in range(9)]


    self.traceback(index,empty)
board = [["5","3",".",".","7","8",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"],]
row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
boxes = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字
print(1,row)
print(2,col)
print(3,boxes)
empty = []  # 收集需填数位置
for i in range(9):
    for j in range(9):
        if board[i][j] != '.':  # 更新可用数字
            val = int(board[i][j])
            row[i].remove(val)
            col[j].remove(val)
            boxes[(i // 3) * 3 + j // 3].remove(val)
        else:
            empty.append((i, j))
print(1,row)
print(2,col)
print(3,boxes)
print(7,empty)
# for val in row[0] & col[0] & boxes[0]:
#     print(val)
print({1, 2, 4, 6, 9}&{1, 2, 3, 4, 5, 6, 7, 9}&{1, 2, 4, 7})
def tracebacke(index= 0):
    if index == len(empty):
        return True
    i, j = empty[index]
    b = (i//3) * 3 + j // 3
    for val in row[i] & col[j]& boxes[b]:
        row[i].remove(val)
        col[j].remove(val)
        boxes.remove(val)
        board[i,j] = str(val)
        if tracebacke(index+1):#    # if sudoku is solved, there is no need to backtrack
                                    # since the single unique solution is promised
        row[i].add(val)
        col[j].remove(val)
        boxes[b].add(val)
    return False




















class Solution2:
    def solve_sudoku(self,board):

        n = 3
        N = n * n
        self.N = N
        self.board = board
        self.box_index = lambda row, col :(row // n)*n +col // n

        self.rows = [defaultdict(int) for i  in range(N)]
        self.cols = [defaultdict(int) for i  in range(N)]
        self.boxes = [defaultdict(int) for i  in range(N)]

        for  i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    self.place_number(num,i,j)

    def place_number(self,num:int,i,j):
        self.rows[i][num] += 1
        self.cols[j][num] += 1
        self.boxes[self.box_index(i,j)][num] += 1
        self.board[i][j] = str(num)

    def remove_number(self,num,i,j):
        del self.rows[i][num]
        del self.cols[j][num]
        del self.boxes[self.box_index(i,j)][num]
        self.board[i][j] = '.'

    def place_next_numbers(self,i,j):

        if i == self.N-1 and j == self.N-1:
            self.solved = True
        else:
            if j == self.N-1:
                self.traceback(i+1,0)
            else:
                self.traceback(i,j+1)

    def could_place(self,num,i,j):
        if num  in self.rows[i] or\
                num in self.cols[j] or\
                num in self.boxes[self.box_index(i,j)]:
            return False
        return True

    def traceback(self,i = 0, j = 0):
        if self.board[i][j] == '.':
            for num in range(1,10):
                if self.could_place(num,i,j):
                    self.place_number(num,i,j)
                    self.place_next_numbers(num,i,j)
                    if not self.solved:
                        self.remove_number(num,i,j)

        else:
            self.place_next_numbers(i,j)
from pprint import pprint
a = [[((i//3)*3+j//3) for i in range(9)]for j in range(9)]
pprint(a)
# box_index =  (i//3)*3+j//3
# box_index =  (j//3)*3+i//3
class Solution1:
    def isValidSudoku(self, board):
        """
        关键在哪呢？？？统计每行、每列、每个box的  词频
        """

        #init data               统计每行、每列、每个box的  词频
        rows = [{} for i in range(9)]
        colums = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        #vilidate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                box_index = (i //3 ) * 3 + j // 3
                if num != '.':
                    #keep the current cell value
                    rows[i][num] = rows[i].get(num,0) + 1
                    colums[j][num] = colums[j].get(num,0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num,0)+1
                #check the value has been already seen before
                if rows[i][num] > 1 or colums[j][num] > 1 or boxes[box_index][num] > 1:
                    return False
        return True


board = [["5","3",".",".","7","8",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"],]

a = [[(board[i][j],i),(j,board[i][j]),(board[i][j],(i//3),j//3,)] for i in range(9) for j in range(9) if board[i][j] != '.']
pprint(a)
# print(sum(a,[]))
#
print(len(sum(a,[])))
print(len(set(sum(a,[]))))
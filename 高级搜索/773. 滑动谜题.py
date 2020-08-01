from typing import List

board = [[1, 2, 3],
         [4, 0, 5]]


class Solution:
    def sliding_puzzle(self, board: List[List[int]]):
        board = [board[i][j] for i in range(len(board)) for j in range(len(board[0]))]  # [1, 2, 3, 4, 0, 5]
        moves = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4)]#save indexes
        # moves = {0: (1, 3),
        #          1: (2, 4, 0),
        #          2: (5, 1),
        #          3: (0, 4),
        #          4: (1, 5, 3),
        #          5: (2, 4)
        #          }
        q, vistited = [(tuple(board), board.index(0), 0)], set()
        while q:
            state, zero_index, step = q.pop(0)
            if state == (1, 2, 3, 4, 5, 0):
                return step       # level
            vistited.add(state)
            for next in moves[zero_index]:
                new_state = list(state)  # 移动0 之后，等价于数组里面元素互换，生成新的数组（元祖），加入队列当中
                new_state[next], new_state[zero_index] = new_state[zero_index], new_state[next]
                new_state = tuple(new_state)
                if new_state not in vistited:
                    q.append((new_state, next, step + 1))
            return -1


class Solution1:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        board = board[0] + board[1]  # 把board连起来变一维
        moves = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4)]  # 每个位置的0可以交换的位置
        q, visited = [(tuple(board), board.index(0), 0)], set()  # bfs队列和已访问状态记录
        while q:
            state, zero, step = q.pop(0)  # 分别代表当前状态，0的当前位置和当前步数
            if state == (1, 2, 3, 4, 5, 0):  # 找到了
                return step
            for next in moves[zero]:  # 遍历所有可交换位置
                new_state = list(state)
                new_state[next], new_state[zero] = new_state[zero], state[next]  # 交换位置
                new_state = tuple(new_state)
                if new_state not in visited:  # 确认未访问
                    q.append((new_state, next, step + 1))
            visited.add(state)
        return -1


board = [[1, 2, 3],
         [4, 0, 5]]
board1 = [board[i][j] for i in range(len(board)) for j in range(len(board[0]))]
print(board1)


def two_to_one(i, j, col=3):
    return i * col + j


def moves(i, j):
    # a = []
    # for _i , _j in ((-1,0),(0,1),(1,0),(0,-1)):
    #     di = i + _i
    #     dj = j + _j
    #     if di >=0 and dj >=0 and di < len(board) and dj < len(board[0]):
    #         a.append((di,dj))
    # return tuple(a)
    return [(i + _i, j + _j) for _i, _j in ((-1, 0), (0, 1), (1, 0), (0, -1)) if
            i + _i >= 0 and j + _j >= 0 and i + _i < len(board) and j + _j < len(board[0])]


b = [moves(i, j) for i in range(len(board)) for j in range(len(board[0]))]
print('b={}'.format(b))

c = [tuple([two_to_one(i, j) for i, j in item]) for item in b]
print('c = {}'.format(c))

d = {i: v for i, v in enumerate(b)}
print('d={}'.format(d))

d1 = {i: v for i, v in enumerate([tuple([i * 3 + j for i, j in item]) \
                                  for item in [[(i + _i, j + _j) \
                                                for _i, _j in ((-1, 0), (0, 1), (1, 0), (0, -1)) \
                                                if i + _i >= 0 and j + _j >= 0 and i + _i < len(board) and j + _j < len(
            board[0])]
                                               for i in range(len(board)) for j in range(len(board[0]))]])}
print('d1={}'.format(d1))

# c = {moves(i,j) for i in range(len(board)) for j in range(len(board[0]))}
# s =''
# a =[]
# for i in range(len(board)):
#     for j in range(len(board[0])):
#         print(i,j,board[i][j])
#         a.append(board[i][j])
#         # s += str(board[i][j])
# print(a)
# 在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.
#
#  一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.
#
#  最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
#
#  给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。
#
#  示例：
#
#
# 输入：board = [[1,2,3],[4,0,5]]
# 输出：1
# 解释：交换 0 和 5 ，1 步完成
#
#
#
# 输入：board = [[1,2,3],[5,4,0]]
# 输出：-1
# 解释：没有办法完成谜板
#
#
#
# 输入：board = [[4,1,2],[5,0,3]]
# 输出：5
# 解释：
# 最少完成谜板的最少移动次数是 5 ，
# 一种移动路径:
# 尚未移动: [[4,1,2],[5,0,3]]
# 移动 1 次: [[4,1,2],[0,5,3]]
# 移动 2 次: [[0,1,2],[4,5,3]]
# 移动 3 次: [[1,0,2],[4,5,3]]
# 移动 4 次: [[1,2,0],[4,5,3]]
# 移动 5 次: [[1,2,3],[4,5,0]]
#
#
#
# 输入：board = [[3,2,4],[1,5,0]]
# 输出：14
#
# 提示：
# board 是一个如上所述的 2 x 3 的数组.
# board[i][j] 是一个 [0, 1, 2, 3, 4, 5] 的排列.

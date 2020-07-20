from typing import List

board = [[1, 2, 3],
         [4, 0, 5]]


class Solution:
    def sliding_puzzle(self, board: List[List[int]]):
        board = [board[i][j] for i in range(len(board)) for j in range(len(board[0]))]  # [1, 2, 3, 4, 0, 5]
        moves = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4)]
        moves = {0: (1, 3),
                 1: (2, 4, 0),
                 2: (5, 1),
                 3: (0, 4),
                 4: (1, 5, 3),
                 5: (2, 4)}
        q, vistited = [(tuple(board), board.index(0), 0)], set()
        while q:
            state, zero_index, step = q.pop(0)
            if state == (1, 2, 3, 4, 5, 0):
                return step

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

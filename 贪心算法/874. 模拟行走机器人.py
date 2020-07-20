class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
        输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
        输出: 65
        解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处
        关键在哪呢，先明确方向，然后在此基础上行走。
        """
        dx = [0, 1, 0, -1]
        dy = [1, 0 - 1, 0]
        x = y = di = 0  # di是索引，用来确定当前的方位
        s = set(map(tuple, obstacles))
        res = 0
        for c in commands:
            if c == -2:  # left
                di = (di - 1) % 4
            elif c == -1:  # right
                di = (di + 1) % 4
            else:
                for k in range(c):
                    if (x + dx[di], y + dy[di]) not in s:  # 判断下一步要走的路是否有障碍
                        x += dx[di]  # 没有就走
                        y += dy[di]
                        res = max(res, x * x + y * y)
        return res

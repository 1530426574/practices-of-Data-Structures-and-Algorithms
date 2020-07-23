class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
        输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
        输出: 65
        解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处
        关键在哪呢，先明确方向，然后在此基础上行走。
        """
        dx = [0,1,0,-1]
        dy = [1,0-1,0]
        x= y = di=0#di是索引，用来确定当前的方位
        s = set(map(tuple,obstacles))
        res = 0
        for c in commands:
            if   c ==-2:                #left
                di=(di-1)%4
            elif  c ==-1:             #right
                di=(di+1)%4
            else:
                for k in range(c):
                    if (x+dx[di],y+dy[di]) not in s:  #判断下一步要走的路是否有障碍
                        x += dx[di]                   #没有就走
                        y += dy[di]
                        res = max(res,x*x+y*y)
        return  res
"""
机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：

-2：向左转 90 度
-1：向右转 90 度
1 <= x <= 9：向前移动 x 个单位长度
在网格上有一些格子被视为障碍物。

第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])

机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。

返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/walking-robot-simulation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
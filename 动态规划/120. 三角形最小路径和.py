class Solution:
    # top down
    def minimumTotal(self, triangle: list) -> int:
        """
        关键在哪呢？？？

        dp[i][j]表示啥，表示当前到达(i,j)这个位置的最优解

        到达每个位置的最小路径（最优情况）
        动态规划会保存以前的运算结果，
        并根据以前的结果对当前进行选择，有回退功能。
        分治 问题能够分解成子问题来解决，
        ***子问题的最优解能递推到最终问题的最优解***。
        这种子问题最优解成为最优子结构。
        重复子问题
        """

        if not triangle:
            return

        res = [[0 for _ in range(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    res[i][j] = res[i - 1][j] + triangle[i][j]  # 存储中间状态
                elif j == len(triangle[i]) - 1:
                    res[i][j] = res[i - 1][j - 1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i - 1][j - 1], res[i - 1][j]) + triangle[i][j]  # 递推公式           #最优解，中途淘汰次优解
        return min(res[-1])

    # bottom up
    def mininumtotal2(self, triangle):
        if not triangle:
            return
        res = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(triangle[i]):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
        return res[0]

    # bottom up 更好理解
    def mininumtotal3(self, triangle):
        if not triangle:
            return

        res = [[0 for i in range(len(row))] for row in triangle]
        res[-1] = triangle[-1]

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(triangle[i]):
                res[i][j] = min(res[i + 1][j], res[i + 1][j + 1]) + triangle[i][j]

        return res[0][0]

# a = []
# for row in triangle:
#     b =[]
#     for i in range(len(row)):
#         b.append(0)
#             a.append(b)

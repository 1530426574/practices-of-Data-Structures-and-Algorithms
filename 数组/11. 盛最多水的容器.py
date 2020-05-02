class Solution:
    def maxArea(self, height: list) -> int:
        """
        001 核心关键：s(j,j) = min(height[i],height[j]) * (j-i)
        002 控制变量法，在最低短板确定的时候，宽度越大，面积也越大。
        003 先固定j-i ,然后看min(height(i),height(j))
        004 在每一个状态下，无论长板或短板收窄 1 格，都会导致水槽 底边宽度 −1：
        005若向内移动短板，水槽的短板 min(h[i],h[j]) 可能变大，因此水槽面积 S(i, j)S(i,j) 可能增大。
        006若向内移动长板，水槽的短板 min(h[i],h[j]) 不变或变小，下个水槽的面积一定小于当前水槽面积。
        007 所以为了得到最大面积，要想内移动短板
        008 https://leetcode-cn.com/problems/container-with-most-water/solution/container-with-most-water-shuang-zhi-zhen-fa-yi-do/
        """
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:  # 此时已经知道最短板是height[i]
                res = max(res, min(height[i], height[j]) * (j - i))  # 记录最大面积。
                i += 1  # 为什么是i+1，因为此时已经知道最短板是height[i],如果是j-1,最短板还是height[i]
            else:  # 此时已经知道最短板是height[j]
                res = max(res, min(height[i], height[j]) * (j - i))
                j -= 1  # 为什么是j-1,因为如果是i+1,此时，j-1已经固定且缩小了，高度最高也由此时的height[j]决定。面积只会小于刚才的面积。
        return res


# 优化
class Solution1:
    def maxArea(self, height: list) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res

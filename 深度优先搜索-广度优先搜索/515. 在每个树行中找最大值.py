class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left,self.right=None,None

class Solution:
    def largestValues(self, root: TreeNode) -> list:
        if not root:
            return []
        res, stack = [], [(root, 1)]
        while stack:
            root, level = stack.pop()
            if root:
                if len(res) < level:
                    res.append(float('-inf'))  #先给每一层赋个初始值，然后比较大小
                res[level - 1]=root.val if root.val>=res[level-1] else res[level-1]
                stack.append((root.right, level + 1))
                stack.append((root.left, level + 1))
        return res

#普通选手
class Solution1:
    def largestValues(self, root: TreeNode) -> list:
        res, queue = [], [(root, 1)]
        while queue:
            root, level = queue.pop(0)
            if root:
                if len(res) < level:
                    res.append(float('-inf'))
                res[level - 1]=root.val if root.val>=res[level-1] else res[level-1]
                queue.append((root.left, level + 1))
                queue.append((root.right, level + 1))
        return res

#BFS 高手
class Solution2: #44ms
    def findValueMostElement(self, root):
        maxes = []
        row = [root]
        while any(row):
            maxes.append(max(node.val for node in row)) #每层所有节点的值
            row = [kid for node in row for kid in (node.left, node.right) if kid]  # 收集所有子节点，
                                                                                   # 每次存放的都是同一层的子节点。
        return maxes

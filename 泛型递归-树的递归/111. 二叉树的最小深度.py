class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left, self.right = None, None
        self.children = None


# recursion 80ms
class Solution1:
    def minDepth(self, root: TreeNode):
        if not root:
            return 0

        if not root.left or not root.right:  # root,left is None and root.right is None
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right))

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


# DFS 56ms
class Solution2:
    def minDepth(self, root):
        """
        关键在哪呢？？？最小值（深度）一定在叶子节点
        """
        if not root:
            return 0

        stack = [(root, 1)]
        min_dep = float('inf')  # 正无穷
        while stack:
            root, depth = stack.pop()
            if root:
                if not root.left and not root.right:  # 遇到叶子节点就更新其最小值，最小值一定咋叶子节点
                    min_dep = min(depth, min_dep)  # 相当于遍历每个节点，然后取所有节点的最小值
                stack.append((root.left, depth + 1))
                stack.append((root.right, depth + 1))
        return min_dep


# BFS 48ms
class Solution3:
    def minDepth(self, root):
        if not root:
            return 0
        from collections import deque
        q = deque([(root, 1)])
        while q:
            node, level = q.popleft()
            if node:
                if not node.left and not node.right:
                    return level  # 最小值一定在叶子结点，遇到了立刻返回。
                q.append((node.left, level + 1))
                q.append((node.right, level + 1))

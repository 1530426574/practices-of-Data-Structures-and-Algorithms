"""
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left, self.right = None, None


# Recursively
class Solution1:  # 76 ms,在所有 Python3 提交中击败了13.91%
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth1(self, root):
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0


class Solution2:  # 40 ms
    # DFS
    def maxDepth(self, root: TreeNode) -> int:
        """
        关键在哪呢？？？ 最大深度，一定是在叶子节点，也可以每个节点遍历的时候更新
        哈哈哈，叶子节点的最大深度，并且从所有的叶子节点深度求最大值
        001 在遍历的过程中，节点与子节点的层数之差为 1 ！！！
        002 不管是递归还是迭代，都是对于每个节点来说，它与它孩子节点的关系,深度相差为1。
        """
        if not root:
            return 0
        stack = [(1, root)]
        maxdepth = 0
        while stack:
            level, root = stack.pop()
            if root:
                if not root.left and not root.right:
                    maxdepth = max(maxdepth, level)  # 最大深度一定在叶子节点，所以只在叶子节点时进行更新
                stack.append((level + 1, root.right))
                stack.append((level + 1, root.left))
        return maxdepth


class Solution3:  # 52 ms
    # DFS
    def maxDepth(self, root: TreeNode) -> int:
        """
        关键在哪呢？？？ 最大深度，一定是在叶子节点，也可以每个节点遍历的时候更新
        哈哈哈，叶子节点的最大深度，并且从所有的叶子节点深度求最大值
        001 在遍历的过程中，节点与子节点的层数之差为 1 ！！！
        002 不管是递归还是迭代，都是对于每个节点来说，它与它孩子节点的关系,深度相差为1。
        """
        if not root:
            return 0
        stack = [(1, root)]
        depth = 0
        while stack:
            level, root = stack.pop()
            if root:
                depth = max(depth, level)  # 当然也可以每次迭代的时候更新
                stack.append((level + 1, root.right))
                stack.append((level + 1, root.left))
        return depth


class Solution4:  # 52ms
    # BFS + deque
    def maxDepth1(self, root):
        if not root:
            return 0
        from collections import deque
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if not node.left and not node.right and not queue:
                return level
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

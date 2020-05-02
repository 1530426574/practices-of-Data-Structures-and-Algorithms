class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left, self.right = None, None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:
        """
        关键在哪呢？循环，自相似性，重复子问题。
        先从栈中弹出根节点，然后依次向栈中加入其右孩子节点，然后是做孩子节点
        """
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node)
                stack.append(node.right)
                stack.append(node.left)

        return res

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 迭代24ms
"""执行用时 :24 ms, 在所有 Python3 提交中击败了99.31%的用户
内存消耗 :13.5 MB, 在所有 Python3 提交中击败了7.41%的用户"""


class Solution:
    def postorderTraversal(self, root: TreeNode) -> list:
        """
        关键： root.left,root.right,root,逆序
        """

        if root is None:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
                stack.append(root.left)  # 3
                stack.append(root.right)  # 2
        return output[::-1]


# 递归
"""
执行用时 :32 ms, 在所有 Python3 提交中击败了90.90%的用户
内存消耗 :13.7 MB, 在所有 Python3 提交中击败了7.41%的用户"""


class Solution1:
    def postorderTraversal(self, root: TreeNode) -> list:
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []

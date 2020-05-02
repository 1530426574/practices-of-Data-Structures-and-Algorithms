class TreeNode:
    def __init__(self, x):
        self.val = x
        self.children = None


# 迭代 52 ms
class Solution:
    def preorder(self, root: TreeNode) -> list:
        """
        root v1 v2 v3 v4 v5
        关键: 子节点以什么顺序装入栈中。倒序 v5 v4 v3 v3 v1
        出栈的顺序： root v1 v2 v3 v4 v5

        """
        if root is None:
            return []
        stack, output = [root], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])  # 逆序导入
        return output


# 递归 72ms
class Solution1:
    def preorder(self, root: TreeNode) -> list:
        if root is None:
            return []
        output, val = [], [root.val]
        for c in root.children:
            output += self.preorder(c)
        return val + output

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.children = None


class Solution:
    def postorder(self, root: TreeNode) -> list:
        """
         v1 v2 v3 v4 v5 root
        关键: 子节点以什么顺序装入栈中。顺序 v1 v2 v3 v4 v5
        出栈的顺序： root v5 v4 v3 v3 v1
        """

        if not root:
            return []
        stack, output = [root], []
        # v3 v2 v1  root v3 v2 v1
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
            for c in root.children:
                stack.append(c)
        return output[::-1]


class Solution1:
    def postorder(self, root: TreeNode) -> list:
        if root is None:
            return []
        output = []
        for c in root.children:
            output += self.postorder(c)
        return output + [root.val]

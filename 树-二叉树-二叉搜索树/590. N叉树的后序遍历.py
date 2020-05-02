class TreeNode:
    def __init__(self, x):
        self.val = x
        self.children = None


class Solution:
    def postorder(self, root: TreeNode) -> list:
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

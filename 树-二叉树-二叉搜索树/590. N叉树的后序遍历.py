class TreeNode:
    def __init__(self, x):
        self.val = x
        self.children = None


class Solution:  # 48ms
    def postorder(self, root: TreeNode) -> list:
        """
         v1 v2 v3 v4 v5 root
        关键: 子节点以什么顺序装入栈中。顺序 v1 v2 v3 v4 v5
        出栈的顺序： root v5 v4 v3 v3 v1
        """

        if not root:
            return []
        stack, res = [root], []
        # v3 v2 v1  root v3 v2 v1
        while stack:
            root = stack.pop()
            # if root is not None:
            res.append(root.val)
            stack.extend(root.children[:])
            # for c in root.children:
            #     stack.append(c)
        return res[::-1]


class Solution1:  # 左 右 根
    def postorder(self, root: TreeNode) -> list:
        if root is None:
            return []
        # res = []
        # for c in root.children:
        #     res += self.postorder(c)
        res = [self.postorder(c) for c in root.children]
        return res + [root.val]


class Solution2:  # 左 右 根
    def postorder(self, root: TreeNode) -> list:
        #     if root is None:
        #         return []
        # res = []
        # for c in root.children:
        #     res += self.postorder(c)
        # res = [self.postorder(c) for c in root.children]
        return [self.postorder(c) for c in root.children] + [root.val] if root else []

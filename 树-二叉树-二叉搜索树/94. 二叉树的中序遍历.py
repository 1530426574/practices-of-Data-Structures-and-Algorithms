class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 迭代 DFS
class Solution:  # 32ms
    def inorderTraversal(self, root: TreeNode) -> list:
        """
        关键在哪呢？ 关键在于压入栈的顺序 ——> 弹出栈的顺序。先不断压入左子节点
        node.left -> node -> node.right
        最后一个左子节点无左子节点，所以直接输出该左子节的val,然后看该左子节点的right
        """
        res, stack = [], []  # 栈的特点 ：先进后出。
        while stack or root:
            while root:
                stack.append(root)  # 先装入根节点，然后依次找到其左子节点的左子节点。直到左子节点为None
                root = root.left
            # if not stack:
            #     return res
            root = stack.pop()  # 弹出最底层的左子节点(该节点没有左子节点，就找node.right)
            res.append(root.val)  # 该节点的值
            root = root.right  # 该节点的右字节点，左节点的右子节点 (看右子节点该节点开始进行，left，node，right)
        return res

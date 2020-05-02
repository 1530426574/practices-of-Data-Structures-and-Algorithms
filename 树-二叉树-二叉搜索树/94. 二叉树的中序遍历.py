class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#迭代
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        """
        关键在哪呢？
        node.left -> node -> node.right
        最后一个左子节点无左子节点，所以直接输出该左子节的val,然后看该左子节点的right
        """
        res, stack = [], []
        while True:
            while root:
                stack.append(root)    # 先装入根节点，然后依次找到其左子节点的左子节点。直到左子节点为None
                root = root.left
            if not stack:
                return res
            node = stack.pop()       # 弹出最底层的左子节点(该节点没有左子节点，就找node.right)
            res.append(node.val)     #
            root = node.right       # 左节点的右子节点(看右子节点该节点开始进行，left，node，right




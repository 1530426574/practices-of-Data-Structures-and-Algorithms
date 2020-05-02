# 一行胜千言！！！不明觉厉的递归
"""
递归 - 循环
通过函数体来进行的循环
"""
"""
def recursion(level, param1, param2, ...):
001 recursion terminator
    if level > MAX_LEVEL:
    process_result
    return
002 process logic in current level
    process(level, data...)
003  drill down
    self.recursion(level + 1, p1, ...)
004 restore the current level status if needed
"""


def recursion(root, level, ):
    # terminator
    if root is None:
        return []
    # process current level
    cur_val = root.val
    # dril down
    left = recursion(root.left, level - 1)
    right = recursion(root.right, level - 1)
    # restore current stauts
    return left + cur_val + right


# 不要人肉递归（最大误区）
# 最近最简方法，拆解为重复子问题
# 数学归纳法

def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []


def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []


def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def inorderTraversal(self, root: TreeNode) -> list:
        """
        关键在哪呢？
        node.left -> node -> node.right
        """
        res, stack = [], []
        while True:
            while root:
                stack.append(root)  # 先装入根节点，然后依次找到其左子节点的左子节点。直到左子节点为None
                root = root.left
            if not stack:
                return res
            node = stack.pop()  # 弹出最底层的左子节点(该节点没有左子节点，就找node.right)
            res.append(node.val)  #
            root = node.right  # 左节点的右子节点(看右子节点该节点开始进行，left，node，right

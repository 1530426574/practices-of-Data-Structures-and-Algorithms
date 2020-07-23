# 若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
# 若任意节点的右子树不空，则右子树上所有节点的值均大于或等于它的根节点的值；
# 任意节点的左、右子树也分别为二叉查找树；
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left, self.right = None, None


class Solution1:
    def isValidBST(self, root):  # root.left <root  ,root<root.right
        def valid(node, lower, upper):
            if not node:
                return True
            if lower is not None and node.val <= lower:
                return False
            if upper is not None and node.val >= upper:
                return False
            return valid(node.left, lower, node.val) and valid(node.right, node.val, upper)

        return valid(root, None, None)


class Solution3:  # 48ms
    def isValidBST(self, root):
        def valid(node, lower=float('-inf'), upper=float('inf')):
            # terminator 边界条件
            if not node:
                return True
            # handle currentr logic 处理当前逻辑层
            val = node.val
            # dril down
            if val <= lower or val >= upper:
                return False
            if not valid(node.left, lower, val):
                return False
            if not valid(node.right, val, upper):
                return False
            return True  # restore current status

        return valid(root)


class Solution2:  # 52ms
    def isValidBST(self, root):
        """
        关键在于：node.left<node<node.right  中序的顺序刚好也是这样的。
        放在一个数组里面，如果是二叉搜索树，这是一个单调递增数列。
        """
        stack, res = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            val = node.val
            if res and val <= res[-1]:  # root.left root root.right
                return False
            res.append(val)  # root.left root root.right,
            root = node.right
        return True


class Solution4:  # 52ms
    def isValidBST(self, root):
        stack, res = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            val = root.val
            if val <= res:  # root.left root root.right
                return False
            res = val
            root = root.right
        return True
        # """
        # if not stack:
        #     return res
        # node = stack.pop()       # 弹出最底层的左子节点(该节点没有左子节点，就找node.right)
        # res.append(node.val)     # 该节点的值
        # root = node.right       # 该节点的右字节点，左节点的右子节点(看右子节点该节点开始进行，left，node，right
        # # """

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left,self.right = None,None


class Solution1:
    def isValidBST(self, root):

        def helper(node,lower=float('-inf'),upper=float('inf')):
            #terminator 边界条件
            if not node:
                return True
            # handle currentr logic 处理当前逻辑层
            val = node.val
            if lower<= val <= upper:
                return True
            # dril down
            if  helper(node.right,val,upper):
                return True
            if  helper(node.left,lower,val):
                return True

            return False # restore current status

        return help(root)

class Solution2:
    def isValidBST(self, root):
        """
        关键在于：node.left,node,node.right  中序的顺序刚好也是这样的。
        放在一个数组里面，如果是二叉搜索树，这是一个单调递增数列。
        """
        stack,res = [],[]
        while True:
            while root:
                stack.append(root)
                root = root.left

            node = stack.pop()
            val = node.val
            if res and val< res[-1]:  # root.left root root.right
                return False
            res.append(val)   # root.left root root.right,
            root = node.right






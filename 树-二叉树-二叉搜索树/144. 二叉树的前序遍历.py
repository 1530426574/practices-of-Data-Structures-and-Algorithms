class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left, self.right = None, None


class Solution:  # 36ms
    def preorderTraversal(self, root: TreeNode) -> list:
        """
        关键在哪呢？“压栈“顺序，先压right，再压left，这样先弹出left,再弹出right
        循环，自相似性，重复子问题。 root root.left root.right
        先从栈中弹出根节点，然后依次向栈中加入其右孩子节点，然后是做孩子节点
        """
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            if root:  # Nonetype object dose not have value
                res.append(root.val)
                stack.append(root.right)
                stack.append(root.left)
        return res


"""
输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [1,2,3]
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:  # 76ms
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right


class Solution2:  # 76ms
    def lowestCommonAncestor1(self, root, p, q):
        """
        关键在于树的遍历，
        001 可以一边遍历一遍保存深度，从而比较深度
        002 可以一边遍历一边遍历进行翻转
        003 也可以一边遍历一遍判断root root.left, root.right 的关系大小，来判别是否是二叉搜索树
        004 也可以一遍遍历一遍保存节点和节点的属性(level,find_parent,left,right)
        遍历完所有节点后，
        """

        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:  # ==   (root == p) or (root == q):
            node = stack.pop()
            if node.left:  # 为什么是node.left,因为下面要node.left充当了key
                parent[node.left] = node
                stack.append(node.left)
            if node.right:  # 为什么是node.right,
                parent[node.right] = node
                stack.append(node.right)  # 遍历完所有节点，并且保存到了字典中了，node:node.find_parent
        ancestors = set()
        while p:  # 先把p,p.parents全部放入一个集合中
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:  # q,q.parents 去里面找。
            q = parent[q]
        return q


"""
最近公共祖先的定义为：
“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）

具体思路：
（1） 如果当前结点 root 等于NULL，则直接返回NULL
（2） 如果 root等于 p或者 q ，那这棵树一定返回 p 或者 q
（3） 然后递归左右子树，因为是递归，使用函数后可认为左右子树已经算出结果，用 left 和 right 表示
（4） 此时若left为空，那最终结果只要看 right；若 right 为空，那最终结果只要看 left
（5） 如果 left 和 right 都非空，因为只给了 p和q 两个结点，都非空，说明一边一个，因此 root 是他们的最近公共祖先
（6） 如果 left 和 right 都为空，则返回空（其实已经包含在前面的情况中了）

链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
"""

"""
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
"""
# root root.left root.right
preorder = [1, 2, 4, 5, 3, 6, 7]
# root.left root root.right
inorder = [4, 2, 5, 1, 6, 3, 7]  # 1


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left, self.right = None, None


class Solution:
    def buildTree(self, preorder, inorder):  # 不管是那种遍历，都可以分为三大块，root,  root.left, root.right
        if inorder:  # 本质还是在遍历中序节点，从中序节点里构造二叉树，先找到根在中序里的位置（索引）。
            ind = inorder.index(preorder.pop(0))  # pop很重要，先pop: root  root.left  root.right
            root = TreeNode(inorder[ind])  # 为什么要在中序里找到根的索引
            root.left = self.buildTree(preorder, inorder[0:ind])  # 中序确定左子树的遍历范围
            root.right = self.buildTree(preorder, inorder[ind + 1:])  # 中序确定右子树的遍历范围
            return root



# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
#  注意:
# 你可以假设树中没有重复的元素。
#
#  例如，给出
#
#  前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
#
#  返回如下的二叉树：
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  Related Topics 树 深度优先搜索 数组


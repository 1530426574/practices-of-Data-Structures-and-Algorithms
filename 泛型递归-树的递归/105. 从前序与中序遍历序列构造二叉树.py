"""
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
"""
# root root.left root.right
preorder = [3,9,20,15,7]
# root.left root root.right
inorder = [9,3,15,20,7]  #1

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left,self.right = None,None

class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root

"""
参考链接
树的遍历 Demo https://visualgo.net/zh/bst
实战题目 / 课后作业
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/
https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/
https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/
"""
"""
二叉树中任意一个节点的左右子树的高度相差不能大于 1。
"""

"""
二叉查找树要求，在树中的任意一个节点，
其左子树中的每个节点的值，都要小于这个节点的值， node.left<node<node.right
而右子树节点的值都大于这个节点的值
"""
"""
前序遍历是指，node -> node.left -> node.right
对于树中的任意节点来说，
先打印这个节点，
然后再打印它的左子树，
最后打印它的右子树。"""

"""
中序遍历是指，  node.left -> node -> node.right
对于树中的任意节点来说，
先打印它的左子树， node.left
然后再打印它本身，node
最后打印它的右子树。node.right
"""

"""
后序遍历是指，node.left -> node.right -> node
对于树中的任意节点来说，
先打印它的左子树，node.left
然后再打印它的右子树，node.right
最后打印这个节点本身。node
"""
"""
前序遍历的递推公式：
preOrder(r) = print r->preOrder(r->left)->preOrder(r->right)

中序遍历的递推公式：
inOrder(r) = inOrder(r->left)->print r->inOrder(r->right)

后序遍历的递推公式：
postOrder(r) = postOrder(r->left)->postOrder(r->right)->print r
"""
"""
想要存储一棵二叉树，我们有两种方法，
一种是基于指针或者引用的二叉链式存储法，
一种是基于数组的顺序存储法。
"""

"""
 递归指的是调用自己的函数。
 每个递归函数都有两个条件：基线条件和递归条件。
 栈有两种操作：压入和弹出。
 所有函数调用都进入调用栈。
 调用栈可能很长，这将占用大量的内存。
"""

"""
实战题目
https://leetcode-cn.com/problems/climbing-stairs/
https://leetcode-cn.com/problems/generate-parentheses/
https://leetcode-cn.com/problems/invert-binary-tree/description/
https://leetcode-cn.com/problems/validate-binary-search-tree
https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
每日一课
如何优雅地计算斐波那契数列
https://time.geekbang.org/dailylesson/detail/100028406
课后作业
https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
https://leetcode-cn.com/problems/combinations/
https://leetcode-cn.com/problems/permutations/
https://leetcode-cn.com/problems/permutations-ii/
"""

"""
宽度优先搜索（BFS）

我们按照高度顺序一层一层的访问整棵树，高层次的节点将会比低层次的节点先被访问到。

深度优先搜索（DFS）

在这个策略中，我们采用深度作为优先级，以便从跟开始一直到达某个确定的叶子，然后再返回根到达另一个分支。

深度优先搜索策略又可以根据根节点、左孩子和右孩子的相对顺序被细分为前序遍历，中序遍历和后序遍历

"""

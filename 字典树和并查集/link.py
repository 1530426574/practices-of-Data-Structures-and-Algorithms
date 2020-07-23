"""
实战题目
https://leetcode-cn.com/problems/implement-trie-prefix-tree/#/description
https://leetcode-cn.com/problems/word-search-ii/
分析单词搜索 2 用 Tire 树方式实现的时间复杂度，请同学们提交在第 6 周的学习总结中
参考链接
岛屿数量
并查集代码模板
实战题目
https://leetcode-cn.com/problems/friend-circles
https://leetcode-cn.com/problems/number-of-islands/
https://leetcode-cn.com/problems/surrounded-regions/
"""
# 并查集常用来解决连通性的问题，即将一个图中连通的部分划分出来。
# 并查集的思想就是，同一个连通区域内的所有点的根节点是同一个。
# 将每个点映射成一个数字。
# 先假设每个点的根节点就是他们自己，然后我们以此输入连通的点对，
# 然后将其中一个点的根节点赋成另一个节点的根节点，这样这两个点所在连通区域又相互连通了

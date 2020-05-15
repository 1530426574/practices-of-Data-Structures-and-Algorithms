class  TreeNode:
    def __init__(self,x):
        self.val = x
        self.left,self.right =None,None
#递归

#首先最核心的代码还是树节点的遍历，深度优先遍历和广度优先遍历，这道题的关键在于，怎么判断和存储每一层的节点

class Solution:#40ms
    def levelOrder(self, root: TreeNode) -> list:      #递归的本质就是调用自身函数，函数的本质就是压栈与出栈。
        def dfs(root,level):
            if not root:                #001 terminator
                return
            if len(res)<level:          #002  process current level
                res.append([])    #最关键的！！！！

            res[level-1].append(root.val)

            dfs(root.left,level+1)     #003 dril down
            dfs(root.right,level+1)
                                      #004 reverse  the curreent status if needed
        res = []
        dfs(root,1)
        return res

#DFS，preorder
class Solution1:#44ms
    def levelOrder(self, root: TreeNode) -> list:
        """
        关键在哪呢？？？访问节点的时候，节点的层数是知道的，
        因为根节点的层数是1，所以子节点的层数自然在遍历的过程也是知道的。
        以终为始，相当于构建n个盒子，每个盒子存放每层的节点值。
        001 每个节点对应着相应的层
        002 不管是BFS还是DFS(preorder)，都是逐层遍历
        003 所以在遍历的过程中，一边dirl down，一边创建存储该层节点值的列表，
        一边把刚好遍历到该节点的值，根据其层数，添加到 对应的列表中，
        004 我一直在纠结压栈出栈，或者进队或者出队这样的细节，忘了他们这样做的目的->访问顺序。
        """

        if not root:
            return []
        res, stack = [], [(root, 1)]
        while stack:
            root, level = stack.pop()
            if root:
                if len(res) < level:
                    res.append([])
                res[level - 1].append(root.val)
                stack.append((root.right, level + 1))
                stack.append((root.left, level + 1))
        return res
        # DFS + stack I

    def levelOrder2(self, root):#40ms
        if not root:
            return []
        res, stack = [], [(root, 0)]
        while stack:
            root, level = stack.pop()
            if len(res) < level + 1:
                res.append([])
            res[level].append(root.val)
            if root.right:
                stack.append((root.right, level + 1))
            if root.left:
                stack.append((root.left, level + 1))
        return res


class Solution2:#48ms
    def levelOrder(self, root: TreeNode) -> list:
        res, queue = [], [(root, 0)]
        while queue:
            root, level = queue.pop(0)
            if root:
                if len(res) < level + 1:
                    res.append([])
                res[level].append(root.val)
                queue.append((root.left, level + 1))
                queue.append((root.right, level + 1))

        return res
    # BFS + deque
    def levelOrder2(self, root):#44ms
        from collections import deque
        res, queue = [], deque([(root, 0)])
        while queue:
            curr, level = queue.popleft()
            if curr:
                if len(res) < level + 1:
                    res.append([])
                res[level].append(curr.val)
                queue.append((curr.left, level + 1))
                queue.append((curr.right, level + 1))
        return res





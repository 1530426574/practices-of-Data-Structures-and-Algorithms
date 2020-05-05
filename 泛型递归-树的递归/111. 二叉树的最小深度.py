class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left,self.right =  None,None
        self.children = None



#recursion 80ms
class Solution1:
    def minDepth(self, root:TreeNode):
        if  not root:
            return 0

        if not root.left or not root.right: # root,left is None and root.right is None
            return 1 + max(self.minDepth(root.left),self.minDepth(root.right))

        return 1 + min(self.minDepth(root.left),self.minDepth(root.right))


#DFS 64ms
class Solution2:
    def minDepth(self, root):
        if not root:
            return 0

        stack = [(root, 1)]
        min_dep = float('inf')
        while stack:
            root, depth = stack.pop()
            if root:
                if not root.left and not root.right:
                    min_dep = min(depth, min_dep)
                stack.append((root.left, depth + 1))
                stack.append((root.right, depth + 1))
        return min_dep
#BFS 48ms
class Solution3:
    def minDepth(self, root):
        if not root:
            return 0
        from collections import deque
        q = deque([(root, 1)])
        while q:
            node, level = q.popleft()
            if node:
                if not node.left and not node.right:
                    return  level
                q.append((node.left, level + 1))
                q.append((node.right, level + 1))

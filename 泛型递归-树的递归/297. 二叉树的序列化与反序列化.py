class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left,self.right = None,None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return 'None'
        return root.val, self.serialize(root.left), self.serialize(root.right)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root


class Codec1:
    def serialize(self, root):
        # take care of base cases
        # if a node is empty, add 'x' to string
        # you can set 'x' to any mark as you want
        if not root: return 'x'
        # preoder(Root->left->right)
        # ex,
        #     1
        #    / \
        #   2   3
        #      / \
        #     4   5
        #
        # return (1, (2, 'x', 'x'), (3, (4, 'x', 'x'), (5, 'x', 'x')))
        # if you look at the return statement very closely, it is actually very intuitive
        # for value 1, you have 2 as left child and 3 as right child
        # for value 2, you have 'x'(None) as left child and 'x'(None) as right child which indicates it is a leaf node
        return root.val, self.serialize(root.left), self.serialize(root.right)

    def deserialize(self, data):
        #######################INTUITION#########################
        # The initial data string will be something like below:
        # (1, (2, 'x', 'x'), (3, (4, 'x', 'x'), (5, 'x', 'x')))
        # if you loop through string:
        # 1                                 -> this is node value
        # (2, 'x', 'x')                     -> this is node left
        # (3, (4, 'x', 'x'), (5, 'x', 'x')) -> this is node right
        ########################################################
        # always take care of base case: if the node's value is 'x' then return None
        if data[0] == 'x': return None
        # create new treenode for node value
        node = TreeNode(data[0])
        # do the recursive to unpack string value
        node.left = self.deserialize(data[1])
        node.right = self.deserialize(data[2])
        # return the new TreeNode that we just created

    def serialize1(self, root):
        if not root: return 'x'
        return root.val, self.serialize(root.left), self.serialize(root.right)


    def deserialize1(self, data):
        if data[0] == 'x': return None
        node = TreeNode(data[0])
        node.left = self.deserialize(data[1])
        node.right = self.deserialize(data[2])
        return node

#Returning string instead of tuple.
class Codec2:
    def serialize(self, root):
        if not root: return 'x'
        return ','.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])

    def deserialize(self, data):
        self.data = data   #self.data 而不是data，self.data 会一直发生变化。omg。
        if data[0] == 'x': return None
        node = TreeNode(self.data[:self.data.find(',')])
        node.left = self.deserialize(self.data[self.data.find(',') + 1:])
        node.right = self.deserialize(self.data[self.data.find(',') + 1:])
        return node




"""
序列化是将一个数据结构或者对象转换为连续的比特位的操作，
进而可以将转换后的数据存储在一个文件或者内存中，
同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
广度优先搜索（BFS）
我们按照高度的顺序从上到下逐级扫描树。更高级别的节点将先于较低级别的节点访问。
深度优先搜索（DFS)
在这个策略中，我们采用深度作为优先顺序，这样我们就可以从一个根开始，一直延伸到某个叶，然后回到根，到达另一个分支。
根据根节点、左节点和右节点之间的相对顺序，可以进一步将DFS策略区分为 preorder、inorder 和 postorder 。

"""


# Deserialization
class Codec3:

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root


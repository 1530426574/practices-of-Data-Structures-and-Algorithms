# 一行胜千言！！！不明觉厉的递归
"""
递归 - 循环
通过函数体来进行的循环
"""
"""
def recursion(level, param1, param2, ...):
    001 recursion terminator
        if level > MAX_LEVEL:
            process_result
            return
    002 process logic in current level
        process(level, data...)
    003  drill down
        self.recursion(level + 1, p1, ...)           #函数压栈的过程
    004 reverse the current level status if needed
"""


def recursion(root, level, ):
    # terminator
    if root is None:
        return []
    # process current level
    cur_val = root.val
    # dril down
    left = recursion(root.left, level - 1)
    right = recursion(root.right, level - 1)
    # restore current stauts
    return left + cur_val + right

#函数：输入什么，返回什么，里面怎么实现，我不管。

# 不要人肉递归（最大误区）
# 最近最简方法，拆解为重复子问题
# 数学归纳法
#递归的关键在于找关系，就好像找f(n)=f(n-1)+1 ,找重复性，找递推公式。

def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []


def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []


def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []



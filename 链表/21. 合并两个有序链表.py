class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        # l1 : 0 2 4 6
        # l2: 1 3 5 7 9 11 13
        """
        关键在哪呢？递归真是服了。。。。捂脸
        递归的前提是 重复子问题 ，并且假设已经知道结果了。
        传进去的是啥，最后返回值是啥？
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:  # l1 : 1 2 3 4 5 6      #l2 : 7 8 9 10 11 12
            # 进入这一步,意味着l1.val更小,需要指定  l1.next
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1  # l1 l2 l2.next ->l1.next
        else:
            # l2 更小,需要指定它的下一节点，即      l2.next
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2


class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        """
        关键在哪？？？有个哨兵站着问下一个是谁呢（判断依据是谁小谁先上。）
        001 关键在于找到哨兵节点pre的next是l1和l2中的哪个 pre.next = l1 ??? l2
        002 找到next之后，就继续寻找next的next 会是剩下的l1和l2中的哪个（—循环遍历）
        003 相当于重新生成了一个新的链表链接了。
        """
        prehead = ListNode(-1)
        pre = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                pre.next = l1
                pre = l1
                l1 = l1.next
            else:
                pre.next = l2
                pre = l2
                l2 = l2.next
        pre.next = l2 if l1 is None else l1

        return prehead.next

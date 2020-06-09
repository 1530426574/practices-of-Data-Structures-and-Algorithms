class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        #关键在哪？？？两两交换指的是什么意思？？？
        关键在于添加一个哨兵，保存b.next
        pre -> a -> b -> b.next       ==>
        pre -> b -> a -> b.next
        Here, pre is the previous node.
        Since the head doesn't have a previous node,
        I just use self instead.
        Again, a is the current node and b is the next node.
        To go from pre -> a -> b -> b.next to pre -> b -> a -> b.next,
        we need to change those three references.
        Instead of thinking about in what order I change them,
        I just change all three at once.
        https://leetcode-cn.com/problems/swap-nodes-in-pairs/submissions/
        """
        dumy = ListNode(0)
        pre, pre.next = dumy, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return dumy.next


# 递归
class Solution1:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :param head:
        :return:
        从链表的头节点 head 开始递归。
        每次递归都负责交换一对节点。由 firstNode 和 secondNode 表示要交换的两个节点。
        下一次递归则是传递的是下一对需要交换的节点。若链表中还有节点，则继续递归。
        交换了两个节点以后，返回 secondNode，因为它是交换后的新头。
        在所有节点交换完成以后，我们返回交换后的头，实际上是原始链表的第二个节点
        """
        if head is None or head.next is None:      # terminator
            return head

        first = head                               # process current logical
        second = head.next
        # Swapping   1 -> 2 -> 3 -> 4     =>   2->1->3->4
        first.next = self.swapPairs(second.next)   # dril down
        second.next = first
        # Now the head is the second node
        return second                              # restore cur status
#重复子问题
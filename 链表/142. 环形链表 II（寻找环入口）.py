class ListNode:
    def __init__(self,x):
        self.val =x
        self.next =None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        关键在哪呢？？？ 索引查找
        001 在条件判断上还不是很清晰
        :param head:
        :return:
        """
        s = set()
        while head:
            if head in s:
                return head
            s.add(head)
            head = head.next

class Solution1(object):
    def detectCycle(self, head):
        """

        :param head:
        :return:
        """
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
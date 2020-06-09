class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def hasCycle(self, head: ListNode) -> bool:
        """
        关键在哪呢？？？
        1->2->3>4->2
        在遍历一遍后并把节点存在集合中：
        如果最后一个节点是null，说明没有环，返回False
        如果不是null,而且最后一个节点的next还能在集合中找到，说明有环了。
        :param head:
        :return:
        """
        s = set()    #很神奇的方法
        while head:
            if head not in s:
                s.add(head)
                head = head.next
            else:
                return True
        return False


class Solution2:
    def hasCycle(self, head: ListNode) -> bool:
        if not (head and head.next):
            return False
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

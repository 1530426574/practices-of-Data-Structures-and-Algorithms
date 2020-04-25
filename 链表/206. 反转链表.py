class ListNode:
    def __init__(self,x):
        self.val =x
        self.next =None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """

        关键在哪呢???    cur.next -> pre   cur.next = pre
        改变当前节点(cur)的指针指向上一个节点（pre)，同时保存当前节点的下一个节点(next)
        Assume that we have linked list  1 → 2 → 3 → NULL
        we would like to change it to   NULL ← 1 ← 2 ← 3
        While you are traversing the list,
        change the current node's next pointer to point to its previous element.
        Since a node does not have reference to its previous node,
        you must store its previous element beforehand.
        You also need another pointer to store the next node before changing the reference.
        Do not forget to return the new head reference at the end!
        https://leetcode.com/problems/reverse-linked-list/
        """
        pre  = None
        while head is not None:
            next = head.next
            head.next  = pre
            pre = head
            head = next
        return pre

class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        pre  = None
        cur = head
        while cur :             #1 → 2 → 3 → NULL
            next = cur.next     #NULL ← 1 ← 2 ← 3
            cur.next = pre
            pre = cur
            cur = next

        return pre
#封装与解构
class Solution3:
    def reverseList(self, head: ListNode) -> ListNode:
        pre  = None
        while head is not None:
            next,head.next = head.next,pre
            pre,head = head,next
        return pre



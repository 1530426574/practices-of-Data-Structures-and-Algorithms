class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution1:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        关键在哪呢，链表翻转以后，如何把他们首尾相连呢？
        001 链表的本质：链接的是一个个分散的对象。不是变量或者标识符。
        002 需要知道，翻转链表的首，尾，以及尾的下一个节点。
        003 一个对象可以被多个变量引用
        l, r : define reversing range
        pre, cur : used in reversing, standard reverse linked linked list method
        jump : used to connect last node in previous k-group to first node in following k-group
        https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
        """
        dumpy = jump = ListNode(0)
        dumpy.next = l = r = head
#       dumpy->1->2->3->4->5->6 ->7->8->9->10
#       j->3 -> 2-> 1 -> 6 -> 5 -> 4
        while True:
            #遍历出4
            count = 0
            while r and count <k:
                count +=1     # (1,head) (2,2）（3,3）（4,4）(5,5)(5,None)    2
                r = r.next
            if count==k :
                # dumpy -> 1 -> 2 -> 3 -> 4 -> 5
                # pre,cur = r.next,l #(4,1) #(7,4)
                pre = r
                cur = l
                for _ in range(k):
                    next = cur.next
                    cur.next = pre
                    pre = cur
                    cur = next
                # pre = self.reverse_link_list(cur, k, pre)
                jump.next = pre
                #理解这步的关键在于，理解链表的本质，将一个个不连续，分散的对象链接在一起。一切皆对象，链表链接的是一个个对象（节点对象），链表的特点是
                jump = l  # jump =1
                l = r   # l = 4 l =7
            else:
                return dumpy.next




#明确翻转的链表范围
    def reverse_link_list(self, cur, k, pre):
        for _ in range(k):
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next  # pre =3,cur =4
        return pre


    def reverse_link_list1(self,cur:ListNode,pre:ListNode):
        while cur:
            next= cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre




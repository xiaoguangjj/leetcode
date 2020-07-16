# -*- coding:utf-8 -*-

"""
回文链表
请判断一个链表是否为回文链表。
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverst(self, head):
        a = head
        b = head.next
        head.next = None

        while b:
            c = b.next
            b.next = a
            a = b
            b = c
        head = a
        return head

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow = slow.next
        slow = self.reverst(slow)
        while slow:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next
        return True

if __name__=='__main__':
    head1 = ListNode(0) #加上就有头节点，去掉就没有头节点
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(2)
    n4 = ListNode(1)

    head1.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    print(Solution().isPalindrome(n1))  # 以谁为头，就填写谁
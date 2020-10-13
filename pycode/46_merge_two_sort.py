# -*- coding:utf-8 -*-

"""
合并两个有序链表
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newHead = ListNode(0)
        pre = newHead
        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        if l1:
            pre.next = l1
        elif l2:
            pre.next = l2
        return newHead.next


if __name__ == '__main__':
    # 有序链表
    head1 = ListNode(2)
    n1 = ListNode(3)
    n2 = ListNode(4)
    n3 = ListNode(9)
    head1.next = n1
    n1.next = n2
    n2.next = n3

    # 有序链表
    head2 = ListNode(3)
    m1 = ListNode(5)
    m2 = ListNode(7)
    m3 = ListNode(8)
    head2.next = m1
    m1.next = m2
    m2.next = m3

    s = Solution()
    res = s.mergeTwoLists(head1, head2)
    res_list = []
    while res:
        res_list.append(res.val)
        res = res.next
    print(res_list)

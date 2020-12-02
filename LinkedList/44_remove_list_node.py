# -*- coding:utf-8 -*-

"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。
"""


class Node(object):
    '''
    节点类
    '''

    def __init__(self, data):
        self.num = data
        self.next = None

    def print_node(self, node):
        res_list = []
        while node:
            res_list.append(str(node.num))
            node = node.next
        print('->'.join(res_list))


class Solution:
    def removeNthFromEnd(self, head, n):
        h = Node(0)
        h.next = head
        before_node, back_node = h, h

        for _ in range(n + 1):
            before_node = before_node.next

        while before_node != None:
            before_node = before_node.next
            back_node = back_node.next

        back_node.next = back_node.next.next
        return h.next


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    # node6 = Node(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print('init single linknode is:')
    node1.print_node(node1)
    node2.print_node(node1)
    node3.print_node(node1)
    # node5.print_node(node1)
    # node5.print_node(node1)
    print(Solution().removeNthFromEnd(node1, 4))
    node4.print_node(node1)

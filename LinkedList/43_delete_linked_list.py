# -*- coding:utf-8 -*-

"""
删除链表中的节点
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

现有一个链表 -- head = [4,5,1,9]，它可以表示为:

4 -> 5 -> 1 -> 9

示例 1:

输入: head = [4,5,1,9], node = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
"""


class Node(object):
    """
    节点类
    """
    def __init__(self, data):
        self.num = data
        self.next = None


class DeleteNode:
    """
    实现删除指定节点功能
    """
    def delete_node(self, node):
        node.num = node.next.num
        node.next = node.next.next


class PrintNode:
    """
    输出指定节点为起始节点的链表
    """
    def print_node(self, node):
        res_list = []
        while node:
            res_list.append(str(node.num))
            node = node.next
        print('->'.join(res_list))


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print('init single linknode is:')
    printnode = PrintNode()
    printnode.print_node(node1)
    delete = DeleteNode()
    delete.delete_node(node4)
    print('after delete node,the single linknode is:')
    printnode.print_node(node1)
    node5.next = node6
    print('add node,the single linknode is:')
    printnode.print_node(node1)

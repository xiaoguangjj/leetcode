"""
24. 两两交换链表中的节点
难度：中等

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。



示例 1：
1->2->3->4
    |
    ∨
2->1->4->3


输入：head = [1,2,3,4]
输出：[2,1,4,3]
示例 2：

输入：head = []
输出：[]
示例 3：

输入：head = [1]
输出：[1]


提示：

链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 功能：建表
    def cre_link(self, data):
        self.head = ListNode(data[0])
        phead = self.head
        for i in data[1:]:
            node = ListNode(i)
            phead.next = node
            phead = phead.next
        return phead

    # 功能：遍历输出链表
    def traveling(self):
        tmp = self.head
        list1 = []
        while tmp != None:
            list1.append(tmp.val)
            tmp = tmp.next
        return list1

    # 功能：两两交换链表中的元素
    def swapPairs(self, head):
        dummyHead = ListNode(0)
        dummyHead.next = head
        temp = dummyHead
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return dummyHead.next


if __name__ == '__main__':
    ll = Solution()
    data = [1, 2, 3, 4]
    phead = ll.cre_link(data)
    print(ll.traveling())  # 创建完列表，遍历
    print(ll.swapPairs(phead))
    print(ll.traveling())  # 互换链表后遍历

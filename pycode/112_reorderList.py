"""
143. 重排链表
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

"""


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

    # 功能：重排链表
    # solution: 链表不能访问下标，所以，先将链表储存在线性表中，然后重建单链表。
    def reorderList(self, head):
        if not head:
            return

        vec = list()  # 创建列表
        node = head
        while node:  # 把链表中的值，储存到列表中
            vec.append(node)
            node = node.next

        i, j = 0, len(vec) - 1
        while i < j:    # 重构链表
            vec[i].next = vec[j]
            i += 1
            if i == j:
                break
            vec[j].next = vec[i]
            j -= 1
        vec[i].next = None
        return vec


if __name__ == "__main__":
    ll = Solution()
    data = [1, 2, 3, 4, 5]
    phead = ll.cre_link(data)
    vec = ll.reorderList(phead)
    # print(ll.traveling())  # 创建完列表，遍历

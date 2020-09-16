"""
83. 删除排序链表中的重复元素
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 功能：建表
    def cre_link(self, data):
        self.head = ListNode(data[0])
        phead = self.head
        for i in data[1:]:
            node = ListNode(i)
            phead.next = node
            phead =phead.next
        return phead

    # 功能：删除单链表中重复的值
    # 注意是排序链表

    def deleteDuplicates(self):
        node = self.head                 # 记住链表头的位置
        while node and node.next:
            if node.val == node.next.val:   # 遇到相同的两项，删掉
                node.next = node.next.next
            else:                           # 遇到不同的两项，过
                node = node.next
        return self.head         # 返回链表头的位置

    # 功能：遍历输出链表
    def traveling(self):
        tmp = self.head
        list1 = []
        while tmp != None:
            list1.append(tmp.val)
            tmp = tmp.next
        return list1


if __name__ == "__main__":
    ll = Solution()
    data = [1, 1, 2, 3, 3]
    phead = ll.cre_link(data)
    print(ll.traveling())  # 创建完列表，遍历
    ll.deleteDuplicates()
    print(ll.traveling())   # 删除完列表，遍历

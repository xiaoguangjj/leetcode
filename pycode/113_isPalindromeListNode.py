"""
234. 回文链表
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 创建链表
    def cre_link(self, data):
        self.head = ListNode(data[0])  # 第一个值 赋值给链表头
        phead = self.head
        for i in data[1:]:
            node = ListNode(i)
            phead.next = node
            phead = phead.next
        return self.head

    # 遍历链表
    def traveling(self):
        tmp = self.head
        list1 = []
        while tmp != None:
            list1.append(tmp.val)
            tmp = tmp.next
        return list1

    # 判断单链表是否是回文链表
    def isPalindrome(self, head):
        vec = list()
        node = head
        while node:
            vec.append(node.val)
            node = node.next
        if vec == vec[::-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    val = [1, 2, 2, 1]
    s = Solution()
    head = s.cre_link(val)
    print(s.traveling())
    print(s.isPalindrome(head))

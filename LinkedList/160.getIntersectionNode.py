"""
160. 相交链表
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

图示两个链表在节点 c1 开始相交：



题目数据 保证 整个链式结构中不存在环。

注意，函数返回结果后，链表必须 保持其原始结构 。



示例 1：



输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
示例 2：



输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'
解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
示例 3：



输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
这两个链表不相交，因此返回 null 。


提示：

listA 中节点数目为 m
listB 中节点数目为 n
0 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA <= m
0 <= skipB <= n
如果 listA 和 listB 没有交点，intersectVal 为 0
如果 listA 和 listB 有交点，intersectVal == listA[skipA + 1] == listB[skipB + 1]


进阶：你能否设计一个时间复杂度 O(n) 、仅用 O(1) 内存的解决方案？

https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/chi-xiao-dou-python-tu-wen-xiang-jie-by-j7tyi/
"""

"""
双指针法：
解题思路
这道题目让求两个链表相交的节点, 利用双指针法 O(m+n)O(m+n) 就可以遍历完成
这道题目的思想是让 aa, bb 指针都走一遍 headAheadA, headBheadB 两个链表, aa, bb 相遇的地方就是两个链表相交的地方.

aa 指向 headAheadA, 一步一步往 next 走, 走到结尾 null 时, 跳到 headBheadB 继续往后遍历
bb 指针跟 aa 一样的, 只不过先遍历 headBheadB, 到结尾了再跳到 headAheadA
为什么 a, b 会在交点相遇
假设headA, headB是有交点的, 他们整个移动的路径像一个 8 字. 我觉得这个有点像莫比乌斯环~, 两个指针的起始位置虽然不一样, 但是大家的走的步伐是一致的, 而且朝着相交的点在移动, 于是可以相遇. 画一个图来理解一下可能更加清晰.

作者：niconiconi-12
链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/chi-xiao-dou-python-tu-wen-xiang-jie-by-j7tyi/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回相交的位置。双链表法，思路：让 aa, bb 指针都走一遍 headAheadA, headBheadB 两个链表, aa, bb 相遇的地方就是两个链表相交的地方.
    # 时间复杂度 O(m+n), m, n 分别为两个链表的节点数
    # 空间复杂度O(1)
    def getIntersectionNode(self, headA, headB):
        a, b = headA, headB
        while a != b:
            if a:
                a = a.next
            else:
                a = headB

            if b:
                b = b.next
            else:
                b = headA

        return a
    # 判断是否相交，两个链表。一个链表先取出来值，另一个链表判断是否存在其中
    # 时间复杂度O(n)
    # 空间复杂度O(n)
    def getIntersectionNode_(self, headA, headB):
        s = set()
        p, q = headA, headB
        while p:
            s.add(p)
            p = p.next
        while q:
            if q in s:
                return q
            q = q.next
        return None


if __name__=="__main__":
    intersectVal = 8
    listA = [4, 1, 8, 4, 5]
    listB = [5, 0, 1, 8, 4, 5]
    skipA = 2
    skipB = 3


/*
2. 两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

*/
package main

import "fmt"

/*
 * Definition for singly-linked list.
*/

type ListNode struct {
	Val int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode)*ListNode{
	headList := new(ListNode)
	head := headList
	num := 0

	for (l1 != nil || l2 != nil || num > 0){
		headList.Next = new(ListNode)
		headList = headList.Next
		if l1 != nil{
			num = num + l1.Val
			l1 = l1.Next
		}
		if l2 != nil{
			num = num + l2.Val
			l2 = l2.Next
		}
		headList.Val = (num) % 10
		num = num / 10
	}
	return head.Next
}

func  main() {
	l1 := [5]int{2, 4, 3}
	l2 := [5]int{5, 6, 4}
	fmt.Printf("链表求和：%d\n",addTwoNumbers(&l1, &l2))
}
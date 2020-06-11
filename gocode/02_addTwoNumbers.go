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

import (
	"fmt"
)

/*
 * Definition for singly-linked list.
*/

type ListNode struct {
	Val int
	Next *ListNode
}

// 生成头节点
func New() *ListNode {
	//下面的Val可以用来表示链表的长度
	return &ListNode{0, nil}
}

//在链表的第i个位置前插入一个元素e，复杂度为o(n)
func (head * ListNode) Insert(i int, e int) bool{
	p := head
	j := 1
	for nil != p && j < i{
		p = p.Next
		j++
	}
	if nil == p || j > i {
		fmt.Println("pls check i:", i)
		return false
	}
	s := &ListNode{Val:e}
	s.Next = p.Next
	p.Next = s
	return true
}

// 遍历链表
func (head *ListNode) traverse(){
	point := head.Next
	for nil != point{
		fmt.Println(point.Val)
		point = point.Next
	}
	fmt.Println("-----------done----------")
}
func  main() {
	l1 := New()
	l1.Insert(1, 3)
	l1.Insert(1, 4)
	l1.Insert(1, 2)
	l1.traverse()
	l2 := New()
	l2.Insert(1, 4)
	l2.Insert(1, 6)
	l2.Insert(1, 5)
	l2.traverse()

	result := addTwoNumbers(l1, l2)
	result.traverse()
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

//next 进入l的下一位。
func next(l *ListNode)*ListNode{
	if l != nil {
		return l.Next
	}
	return nil
}

func add(n1, n2 *ListNode, i int)(v, n int)  {
	if n1 != nil{
		v += n1.Val
	}

	if n2 != nil {
		v += n2.Val
	}

	v += i

	if v > 9 {
		v -= 10
		n = 1
	}
	return
}

"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

 

示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：

1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用

在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value):
        self.A.append(value)

    def deleteHead(self):
        if self.B:
            return self.A.pop()
        if not self.A:
            return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()


if __name__ == "__main__":
    B = [[],[3],[],[],[]]
    c = CQueue()
    c.appendTail(3)
    c.deleteHead()
    c.deleteHead()
    c.deleteHead()


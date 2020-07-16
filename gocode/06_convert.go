/*
6. Z 字形变换
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
*/

package main

import "fmt"

func convert(s string, numRows int) string{
	//不满足，提前返回
	if numRows < 2{
		return s
	}
	// 保存最终结果
	var res string
	//保存每次的结果
	var tmp = make([]string, numRows)
	//初始位置
	curPos := 0
	//用来标志是否该转向了
	shouldTurn := -1
	// 遍历每个元素
	for _, val := range s {
		//添加进tmp 里面，位置为curPos
		tmp[curPos] += string(val)
		//如果走到头或者尾，就该转向了
		//因为就在numRows的长度里面左右震荡
		if curPos == 0 || curPos == numRows-1 {
			//转向
			shouldTurn = - shouldTurn
		}
		// curPos 用来标记tmp里面我们该去哪个位置
		curPos += shouldTurn
	}
	// 这时tmp里面已经保存了数据了，我们只需要转换一下输出格式
	for _, val := range tmp{
		res += val
	}
	//最后的输出
	return res
}


func main() {
	s := "LEETCODEISHIRING"
	numRows := 3
	fmt.Printf("res: %s\n", convert(s, numRows))
}
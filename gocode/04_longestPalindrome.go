/*
5. 最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
*/

//本题采用动态规划的方法

package main

import "fmt"



func longestPalindrome(s string) string{
	n := len(s)
	ans := ""
	dp := make([][]int, n)
	for i:= 0; i < n; i++ {
		dp[i] = make([]int, n)
	}
	for l := 0; l < n; l++{
		for i:= 0; i + l < n; i++{
			j := i + l
			if l == 0 {
				dp[i][j] = 1
			} else if l == 1 {
				if s[i] == s[j] {
					dp[i][j] = 1
				}
			}else {
				if s[i] == s[j] {
					dp[i][j] = dp[i+1][j-1]
				}
			}
			if dp[i][j] > 0 && l + 1 > len(ans) {
				ans = s[i:i+l+1]
			}
		}
	}
	return ans
}

func main(){
	s := "babad"
	re := longestPalindrome(s)
	fmt.Printf("%s\n",re)
}

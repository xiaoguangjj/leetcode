"""
22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：

输入：n = 1
输出：["()"]

提示：

1 <= n <= 8

链接：https://leetcode-cn.com/problems/generate-parentheses/
"""
"""
思路：
1、输入n对括号，随机生成字符串组合
2、验证字符串组合是否成对存在

优化思路：
1、生成括号的时候就注意，让其成对存在。"("数量少于"）"时，则添加"（"，"（"数量多于"）"数量时，添加"）"

会用到的方法：递归
"""
class Solution:
    def generateParenthesis(self, n):
        pass


if __name__ == "__main__":
    n = 3
    s = Solution()
    print(s.generateParenthesis(n))
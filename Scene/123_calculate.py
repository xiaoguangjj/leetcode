"""
LCP 17. 速算机器人
小扣在秋日市集发现了一款速算机器人。店家对机器人说出两个数字（记作 x 和 y），请小扣说出计算指令：

"A" 运算：使 x = 2 * x + y；
"B" 运算：使 y = 2 * y + x。
在本次游戏中，店家说出的数字为 x = 1 和 y = 0，小扣说出的计算指令记作仅由大写字母 A、B 组成的字符串 s，字符串中字符的顺序表示计算顺序，请返回最终 x 与 y 的和为多少。

示例 1：

输入：s = "AB"

输出：4

解释：
经过一次 A 运算后，x = 2, y = 0。
再经过一次 B 运算，x = 2, y = 2。
最终 x 与 y 之和为 4。

提示：

0 <= s.length <= 10
s 由 'A' 和 'B' 组成

"""
"""
题目解读：
本题的题意理解是个难点。意思是：有两种算法，A，B。小扣说出由两个大写字母A、B组成的字符串指令，然后分别运算 两个算法，最后得到两个结果值,x,y
可以累计多次求x的和，可以累计多次求y的和。
"""


class Solution:
    def calculate(self, s):
        x, y = 1, 0
        for i in s:
            if i == "A":
                x = 2*x + y
            if i == "B":
                y = 2*y + x
        return x+y


if __name__=="__main__":
    s = "AB"
    so = Solution()
    print(so.calculate(s))
"""
9. 回文数
已解答
简单
相关标签
premium lock icon
相关企业
提示
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

例如，121 是回文，而 123 不是。


示例 1：

输入：x = 121
输出：true
示例 2：

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3：

输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。


提示：

-231 <= x <= 231 - 1
"""


class Solution:
    def isPalindrome(self, x:int) -> bool:
        s = str(x)
        return s == s[::-1]


if __name__ == "__main__":
    x = 121
    s = Solution()
    result = s.isPalindrome(x)
    print("result:\n", result)
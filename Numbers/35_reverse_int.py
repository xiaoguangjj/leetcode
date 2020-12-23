# -*- coding:utf-8 -*-

"""
7. 整数反转
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)[::-1]
        if x.endswith('-'):
            x = -int(x[:-1])
        else:
            x = int(x)
        if x < -2 ** 31 or x > 2 ** 31 - 1:
            return 0
        return x


if __name__ == '__main__':
    x = 123
    print(Solution().reverse(x))

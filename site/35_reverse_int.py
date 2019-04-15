# -*- coding:utf-8 -*-

"""
整数反转
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
"""


class Solution(object):
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


if __name__=='__main__':
    x = 2 ** 31
    print(Solution().reverse(x))
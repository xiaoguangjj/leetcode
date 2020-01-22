# -*- coding:utf-8 -*-
"""
加一
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
"""
class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)):
            print(i, ~i)
            if digits[~i] < 9:
                print(~i)
                digits[~i] += 1
                print(digits[~i])
                return digits
            digits[~i] = 0
        return [1] + [0] * len(digits)


if __name__ == '__main__':
    a = [9,9,9,9]
    print(Solution().plusOne(a))
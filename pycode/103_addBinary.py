"""
67. 二进制求和
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。



示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"


提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。
"""


class Solution:
    def addBinary(self, a, b):
        """
        思路:
        1、二进制转成十进制 ：1010=（0 * 2的零次方） + （1* 2的一次方）+ （0 * 2 的二次方）+（1 * 2的三次方）
        2、十进制转成二进制 ：循环 除2 取余，逆序读取的值 就为 结果
        :param a:
        :param b:
        :return:
        """
        if a == '0' and b == '0':
            return '0'
        number1 = 0
        number2 = 0
        for i, num in enumerate(a[::-1]):
            number1 += int(num) * (2**i)
        for i, num in enumerate(b[::-1]):
            number2 += int(num) * (2**i)
        string1 = ''
        number1 += number2
        while number1 != 0:
            # remainder = number1 % 2
            # number1 //= 2
            number1, remainder = divmod(number1, 2)
            string1 += str(remainder)
        return string1[::-1]

    def addBinary1(self, a, b):
        """
        思路：利用Python内嵌函数，int(num,2)实现两个2进制数的求和，结果为10进制
        '{0:b}'.format(num) 二进制输出
        :param a:
        :param b:
        :return:
        """
        return '{0:b}'.format(int(a, 2) + int(b, 2))


if __name__ == "__main__":
    # a = "11"
    # b = "1"
    a = "1010"
    b = "1011"
    s = Solution()
    print(s.addBinary1(a, b))

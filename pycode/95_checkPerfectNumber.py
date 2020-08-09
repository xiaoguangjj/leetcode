"""
507. 完美数
对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。

给定一个 整数 n， 如果他是完美数，返回 True，否则返回 False



示例：

输入: 28
输出: True
解释: 28 = 1 + 2 + 4 + 7 + 14
"""

"""
解题思路
可以发现这样一个规律，如24的因子为1，2，3，4，6，8，12，24，我们只需要找到1，2，3，4这四个数，就可以通过num/i的方式找出所有的因子，我称这四个因子为小因子，称num/i得到的因子为大因子，那么大因子和小因子的分割线正好是num**0.5，所以通过这个规律可以大幅度减小时间复杂度。
此外，还需要注意，这题有两个陷阱：（1）完美数的定义是在正整数范围内的，但这里给的是整数，因此需要排除负整数的情况；（2）正整数1，它并不是完美数。

链接：https://leetcode-cn.com/problems/perfect-number/solution/on05-by-yi-wen-statistics/
"""

class Solution:
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
        valueList = []
        for i in range(1, int(num ** 0.5 + 1)):
            if num % i == 0:
                valueList.append(i)
                valueList.append(num // i)
        valueList.remove(num)
        return sum(valueList) == num


if __name__ == "__main__":
    number = 1000
    s = Solution()
    for i in range(number):
        if s.checkPerfectNumber(i) is True:
            print(i)

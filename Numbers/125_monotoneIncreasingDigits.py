"""
738. 单调递增的数字
给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。

（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）

示例 1:

输入: N = 10
输出: 9
示例 2:

输入: N = 1234
输出: 1234
示例 3:

输入: N = 332
输出: 299
说明: N 是在 [0, 10^9] 范围内的一个整数。
"""


class Solution:
    def monotoneIncreasingDigits(self, N):
        number_list = list()
        M = N
        flag = 1
        while flag:
            while M > 0:
                number = M % 10
                number_list.append(number)
                M = M // 10
            if all([number_list[i] < number_list[i + 1] for i in range(len(number_list) - 1)]) is True:
                flag = 0
            else:
                M -= 1
        return M


if __name__=="__main__":
    N = 332
    s = Solution()
    print(s.monotoneIncreasingDigits(N))
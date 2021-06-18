# -*-encoding:UTF-8 -*-

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4
"""
"""
解析：
与运算是二进制数按位做相与运算再赋值，其运算规则是：

0&0=0;   0&1=0;    1&0=0;     1&1=1

"""

def singlenumber(nums):
    num = 0
    for i in nums:
        num ^= i
    return num


if __name__ == '__main__':
    # a = [1,2,3,4,1,2,3]
    a = [1, 1, 2]
    print(singlenumber(a))

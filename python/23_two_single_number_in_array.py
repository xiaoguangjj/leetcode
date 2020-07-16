# -*- coding:utf-8 -*-
"""
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
"""
"""
解题思路：
找到一个不重复的数字：任何一个数异或它自己，都等于0，所以数组中的数，依次异或一遍，得到的结果就是 那个不重复的数。
找到两个不重复的数字：将一个数组的每个序列位置，标记为i，分别乘以其他位置的数，为0 就是有重复的数字，不为0，就是没有数组中只有这一个数字。

"""


class Solution:
    def FindNumsAppearOnce(self, array):
        if len(array) <= 0:
            return []
        resultExclusiveOR = 0
        length = len(array)
        for i in array:
            resultExclusiveOR ^= i
        firstBitIs1 = self.FindFirstBitIs1(resultExclusiveOR)
        num1, num2 = 0, 0
        for i in array:
            if self.BitIs1(i, firstBitIs1):
                num1 ^= i
            else:
                num2 ^= i
        return num1, num2

    def FindFirstBitIs1(self, num):
        indexBit = 0
        while num & 1 == 0 and indexBit <= 32:
            indexBit = 0
            while num & 1 == 0 and indexBit <= 32:
                indexBit += 1
                num = num >> 1
            return indexBit

    def BitIs1(self, num, indexBit):
        num = num >> indexBit
        return num & 1


if __name__=='__main__':
    a = [1, 1, 2, 2, 3, 3, 4, 4, 5]
    print(Solution.FindNumsAppearOnce(a))

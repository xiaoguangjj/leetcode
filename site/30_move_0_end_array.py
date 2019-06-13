# -*- coding:utf-8 -*-

"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(i)
        return nums


if __name__=='__main__':
    a = [0, 1, 0, 3, 12]
    print(Solution().moveZeroes(a))

# -*- coding:utf-8 -*-
"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
"""
from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a, b = map(Counter, (nums1, nums2))
        return list((a & b).elements())


if __name__=='__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(Solution().intersect(nums1,nums2))
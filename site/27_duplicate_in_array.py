# -*- coding:utf-8 -*-
"""
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
"""


class Solution(object):
    """排序数组，然后访问数组，判断相邻元素是否相等"""
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        count = 0
        while count < len(nums) - 1:
            if nums[count] == nums[count + 1]:
                return True
            count += 1
        return False

    """判断列表转元组之后的长度是否和原长度相等"""
    def containsDuplicate_2(self, nums):
        if len(set(nums)) == len(nums):
            return False
        else:
            return True


if __name__=='__main__':
    a = [1,1,1,3,3,4,3,2,4,2]
    b = [1,2,3,4]
    print(Solution().containsDuplicate(b))
"""
35. 搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0
"""


class Solution:
    # 思路：比较两数大小，定位坐标
    def searchInsert(self, nums, target):
        """
        :param nums:
        :param target:
        :return:
        """
        index = 0
        if target in nums:
            index = nums.index(target)
        else:
            if target < nums[0]:
                index = 0
            elif target > nums[len(nums)-1]:
                index = len(nums)
            else:
                for i in range(len(nums)):
                    if nums[i] < target < nums[i+1]:
                        index = i + 1
        return index

    # 二分查找，定位坐标
    def searchInsert1(self, nums, target):
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:  # target 位于右侧
                left = mid + 1
            else:                   # target 位于左侧
                right = mid
        return left


if __name__ == '__main__':
    nums, target = [1, 3, 5, 7], 6
    s = Solution()
    print(s.searchInsert1(nums, target))

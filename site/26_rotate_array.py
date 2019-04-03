# -*- coding:utf-8 -*-

"""
旋转数组
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

"""


class Solution(object):
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        t = k % len(nums)
        nums[:] = nums[-t:] + nums[: -t]
        return nums

    def rotate_2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a = nums[:]
        if len(nums) == 1 or len(nums) == k or k == 0:
            print(nums)
        else:
            for i in range(len(nums)):
                nums[(i + k) % len(nums)] = a[i]
        return nums

    def rotate_3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for _ in range(k % len(nums)):
            nums.insert(0, nums[-1])
            nums.pop()
        return nums


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7]
    k = 2
    print(Solution().rotate_3(a, k))

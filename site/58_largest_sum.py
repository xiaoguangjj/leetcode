# -*- coding:utf-8 -*-

"""
最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxSum = sum(nums)
        curSum = 0
        for i in range(n):
            # 从i开始求和，如果当前和大于maxSum,则赋值给maxSum
            curSum += nums[i]
            if curSum > maxSum:
                maxSum = curSum
            # 前面的和如果已经小于0了，那么加上下一个元素值，肯定是小于下一个元素值
            # 所以如果前面加起来的值小于0了，则舍弃前面的和，从下一位开始继续求和
            if curSum < 0:
                curSum = 0
        return maxSum


if __name__ == '__main__':
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(a))
#coding=utf-8

import json


class Solution(object):
    def twoSum(self, nums, target):
        """
        :solution1
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
        return

    def twoSum1(self, nums, target):
        """
        :solution2
        :param nums:
        :param target:
        :return:
        """
        hashmap = {}
        for ind, num in enumerate(nums):
            hashmap[num] = ind
            print(hashmap)
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i != j:
                return i, j


def main():
    import sys
    nums = [3, 2, 4]
    target = 6
    # nums = [2, 7, 11, 15]
    # target = 9

    ret = Solution().twoSum1(nums, target)
    print(ret)


if __name__ == '__main__':
    main()
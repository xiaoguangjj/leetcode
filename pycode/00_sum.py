#coding=utf-8

import json


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target :
                    print(i, j)
                    return i, j
        return


def main():
    import sys
    nums = [3, 2, 4]
    target = 6
    # nums = [2, 7, 11, 15]
    # target = 9

    ret = Solution().twoSum(nums, target)
    print(ret)


if __name__ == '__main__':
    main()
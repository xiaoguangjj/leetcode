import json
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)-1):
                if nums[i] + nums[j] == target :
                    return i, j

def stringToIntegerList(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        print nums
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    import sys

    nums = [2, 7, 11, 15]
    target = 9

    ret = Solution().twoSum(nums, target)
    out = integerListToString(ret)
    print out

if __name__ == '__main__':
    main()
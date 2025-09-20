"""
485.最大连续1的个数

给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。



示例 1：

输入：nums = [1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
示例 2:

输入：nums = [1,0,1,1,0,1]
输出：2


提示：

1 <= nums.length <= 105
nums[i] 不是 0 就是 1.
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        if not nums:
            return 0
        max_length = 1
        current_length = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 1

        return max_length


if __name__=="__main__":
    # 数组的测试用例
    # nums = [1, 1, 0, 1, 1, 1]
    # 字符串的测试用例
    nums = "aabbbccccbbcc"
    s_c = Solution()
    result = s_c.findMaxConsecutiveOnes(nums)
    print("result:\n", result)
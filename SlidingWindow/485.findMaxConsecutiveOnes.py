from typing import List

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


# 测试数据为"aabbbccccbbcc"
class Solution:
    def findMaxConsecutiveOnes(self, s):
        if not s:
            return 0
        max_length = 1
        current_length = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 1

        return max_length

    def findMaxConsecutiveNumOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_count = 0
        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
        return max_count


if __name__ == "__main__":
    # 字符串的测试用例
    s = "aabbbccccbbcc"
    s_c = Solution()
    result1 = s_c.findMaxConsecutiveOnes(s)
    print("result:\n", result1)

    # 数组的测试用例
    nums = [1, 1, 0, 1, 1, 1]
    result2 = s_c.findMaxConsecutiveNumOnes(nums)
    print("result:\n", result2)
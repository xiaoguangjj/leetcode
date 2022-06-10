"""
45. Jump Game II
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
"""


class Solution:
    def jump(self, nums):
        max_position = 0  # 每步跳跃的最大步长
        end = 0  # 每一步的 终点
        step = 0  # 跳跃的步数
        for i in range(len(nums) - 1):
            max_position = max(max_position, i+nums[i])
            if i == end:
                step += 1
                end = max_position
        return step

    def jump1(self, nums):
        max_position = 0  # 每步跳跃的最大步长
        start = 0  # 每一步的 起点
        end = 0  # 每一步的 终点
        step = 0 # 跳跃的步数
        while end < len(nums) - 1:
            for i in range(start, end+1):
                max_position = max(max_position, i+nums[i])
            start = end
            end = max_position
            step += 1
        return step


nums = [2, 3, 1, 1, 4]
s = Solution()
result = s.jump1(nums)
print(result)
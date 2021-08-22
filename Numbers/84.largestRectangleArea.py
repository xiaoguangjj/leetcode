"""
84. 柱状图中最大的矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

示例 1:


输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10

示例 2：

输入： heights = [2,4]
输出： 4

提示：

1 <= heights.length <=105
0 <= heights[i] <= 104
链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
"""


class Solution:
    """
    暴力求解发法
    """
    def largestRectangleArea(self, heights):
        n = len(heights)
        area = 0
        for i in range(n):  # 枚举左边界
            left_i = i
            right_i = i
            while left_i >= 0 and heights[left_i] >= heights[i]:
                left_i -= 1 # 获取左边界，向左遍历，直到遇到小于标杆值为止
            while right_i < n and heights[right_i] >= heights[i]:
                right_i += 1  # 获取右边界，向右遍历，直到遇到小于标杆值为止
            area = max(area, (right_i - left_i -1)*heights[i])
        return area


if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    s = Solution()
    print(s.largestRectangleArea(heights))

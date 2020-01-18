"""
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-rectangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def stack(self,heights):
        stack = [-1]
        maxarea = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                maxarea = max(maxarea,heights[stack.pop()] * (i - stack[-1] -1))
            stack.append(i)
        while stack[-1] != -1:
            maxarea = max(maxarea,heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return maxarea

    def maximalRectangle(self,matrix):
        if not matrix: return 0
        maxarea = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrixp[i][j] == '1' else 0
            maxarea = max(maxarea, self.stack(dp))
        return maxarea

    def maximalRectangle_1(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = 0
        if m > 0:
            n = len(matrix[0])
        max_height = [0 for i in range(0, n)]
        max_right = [n - 1 for i in range(0, n)]
        max_left = [0 for i in range(0, n)]
        max_area = 0

        for i in range(0, m):
            left_border = 0
            right_border = n - 1

            for j in range(0, n):
                if matrix[i][j] == "1":
                    max_height[j] = max_height[j] + 1
                    max_left[j] = max(max_left[j], left_border)
                else:
                    max_height[j] = 0
                    left_border = j + 1
                    max_left[j] = 0

            j = n - 1
            while j >= 0:
                if matrix[i][j] == "1":
                    max_right[j] = min(max_right[j], right_border)
                else:
                    right_border = j - 1
                    max_right[j] = n - 1
                j = j - 1

            for j in range(0, n):
                if (max_right[j] - max_left[j] + 1) * max_height[j] > max_area:
                    max_area = (max_right[j] - max_left[j] + 1) * max_height[j]

        return max_area


if __name__=='main':
    maxarea = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    a = Solution.maximalRectangle_1(maxarea)
    print(a)

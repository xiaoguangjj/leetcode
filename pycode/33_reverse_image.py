# -*- coding:utf-8 -*-

"""
48. 旋转图像
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要"直接修改输入的二维矩阵"。请不要使用另一个矩阵来旋转图像。



示例 1:

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
"""

"""
思路：你需要直接修改输入的二维矩阵
这句话很重要

"""
class Solution:
    def rotate(self, matrix):
        """
        暴力求解法
        :param matrix:
        :return:
        """
        n = len(matrix)
        matrix_new = [[0]*n for _ in range(n)]
        for i, l in enumerate(matrix):
            for j, m in enumerate(l):
                matrix_new[j][n-i-1] = matrix[i][j]
        # matrix[:]=才会改变传进来的matrix值
        # matrix=创建一个新的列表，无法修改传进来的matrix.在之前和之后打印下id，就知道了。
        matrix[:] = matrix_new
        return matrix


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    Solution().rotate(matrix)
    print(matrix)

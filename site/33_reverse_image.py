# -*- coding:utf-8 -*-

"""
旋转图像
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

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


class Solution(object):

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = map(list, zip(*matrix[::-1]))
        return matrix

    def rotate_1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        num = len(matrix)
        for i in range(0, num):
            for j in range(i + 1, num):
                t = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = t
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
        return matrix

if __name__=='__main__':
    matrix =[
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(Solution().rotate_1(matrix))
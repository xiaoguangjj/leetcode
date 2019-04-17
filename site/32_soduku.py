# -*- coding:utf-8 -*-

"""
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。


上图是一个部分填充的有效的数独。

数独部分空格内已填入了数字，空白格用 '.' 表示。
示例 1:

输入:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: true

"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(0, 9):
            row = [0] * 9
            col = [0] * 9
            cube = [0] * 9
            for j in range(0, 9):
                if board[i][j] != '.':
                    if row[int(board[i][j]) - 1] == 1:
                        print(1)
                        return False
                    else:
                        row[int(board[i][j]) - 1] = 1
                if board[j][i] != '.':
                    if col[int(board[j][i]) - 1] == 1:
                        print(2)
                        return False
                    else:
                        col[int(board[j][i]) - 1] = 1
                cubeX = int(3 * (i // 3) + j // 3)
                cubeY = int(3 * (i % 3) + j % 3)
                if board[cubeX][cubeY] != '.':
                    if cube[int(board[cubeX][cubeY]) - 1] == 1:
                        print(cubeX)
                        print(cubeY)
                        print(int(board[cubeX][cubeY]) - 1)
                        return False
                    else:
                        cube[int(board[cubeX][cubeY]) - 1] = 1
        return True


if __name__=='__main__':
    a = [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    b = [
      ["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    print(Solution().isValidSudoku(b))

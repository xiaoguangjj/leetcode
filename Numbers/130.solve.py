"""

130. 被围绕的区域
给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。


输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。


示例 2：

输入：board = [["X"]]
输出：[["X"]]

提示：

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] 为 'X' 或 'O'


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def dfs(self, board, cur_i, cur_j):
        if board[cur_i][cur_j] == 'O':
            board[cur_i][cur_j] = 'A'
        for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            # 注意中间参数tmp_i, tmp_j 访问矩阵相邻的项
            tmp_i, tmp_j = cur_i + i, cur_j + j
            if 1 <= tmp_i < len(board) and 1 <= tmp_j < len(board[0]) and board[tmp_i][tmp_j] == "O":
                self.dfs(board, tmp_i, tmp_j)

    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        for j in range(col):
            # 第一行
            if board[0][j] == "O":
                self.dfs(board, 0, j)
            # 最后一行
            if board[row-1][j] == "O":
                self.dfs(board, row-1, j)
        for i in range(row):
            # 第一列
            if board[i][0] == "O":
                self.dfs(board, i, 0)
            # 最后一列
            if board[i][col-1] == "O":
                self.dfs(board, i, col-1)

        for i, l in enumerate(board):
            for j, m in enumerate(l):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        for i, l in enumerate(board):
            for j, m in enumerate(l):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
        return board


if __name__ == "__main__":
    # board = [["X", "X", "X", "X"],
    #          ["X", "O", "O", "X"],
    #          ["X", "X", "O", "X"],
    #          ["X", "O", "X", "X"]]
    board = [["O", "X", "X", "O", "X"],
             ["X", "O", "O", "X", "O"],
             ["X", "O", "X", "O", "X"],
             ["O", "X", "O", "O", "O"],
             ["X", "X", "O", "X", "O"]]

    after = [['A', 'X', 'X', 'A', 'X'],
             ['X', 'O', 'O', 'X', 'A'],
             ['X', 'O', 'X', 'O', 'X'],
             ['A', 'X', 'O', 'O', 'A'],
             ['X', 'X', 'A', 'X', 'A']]

    s = Solution()
    print(s.solve(board))

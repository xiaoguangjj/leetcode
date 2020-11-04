"""
129. 求根到叶子节点数字之和
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

例如，从根到叶子节点路径 1->2->3 代表数字 123。

计算从根到叶子节点生成的所有数字之和。

说明: 叶子节点是指没有子节点的节点。

示例 1:

输入: [1,2,3]
    1
   / \
  2   3
输出: 25
解释:
从根到叶子节点路径 1->2 代表数字 12.
从根到叶子节点路径 1->3 代表数字 13.
因此，数字总和 = 12 + 13 = 25.
示例 2:

输入: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
输出: 1026
解释:
从根到叶子节点路径 4->9->5 代表数字 495.
从根到叶子节点路径 4->9->1 代表数字 491.
从根到叶子节点路径 4->0 代表数字 40.
因此，数字总和 = 495 + 491 + 40 = 1026.

"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    '列表创建二叉树'

    def listcreattree(self, root, llist, i):
        # 用列表递归创建二叉树，它其实创建过程也是从根开始a开始，创建左子树b，再创建b的左子树，如果b的左子树为空，返回None。
        # 再接着创建b的右子树。
        if i < len(llist):
            if llist[i] is None:
                return  # 跳出循环
            else:
                root = TreeNode(llist[i])
                # 左结点
                root.left = self.listcreattree(root.left, llist, 2 * i + 1)
                # 右结点
                root.right = self.listcreattree(root.right, llist, 2 * i + 2)
                # print('**********返回根：', root.val)
                return root
        return root


    # 深度遍历
    def sumNumbers(self, root):
        def dfs(root: TreeNode, prevTotal: int) -> int:
            if not root:
                return 0
            total = prevTotal * 10 + root.val   # prevTotal为上次的total
            if not root.left and not root.right:  # 如果结点的子结点为空，返回结果
                return total
            else:   # 如果结点不为空，深度遍历树
                return dfs(root.left, total) + dfs(root.right, total)

        return dfs(root, 0)


if __name__ == "__main__":
    val = [4,9,0,5,1]
    s = Solution()
    root1 = s.listcreattree(None, val, 0)
    print(root1)
    print(s.sumNumbers(root1))
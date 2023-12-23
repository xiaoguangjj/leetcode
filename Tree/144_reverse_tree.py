"""
***
LCR 144. 翻转二叉树
给定一棵二叉树的根节点 root，请左右翻转这棵二叉树，并返回其根节点。

示例 1：
输入：root = [5,7,9,8,3,2,4]
输出：[5,9,7,4,2,3,8]
提示：

树中节点数目范围在 [0, 100] 内
-100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        return root


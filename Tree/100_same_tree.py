# 100. 相同的树
"""
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
输入：p = [1,2,3], q = [1,2,3]
输出：true
输入：p = [1,2], q = [1,null,2]
输出：false

提示：

两棵树上的节点数目都在范围 [0, 100] 内
-104 <= Node.val <= 104
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:  # 如果两个节点都为空，则认为是相同的
            return True
        elif not p or not q:  # 如果一个节点为空，另一个不为空，则认为不同
            return False
        elif p.val != q.val:  # 如果两个节点都不为空，值和左右子树都必须相同
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



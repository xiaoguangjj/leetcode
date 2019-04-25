# -*- coding:utf-8 -*-

"""

 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxDepth(self, root):
        # write your code here
        def find(root):
            if (root is None): return 0
            left = find(root.left)
            right = find(root.right)
            if (left > right):
                return left + 1
            else:
                return right + 1

        result = find(root)
        return result


if __name__=='__main__':
    """
            2
           / \
          1   3
               \
                4
               / \
              6   5
    """
    Tree = TreeNode(2)
    Tree.left = TreeNode(1)
    aa = Tree.right = TreeNode(3)
    bb = aa.right = TreeNode(4)
    cc = TreeNode(5)
    bb.right = cc
    dd = TreeNode(6)
    bb.left = dd
    s = Solution()
    print(s.maxDepth(Tree))


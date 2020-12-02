# -*- coding:utf-8 -*-

"""
将有序数组转换为二叉搜索树
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

    def pre_order(self, tree):
        if tree == None:
            return
        print(tree.val)
        self.pre_order(tree.left)
        self.pre_order(tree.right)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [root]
        res = []
        if not root:
            return []
        while queue:
            templist = []
            templen = len(queue)
            for i in range(templen):
                temp = queue.pop(0)
                templist.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            res.append(templist)
        return res


if __name__=='__main__':
    # Tree = TreeNode(2)
    # aa = TreeNode(1)
    # bb = TreeNode(1)
    # cc = TreeNode(4)
    # dd = TreeNode(5)
    # Tree.left = aa
    # Tree.right = bb
    # aa.left = cc
    # aa.right = dd
    # bb.left = dd
    # bb.right = cc
    s = Solution()
    a = [-10, -3, 0, 5, 9]
    result = s.sortedArrayToBST(a)
    # print(s.pre_order(result))
    print(s.levelOrder(result))

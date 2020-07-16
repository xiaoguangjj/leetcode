# -*- coding:utf-8 -*-

"""
对称二叉树
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # 思路主要参考leetcode100题，这里将根节点的左右节点假设成两颗独立的树，这样解题跟100就是类似的了,区别：递归调用时，因是对称，所以是左树左节点与右树右节点，左树右节点与右树左节点
        # 先定义，后调用
        def isSameTree(p, q):
            if not p and not q:  # 两二叉树皆为空，递归边界，两者皆为空返回真
                return True
            if p and q and p.val == q.val:
                l = isSameTree(p.left, q.right)  # ，与leetcode100有区别。递归，每次重新从函数入口处进行，每次进行递归边界判断
                r = isSameTree(p.right, q.left)
                return l and r  # and操作，需要l与r皆为true时，才返回真。只用最后一次递归边界return值
            else:
                return False

        if not root:
            return True
        else:
            # p=root.left;q=root.right
            return isSameTree(root.left, root.right)

    def depth(self, root):
        if root == None:
            return 0
        left, right = self.depth(root.left), self.depth(root.right)
        return max(left, right) + 1  # 定义在类里的

    # 前序遍历
    # 根结点-左结点-右结点
    def pre_order(self, tree):
        if tree == None:
            return
        print(tree.val)
        self.pre_order(tree.left)
        self.pre_order(tree.right)

    # 中序遍历
    # 左结点-根结点-右结点
    def mid_order(self, tree):
        if tree == None:
            return
        mid_order(tree.left)
        print(tree.data)
        mid_order(tree.right)

    # 后序遍历
    # 左结点-右结点-根结点
    def post_order(self, tree):
        if tree == None:
            return
        post_order(tree.left)
        post_order(tree.right)
        print(tree.data)



if __name__=='__main__':
    Tree = TreeNode(2)
    aa = TreeNode(1)
    bb = TreeNode(1)
    cc = TreeNode(4)
    dd = TreeNode(5)
    Tree.left = aa
    Tree.right = bb
    aa.left = cc
    aa.right = dd
    bb.left = dd
    bb.right = cc
    s = Solution()
    print(s.isSymmetric(Tree))
    print(s.pre_order(Tree))
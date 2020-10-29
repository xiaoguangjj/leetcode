# -*-encoding:UTF-8 -*-

"""
104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# 二叉树的最大深度
class Max:
    def maxDepth(self, root):
        """

        :param root:
        :return:
        """
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0


class MaxDepth:
    def maxDepth(self, root):
        """
        方法：递归的办法
        :param root:
        :return:
        """
        if root == None:
            return 0
        leftChildHeight = self.maxDepth(root.lef)
        rightChidHeight = self.maxDepth(root.right)
        return max(leftChildHeight, rightChidHeight) + 1


if __name__ == "__main__":
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
    s = Max()
    print(s.maxDepth(Tree))

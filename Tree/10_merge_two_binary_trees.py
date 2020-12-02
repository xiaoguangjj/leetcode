
# Given two binary trees and imagine that when you put one of them to cover the other,
# some nodes of the two trees are overlapped while the others are not.

# Defination for a binary tree node


class TreeNode(object):
   def __init__(self,x):
       self.val = x
       self.left = None
       self.right = None


class Solution(object):
    def mergeTrees(self,t1,t2):
        """

        :param t1:
        :param t2:
        :return:
        """
        # when all tree node is none
        if t1 is None and t2 is None:
            return
        # if only one tree node is none
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        # when tree node is overload
        t1.val += t2.val
        # iteration
        t1.right = self.mergeTrees(t1.right, t2.right)
        t1.left = self.mergeTrees(t1.left, t2.left)
        return t1

    # the second method to solute the problem
    def mergeTrees_02(self,t1,t2):
        """

        :param t1:
        :param t2:
        :return:
        """
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees_02(t1.left, t2.left)
            root.right = self.mergeTrees_02(t1.right, t2.right)
            return root
        else:
            return t1 or t2
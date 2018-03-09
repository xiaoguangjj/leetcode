# -*-encoding:UTF-8 -*-



#二叉树的最大深度
class Max():
    def maxDepth(self, root):
        """

        :param root:
        :return:
        """
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0


class MaxDepth():
    def maxDepth(self, root):
        """

        :param root:
        :return:
        """
        if root==None:
            return 0
        leftChildHeight=self.maxDepth(root.lef)
        rightChidHeight=self.maxDepth(root.right)
        return max(leftChildHeight,rightChidHeight) + 1
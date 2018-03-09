


def maxDepth(self, root):
    return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0



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
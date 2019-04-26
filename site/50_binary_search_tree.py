# -*- coding:utf-8 -*-

"""
验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
"""


class TreeNode():
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None


# 思路：　二叉搜索树的中序遍历是一个单调递增的序列，最小值一定在左子树的最左边叶子节点，最大值在右子树的最右边叶子节点．
# 所以，先通过中序遍历找到最左边的叶子节点，做最小值，然后后面的值都比他大才对，然后就一层一层的往回返．注意，遍历过得
# 根节点就不再重新遍历左右子树了，也直接开始比较．


def SearchTree(root):
    nodes = []
    ever_nodes = []
    b = float('-Inf')

    while root or nodes:
        if ((not root.left) and (not root.right) or root in ever_nodes):
            if root.data <= b: #　比中序遍历的前一个值还小，不是二叉搜索树
                return False
            else: #　符合条件，那继续看其他的点是否符合条件,下一个点就得比他还小了
                b = root.data
                if len(nodes):
                    root = nodes.pop()
                else:
                    return True
            continue
        else:
            if root.right:
                nodes.append(root.right)
            nodes.append(root)
            if root.left:
                nodes.append(root.left)
            ever_nodes.append(root)
            # 遍历完当前节点,右－＞中－＞左
            # 把左子树pop出来，以他为根节点继续往下遍历直到找到最左边的叶子节点
            root = nodes.pop() # 把左边ｐｏｐ出来，继续往下遍历，或者到达终点


if __name__=='__main__':
    """
             12
           /   \
          5     18
         / \   /  \
        2   9 15   19
          
    """
    a = TreeNode(12)
    b = TreeNode(5)
    c = TreeNode(18)
    d = TreeNode(2)
    e = TreeNode(9)
    f = TreeNode(15)
    g = TreeNode(19)
    h = TreeNode(3)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    # d.left = h
    m = SearchTree(a)
    print(m)

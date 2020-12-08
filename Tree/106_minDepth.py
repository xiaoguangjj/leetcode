"""
111. 二叉树的最小深度
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.

"""

# Definition for a binary tree node.

import collections


'二叉树结点类'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    '列表创建二叉树'
    def listcreattree(self, root, llist, i):
        #用列表递归创建二叉树，它其实创建过程也是从根开始a开始，创建左子树b，再创建b的左子树，如果b的左子树为空，返回None。
        #再接着创建b的右子树。
        if i < len(llist):
            if llist[i] is None:
                return      # 跳出循环
            else:
                root = TreeNode(llist[i])
                # 左结点
                root.left = self.listcreattree(root.left, llist, 2*i+1)
                # 右结点
                root.right = self.listcreattree(root.right, llist, 2*i+2)
                # print('**********返回根：', root.val)
                return root
        return root


    """
    方法一：深度优先遍历
    """
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        min_depth = 10**9
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)
        return min_depth + 1

    """
    方法二：广度优先搜索
    """

    def minDepth1(self, root):
        if not root:
            return 0

        que = collections.deque([(root, 1)])  # 定义双边队列
        while que:
            node, depth = que.popleft()     # 队首元素出列
            if not node.left and not node.right:
                return depth
            if node.left:
                que.append((node.left, depth + 1))  # 入队：修改结点，左子树的深度
            if node.right:
                que.append((node.right, depth + 1))  # 入队：修改结点，右子树的深度
        return 0


if __name__ == "__main__":
    llist = [3, 9, 20, None, None, 15, 7]
    s = Solution()
    root = s.listcreattree(None, llist, 0)
    # print(s.minDepth(root))
    print(s.minDepth1(root))

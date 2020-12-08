"""
530. 二叉搜索树的最小绝对差
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。



示例：

输入：

   1
    \
     3
    /
   2

输出：
1

解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。


提示：

树中至少有 2 个节点。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 列表创建二叉树
    def listcreattree(self, root, llist, i):
        # 用列表递归创建二叉树，它其实创建过程也是从根开始a开始，创建左子树b，再创建b的左子树，如果b的左子树为空，返回None。
        # 再接着创建b的右子树。
        if i < len(llist):
            if llist[i] is None:
                return  # 跳出循环
            else:
                root = TreeNode(llist[i])
                # 左结点
                root.left = self.listcreattree(root.left, llist, 2 * i + 1)
                # 右结点
                root.right = self.listcreattree(root.right, llist, 2 * i + 2)
                # print('**********返回根：', root.val)
                return root
        return root

    pre = 999
    diff = 999

    # 二叉搜索树
    def getMinimumDifference(self, root):
        def Search(root):
            if root == None:
                return

            Search(root.left)
            self.diff = min(self.diff, abs(self.pre - root.val))
            self.pre = root.val
            Search(root.right)

        Search(root)

        return self.diff


if __name__ == '__main__':
    llist = [1, None, 3, None, None, 2, None]
    s = Solution()
    root1 = s.listcreattree(None, llist, 0)
    print("中序遍历-->")
    print(s.getMinimumDifference(root1))

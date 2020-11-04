"""
144. 二叉树的前序遍历
难度 中等

给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '列表创建二叉树'
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

    def preorderTraversal(self, root):
        res = list()
        def preorder(root):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return res


if __name__ == "__main__":
    preTree = [1, None, 2, 3]
    s = Solution()
    root1 = s.listcreattree(None, preTree, 0)
    T = TreeNode()
    s = Solution()
    print(s.preorderTraversal(root1))
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
    # 前序遍历，创建二叉树
    def listcreattree(self, root, llist,i):
        if i < len(llist):
            if llist[i] is None:
                return  # 跳出循环
            else:
                root = TreeNode(llist[i])
                # 左结点
                root.left = self.listcreattree(root.left, llist,i)
                # 右结点
                root.right = self.listcreattree(root.right, llist,i)
                print('**********返回根：', root.val)
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
"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。



例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
限制：

0 <= 节点个数 <= 5000
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self,preorder, inorder):
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder.pop(0))
        # 利用python数组的index函数来定位根节点在inorder数组中的位置。
        index = inorder.index(root.val)
        # preorder数组不需要进行切片操作，递归终止条件主要靠代码前两行中的not inorder来终止。
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index + 1:])
        return root


if __name__=="__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    s = Solution()
    s.buildTree(preorder, inorder)
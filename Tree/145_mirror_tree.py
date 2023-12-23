"""
LCR 145. 判断对称二叉树
请设计一个函数判断一棵二叉树是否 轴对称 。

输入：root = [6,7,7,8,9,9,8]
输出：true
解释：从图中可看出树是轴对称的。
输入：root = [1,2,2,null,3,null,3]
输出：false
解释：从图中可看出最后一层的节点不对称。
"""


class TreeNode:
    def __int__(self, val=0, left=None, right=None):
        self.val = None
        self.left = left
        self.right = right


class Solution:
    def checkSymmetricTree(self, root) -> bool:
        return self.check(root, root)

    def check(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.check(p.left, q.right) and self.check(p.right, q.left)


if __name__ == "__main__":
    root = TreeNode()
    s = Solution()
    s.checkSymmetricTree(root)

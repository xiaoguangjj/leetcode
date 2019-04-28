# -*- coding:utf-8 -*-
"""
二叉树的层次遍历
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def level_print(self, tree):
        if tree == None:
            return
        q = []
        q.append(tree)
        results = {}
        level = 0
        current_level_num = 1
        nextlevelnum = 0
        d = []
        while q:
            current = q.pop(0)
            current_level_num -= 1
            d.append(current.val)
            if current.left != None:
                q.append(current.left)
                nextlevelnum += 1
            if current.right != None:
                q.append(current.right)
                nextlevelnum += 1
            if current_level_num == 0:
                current_level_num = nextlevelnum
                nextlevelnum = 0
                results[level] = d
                d = []
                level += 1
        print(results)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [root]
        res = []
        if not root:
            return []
        while queue:
            templist = []
            templen = len(queue)
            for i in range(templen):
                temp = queue.pop(0)
                templist.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            res.append(templist)
        return res


if __name__=='__main__':
    Tree = TreeNode(2)
    aa = TreeNode(1)
    bb = TreeNode(1)
    cc = TreeNode(4)
    dd = TreeNode(5)
    Tree.left = aa
    Tree.right = bb
    aa.left = cc
    aa.right = dd
    bb.left = dd
    bb.right = cc
    s = Solution()
    # print(s.level_print(Tree))
    print(s.levelOrder(Tree))
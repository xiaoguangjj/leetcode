"""
95. 不同的二叉搜索树 II
中等
相关标签
premium lock icon
相关企业
给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。



示例 1：


输入：n = 3
输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
示例 2：

输入：n = 1
输出：[[1]]


提示：

1 <= n <= 8
"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        return self.generate_trees(1,n)

    def generate_trees(self, start, end):
        if start > end:
            return [None]
        all_nodes = []
        for i in range(start, end+1):
            left_trees = self.generate_trees(start, i-1)
            right_trees = self.generate_trees(i+1, end)
            for l in left_trees:
                for r in right_trees:
                    current_tree = TreeNode(i)
                    current_tree.left = l
                    current_tree.right = r
                    all_nodes.append(current_tree)
        return all_nodes


def tree_to_serialized_list(root):
    """将二叉树序列化为题目要求的格式"""
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append('null')

    # 移除末尾的'null'
    while result and result[-1] == 'null':
        result.pop()

    return result


if __name__ == "__main__":
    n = 3
    s = Solution()
    trees = s.generateTrees(n)

    # 序列化所有树
    serialized_trees = []
    for tree in trees:
        serialized = tree_to_serialized_list(tree)
        serialized_trees.append(serialized)

    # 构建最终输出
    output = "[" + ",".join(["[" + ",".join(tree) + "]" for tree in serialized_trees]) + "]"
    print(output)
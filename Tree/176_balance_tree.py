"""

LCR 176. 判断是否为平衡二叉树
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

示例 1:

输入：root = [3,9,20,null,null,15,7]
输出：true
方法一由于是自顶向下递归，因此对于同一个节点，函数 height\texttt{height}height 会被重复调用，导致时间复杂度较高。如果使用自底向上的做法，则对于每个节点，函数 height\texttt{height}height 只会被调用一次。

自底向上递归的做法类似于后序遍历，对于当前遍历到的节点，先递归地判断其左右子树是否平衡，再判断以当前节点为根的子树是否平衡。如果一棵子树是平衡的，则返回其高度（高度一定是非负整数），否则返回 −1-1−1。如果存在一棵子树不平衡，则整个二叉树一定不平衡。

作者：力扣官方题解
链接：https://leetcode.cn/problems/ping-heng-er-cha-shu-lcof/solutions/832191/ping-heng-er-cha-shu-by-leetcode-solutio-6r1g/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root) -> bool:
        def get_height(root):
            if not root:
                return 0
            leftHeight = get_height(root.left)  # 后续遍历
            rightHeight = get_height(root.right)  # 后续遍历
            if leftHeight == -1 or rightHeight == -1:  # 如果左子树的高度为-1 就 返回-1，子树为-1，父节点也为-1。
                return -1
            elif abs(leftHeight - rightHeight) > 1:    # 左右子树的高度差大于1，不是平衡二叉树返回-1
                return -1
            else:
                return max(leftHeight, rightHeight) + 1    # 正常返回 二叉树的高度
        return get_height(root) >= 0        # 返回二叉树的高度

"""
给你一棵以 root 为根的二叉树和一个整数 target ，请你删除所有值为 target 的 叶子节点 。

注意，一旦删除值为 target 的叶子节点，它的父节点就可能变成叶子节点；如果新叶子节点的值恰好也是 target ，那么这个节点也应该被删除。

也就是说，你需要重复此过程直到不能继续删除。

 示例 1：
         1               1           1
       /  \            /  \           \
      2    3    =>    ②   3    =>     3
     /   /  \              \            \
    ②  ②   4              4            4

输入：root = [1,2,3,2,null,2,4], target = 2
输出：[1,null,3,null,4]
解释：
上面左边的图中，带圈叶子节点，且它们的值与 target 相同（同为 2 ），它们会被删除，得到中间的图。
有一个新的节点变成了叶子节点且它的值与 target 相同，所以将再次进行删除，从而得到最右边的图。
③
示例 2：
    1               1
   / \             /
  3  ③     =>    3
 / \              \
③  2              2
输入：root = [1,3,3,3,2], target = 3
输出：[1,3,null,null,2]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-leaves-with-a-given-value
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def removeLeafNodes(self, root, target):
        if root:
            root.left = self.removeLeafNodes(root.left, target)
            root.right = self.removeLeafNodes(root.right, target)
            return (root.left or root.right or root.val != target) and root or None


if __name__=="__main":
    """
        1               
       /  \           
      2    3   
     /   /  \            
    ②  ②   4
    """
    Tree = TreeNode(1)
    aa = Tree.left = TreeNode(2)
    bb = Tree.right = TreeNode(3)
    aa.left = TreeNode(2)
    bb.left = TreeNode(2)
    bb.right = TreeNode(4)
    # print(Tree)
    print(Solution().removeLeafNodes(Tree, 2))


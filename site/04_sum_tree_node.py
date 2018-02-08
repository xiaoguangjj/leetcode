
class Solution(object):
    def maxPathSum(self, root):
        def dfs(node):  # returns: max one side path sum, max path sum
            l = r = 0
            ls = rs = None
            if node.left:
                l, ls = dfs(node.left)
                l = max(l, 0)
            if node.right:
                r, rs = dfs(node.right)
                r = max(r, 0)
            return node.val + max(l, r), max(node.val + l + r, ls, rs)
        if root:
            return dfs(root)[1]
        return 0

if __name__=='__main__':
    Solution.maxPathSum()

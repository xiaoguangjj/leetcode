# -*- coding: UTF-8 -*-


# 给定一个非空的二叉树，以数组的形式返回每个级别上节点的平均值。
# 例1：
# 输入：
#    3
#   / \
#  9 20
#    / \
#   15 7
# 输出： [3,14.5,11]
# 说明：
# 0级节点的平均值为3，1级为14.5，2级为11，因此返回[3,14.5,11]。


class Average(object):
    def averageoflevel(self, root):
        info = []

        def dfs(node, depth = 0):
            if node:
                if len(info) <= depth:
                    info.append([0, 0])
                info[depth][0] += node.val
                info[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        dfs(root)

        return [s/float(c) for s, c in info]

    def averageoflevels_02(self, root):
        """

        :param root:
        :return:
        """
        res = []
        if not root: return res
        q = [root]
        while q:
            q1 = []
            total = 0
            cnt = 0
            while q:
                node = q.pop()
                if node.left: q1.append(node.left)
                if node.right: q1.append(node.right)
                total += node.val
                cnt += 1
            res.append(total*1.0/cnt)
            q = list(q1)
        return res


if __name__ == '__main':
    aver = Average()
    tree = [3, 9, 20, 15, 7]
    aver.averageoflevel(tree)

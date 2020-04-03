"""
有 n 个城市，按从 0 到 n-1 编号。给你一个边数组 edges，其中 edges[i] = [fromi, toi, weighti] 代表 fromi 和 toi 两个城市之间的双向加权边，距离阈值是一个整数 distanceThreshold。

返回能通过某些路径到达其他城市数目最少、且路径距离 最大 为 distanceThreshold 的城市。如果有多个这样的城市，则返回编号最大的城市。

注意，连接城市 i 和 j 的路径的距离等于沿该路径的所有边的权重之和。

示例 1：

输入：n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
输出：3
解释：城市分布图如上。
每个城市阈值距离 distanceThreshold = 4 内的邻居城市分别是：
城市 0 -> [城市 1, 城市 2] 
城市 1 -> [城市 0, 城市 2, 城市 3] 
城市 2 -> [城市 0, 城市 1, 城市 3] 
城市 3 -> [城市 1, 城市 2] 
城市 0 和 3 在阈值距离 4 以内都有 2 个邻居城市，但是我们必须返回城市 3，因为它的编号最大。

示例 2：

输入：n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
输出：0
解释：城市分布图如上。 
每个城市阈值距离 distanceThreshold = 2 内的邻居城市分别是：
城市 0 -> [城市 1] 
城市 1 -> [城市 0, 城市 4] 
城市 2 -> [城市 3, 城市 4] 
城市 3 -> [城市 2, 城市 4]
城市 4 -> [城市 1, 城市 2, 城市 3] 
城市 0 在阈值距离 4 以内只有 1 个邻居城市。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
思路：

从i = 0开始，遍历所有的城市。对每一个城市i，应用Dijkstra's Algorithm找到城市i到其余所有（n - 1）个城市的最短路径的距离，将结果保存在一个
一维数组中。然后遍历这个最短距离数组，得到与城市i的最短路径距离小于等于threshold distance的城市个数。如果这个城市个数小于当前的最小值，
则将i标记为截止到当前的答案。继续对城市i + 1， ..., 城市n - 1 应用Dijkstra's Algorithm，从而得到最终结果。
Dijkstra's algorithm:

问题描述：给定一个起点城市i，求其余城市到起点城市i的最小距离。已知的数据是n个城市中每两个城市之间的weight矩阵cost （其中cost[i][j] = 
城市i到城市j的weight。对于没有一根线段连接的城市i和城市j，cost[i][j] = +infinity）。对于固定的起点城市i，我们想要找到其余城市到城市i的
最短路径。我们用shortestPath代表距离城市i的最短距离数组，即shortestPath[j]代表城市j与城市i的最短距离（j \neq ij 

​	
 =i）。
算法描述：Dijkstra's algroithm在Dijkstra函数中实现。开始时设置shortestPath[j] = float('inf') （j\neq ij 

​	
 =i），shortestPath[i] = 0。用boolean数组used记录是否已经找到了从城市i到城市k的最短路径。即如果used[k] == 1，则表示已经找到了从
 城市i到城市k的最短路径；如果used[k] == 0则表示还没有。每一次循环，我们从没有得到最短路径的城市中找shortestPath[v]最小的那个城市，
 找到后设置used[v] = 1。然后，对每一个城市到城市i的最短距离进行更新。更新完之后继续循环。如果所有城市与城市i的最短距离均已找到，
 即used[v] == 1, for all v = 0, 1, ..., n - 1 and v \neq iv 

​	
 =i. 我们就跳出循环。最后Dijkstra函数返回的是一个数组shortestPath, shortestPath[v]代表从城市i到城市v的最短距离。
有了shortestPath数组，我们就能找到距离城市i最短距离小于等于distanceThreshold的城市个数。依次对城市i = 0, 1, ..., n - 1
应用Dijkstra's algorithm就能得到答案。

"""


class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        cost = [[float('inf') for _ in range(n)] for _ in range(n)]
        for e in edges:
            cost[e[0]][e[1]] = e[2]
            cost[e[1]][e[0]] = e[2]
        cur = float('inf')
        candi = -1
        for i in range(n):
            temp_path = self.Dijkstra(cost, i, n)
            cnt = 0
            for j in range(n):
                if j != i and temp_path[j] <= distanceThreshold:
                    cnt += 1
            if (cnt < cur) or (cnt == cur and i > candi):
                candi = i
                cur = cnt
        return candi

    def Dijkstra(self, cost, start_point, n):
        shortestPath = [float('inf') for _ in range(n)]
        shortestPath[start_point] = 0
        used = [0 for _ in range(n)]
        while True:
            v = -1 # v is the next vertex with the shortest distance to start_point.
            for i in range(n):
                if (used[i] == 0) and (v == -1 or shortestPath[i] <  shortestPath[v]):
                    v = i
            if v == -1: # if v == -1, it means that we have not found a vertex, i.e., all vertices have been visited.
                break
            used[v] = 1
            for i in range(n):
                shortestPath[i] = min(shortestPath[i], shortestPath[v] + cost[v][i])# update shortestPath

        return shortestPath


if __name__ == "__main__":
    n = 4
    edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
    distanceThreshold = 4
    a = Solution()
    print(a.findTheCity(n, edges, distanceThreshold))
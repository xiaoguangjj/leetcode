"""
在 x 轴上有一个一维的花园。花园长度为 n，从点 0 开始，到点 n 结束。

花园里总共有 n + 1 个水龙头，分别位于 [0, 1, ..., n] 。

给你一个整数 n 和一个长度为 n + 1 的整数数组 ranges ，其中 ranges[i] （下标从 0 开始）表示：如果打开点 i 处的水龙头，可以灌溉的区域为 [i -  ranges[i], i + ranges[i]] 。

请你返回可以灌溉整个花园的 最少水龙头数目 。如果花园始终存在无法灌溉到的地方，请你返回 -1 。
示例 1：
输入：n = 5, ranges = [3,4,1,1,0,0]
输出：1
解释：
点 0 处的水龙头可以灌溉区间 [-3,3]
点 1 处的水龙头可以灌溉区间 [-3,5]
点 2 处的水龙头可以灌溉区间 [1,3]
点 3 处的水龙头可以灌溉区间 [2,4]
点 4 处的水龙头可以灌溉区间 [4,4]
点 5 处的水龙头可以灌溉区间 [5,5]
只需要打开点 1 处的水龙头即可灌溉整个花园 [0,5] 。

示例 2：

输入：n = 3, ranges = [0,0,0,0]
输出：-1
解释：即使打开所有水龙头，你也无法灌溉整个花园。
示例 3：

输入：n = 7, ranges = [1,2,1,0,2,1,0,1]
输出：3
示例 4：

输入：n = 8, ranges = [4,0,0,0,0,0,0,0,4]
输出：2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-number-of-taps-to-open-to-water-a-garden
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    def minTaps(self, n, r):
        ans, i, start = 0, 0, 0# ans:为最少需要选择的水龙头树目， i: 为当前需要覆盖的最左边的位置,
        # start: 为开始选择水龙头的下标, start之前的水龙头不可能会被选取
        while i < n:
            j, maxC = start, i
            while j - i <= 100 and j <= n: # 100 为range[i]的最大值
                if r[j] >= (j - i) and maxC <= r[j] + j: maxC, start = r[j] + j, j + 1
                # r[j] >= (j - i): 表示水龙头j可以覆盖到i, maxC <= r[j] + j: 表示该水龙头覆盖到最右地方,大于当前选择的水龙头
                j = j + 1
            if maxC == i: return -1  # 无法向右覆盖, 即没有办法全覆盖, 返回-1
            ans = ans + 1  # 选择start - 1的水龙头, 拧开
            i = maxC  # 更新最左节点
        return ans


if __name__=="__main__":
    # n = 5
    # ranges = [3, 4, 1, 1, 0, 0]
    n = 3
    ranges = [0, 0, 0, 0]
    a = Solution()
    print(a.minTaps(n, ranges))

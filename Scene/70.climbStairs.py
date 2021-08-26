# -*- coding:utf-8 -*-

"""
 70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""
import functools

class Solution:
    # 直接DP，新建一个字典或者数组来存储以前的变量，空间复杂度O(n)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        climb = dict()
        climb[1], climb[2] = 1, 2
        for i in range(3, n + 1):
            climb[i] = climb[i - 1] + climb[i - 2]
        print(climb)
        return climb[n]

    #直接递归解法，容易超时，python可以加个缓存装饰器，这样也算是将递归转换成迭代的形式了
    @functools.lru_cache(100)
    def climbStairs1(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs1(n-1) + self.climbStairs1(n-2)

if __name__ == '__main__':
    print(Solution().climbStairs(2))
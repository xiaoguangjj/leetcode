"""
204. 计数质数
统计所有小于非负整数 n 的质数的数量。



示例 1：

输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
示例 2：

输入：n = 0
输出：0
示例 3：

输入：n = 1
输出：0


提示：

0 <= n <= 5 * 106

"""

import math

class Solution: # 超时
    def isPrime(self, num):
        max_num = int(math.sqrt(num))
        for i in range(2, max_num + 1):
            if num % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        count = 0
        for num in range(2, n):
            if self.isPrime(num):
                count += 1
        return count




if __name__=="__main__":
    n = 10  # 2,3,5,7
    s = Solution()
    print(s.countPrimes(n))
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

class Solution:
    def isPrime(self, num):
        max_num = int(math.sqrt(num)) # 注意 i 遍历到最大 √n 即可。因为n如果不是素数，那么至少有一个因子是小于等于√n的。√n * √n = n
        for i in range(2, max_num + 1):
            if num % i == 0:
                return False
        return True

    def countPrimes(self, n):
        # 方法一：超时
        count = 0
        for num in range(2, n):
            if self.isPrime(num):
                count += 1
        return count

    def countPrimes1(self, n):
        #方法二：
        # 厄拉多塞筛法：要得到自然数n以内的全部质数，必须把不大于根号 n 的所有质数的倍数剔除，剩下的就是质数。

        # 最小的质数是 2
        if n < 2:
            return 0

        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0  # 0和1不是质数，先排除掉

        # 埃式筛，把不大于根号 n 的所有质数的倍数剔除
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                isPrime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)

        return sum(isPrime)




if __name__=="__main__":
    n = 10  # 2,3,5,7
    s = Solution()
    print(s.countPrimes1(n))
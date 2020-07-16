#coding=utf-8


# 计算海明距离
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :param x:
        :param y:
        :return:
        """
        x = x ^ y
        print('^:', x)
        y = 0
        while x:
            y += 1
            x = x & (x - 1)
            print(x)
        return y

if __name__ == '__main__':
    x = 5
    y = 2
    So = Solution().hammingDistance(x, y)
    # print(So)
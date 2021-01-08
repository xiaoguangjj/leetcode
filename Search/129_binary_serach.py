"""
1. 二分查找(Binary Search)
算法核心：在查找表中不断取中间元素与查找值进行比较，以二分之一的倍率进行表范围的缩小。

"""


class Solution:
    def binary_serach(self, li, val):
        left = 0
        right = len(li) - 1
        while left <= right:  # 候选区有值
            mid = (left + right) // 2
            if li[mid] == val:
                return mid
            elif li[mid] > val:  # 待查找的值在左边
                right = mid - 1
            else:  # 待查找的值在右边
                left = mid + 1
        else:
            return None


if __name__ == "__main__":
    s = Solution()
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(s.binary_serach(li, 6))

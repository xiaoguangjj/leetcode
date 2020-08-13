"""
输入两个列表 alist, blist，依次顺序比较两个list中的元素
如果alist的元素大于blist的元素，返回alist;
如果alist的元素小于blist的元素，返回blist;
如果两个list的所有元素都相等，返回alist，否则返回blist

"""


class Solution:
    def compare_list(self, alist, blist):
        if alist >= blist:
            return alist
        else:
            return blist


if __name__ == "__main__":
    alist = [1, 2, 3, 4, 5]
    blist = [5, 4, 3, 2, 1]
    s = Solution()
    print(s.compare_list(alist, blist))

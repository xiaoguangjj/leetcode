# -*- coding:utf-8 -*-

"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
"""


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        minl = min([len(x) for x in strs])
        end = 0
        while end < minl:
            for i in range(1, len(strs)):
                if strs[i][end] != strs[i - 1][end]:
                    return strs[0][:end]
            end += 1
        return strs[0][:end]


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    # a = ["dog","racecar","car"]
    print(Solution().longestCommonPrefix(strs))

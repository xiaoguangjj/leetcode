# -*- coding:utf-8 -*-

"""
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        方法1
        :param strs:
        :return:
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        minl = min([len(x) for x in strs])  # 求最小字符串的长度
        end = 0
        while end < minl:
            for i in range(1, len(strs)):
                if strs[i][end] != strs[i - 1][end]:
                    return strs[0][:end]
            end += 1
        return strs[0][:end]


    def longestCommonPrefix1(self):
        """
        方法2
        :return:
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs[1:]:
                if i == len(s) or s[i] != char:
                    return strs[0][:i]
        return strs[0]


if __name__ == '__main__':
    # strs = ["flower", "flow", "flight"]
    strs = ["dog", "racecar", "car"]
    print(Solution().longestCommonPrefix(strs))

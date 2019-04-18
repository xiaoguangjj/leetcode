# -*- coding:utf-8 -*-

"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
"""


class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]
        if len(strs) == 0:
            return ""
        min_len = min([ len(i) for i in strs])
        if min_len == 0:
            return ""
        result = []
        str_list = [list(i) for i in strs]
        for i in range(min_len):
            for j in range(len(strs)-1):
                if str_list[j][i] != str_list[j+1][i]:
                    return ''.join(result)
                print(str_list[j][i])
                result.append(str_list[j][i])
                # if(min_len == i+1):
                #     return ''.join(result)
        return result

    def longest(self,strs):
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
    # print(Solution().longestCommonPrefix(strs))
    print(Solution().longest(strs))
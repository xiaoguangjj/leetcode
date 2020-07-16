# -*- coding:utf-8 -*-

"""
实现strStr()
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
"""


class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        return haystack.find(needle)

    def strStr_1(self, haystack, needle):
        if not needle:
            return 0
        if needle not in haystack:
            return -1
        else:
            for index in range(len(haystack)):
                if haystack[index:index + len(needle)] == needle:
                    return index


if __name__ == '__main__':

    haystack = "aaaaa"
    needle = "a"
    # haystack = "hello"
    # needle = "ll"
    print(Solution().strStr_1(haystack, needle))


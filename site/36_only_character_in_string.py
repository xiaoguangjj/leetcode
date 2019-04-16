# -*- coding:utf-8 -*-

'''
字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
'''


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if s[i] not in s[i + 1:] and s[i] not in s[:i]:
                return i
        return -1

if __name__=='__main__':
    s = "loveleetcode"
    print(Solution().firstUniqChar(s))
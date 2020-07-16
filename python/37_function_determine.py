# -*- coding:utf-8 -*-

"""
有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。
"""


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def splitstr(x):
            y = []
            for i in range(len(x)):
                y.append(x[i])
            return y

        s = splitstr(s)
        t = splitstr(t)
        s.sort()
        t.sort()
        if s == t:
            return True
        return False


if __name__=='__main__':
    s = "anagram"
    t = "nagaram"
    # s = "rat"
    # t = "car"
    print(Solution().isAnagram(s, t))
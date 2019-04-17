# -*- coding:utf-8 -*-

"""
验证回文字符串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。
https://www.cnblogs.com/tianrunzhi/p/10382068.html
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(filter(str.isalnum, s)).lower()

        if s == s[::-1]:

            return True
        else:
            return False

if __name__=='__main__':
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))
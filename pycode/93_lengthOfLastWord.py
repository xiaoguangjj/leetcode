"""
58. 最后一个单词的长度
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。



示例:

输入: "Hello World"
输出: 5

https://leetcode-cn.com/problems/length-of-last-word/
"""


class Solution:
    def lengthOfLastWord(self, s):
        a = False
        if s.isspace() is True:
            return 0
        for i in s:
            if i == ' ':
                a = True
        if a is True:
            b = s.split(' ')
            l = b[::-1]
            try:
                for i in l:
                    if i != '':
                        print("16",len(i))
                        return len(i)
            except:
                return 0
        else:
            return len(s)

    def lengthOfLastWord2(self, s):
        s = s.split()
        if s:
            return len(s[-1])
        else:
            return 0


if __name__ == "__main__":
    # str = "a"
    # str = "a "
    str = " "
    s = Solution()
    print(s.lengthOfLastWord2(str))

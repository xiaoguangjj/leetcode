"""
387. 字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。



示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2


提示：你可以假定该字符串只包含小写字母。
"""
import collections


class Solution:
    #方法一：count计数
    def firstUniqChar(self, s):
        str_l = list(s) # 字符串列表化
        for i,item in enumerate(str_l):
            nums = s.count(item) # 每个项计数,count计数
            if nums == 1:
                return i # 返回索引
        return -1 # 查询不到时返回-1


    # 方法二：引用 collections.Counter()计数
    def firstUniqChar1(self, s):
        frequency = collections.Counter(s) # collections.Counter()计数
        for i, ch in enumerate(s):
            if frequency[ch] == 1:
                return i
        return -1


if __name__=="__main__":
    str = "loveleetcode"
    s = Solution()
    print(s.firstUniqChar1(str))

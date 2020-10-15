"""
1002. 查找常用字符
难度：简单
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。



示例 1：

输入：["bella","label","roller"]
输出：["e","l","l"]
示例 2：

输入：["cool","lock","cook"]
输出：["c","o"]

提示：

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] 是小写字母
"""


class Solution:
    def commonChars(self, A):
        minfreq = [float('inf')] * 26  # 26个字母构建的最小频率数组，数组中第几个数就是26个字母中，第几个字母，初始值是正无穷大inf
        for word in A:  # 第几个项
            freq = [0] * 26  # A 数组中所有字母出现的频率。每次循环都得到一个最小的
            for ch in word:  # 某一项的第几个字符
                freq[ord(ch) - ord('a')] += 1   # 用ascii码表示，第几个数就是第几个字母
            for i in range(26):
                minfreq[i] = min(minfreq[i], freq[i])
        print(minfreq)
        ans = list()
        for i in range(26):
            ans.extend(chr(i + ord('a')) * minfreq[i])  # chr(i + ord('a')) 数组第几个数字，转化成字母，
                                                        # 然后 * minfreq频率统计，出现几次，0次的 可以同时消项
                                                        # 由于minfreq已经是list了，所以用extend扩展收集每一项

        return ans


if __name__ == '__main__':
    str = ["bella", "label", "roller"]
    s = Solution()
    print(s.commonChars(str))

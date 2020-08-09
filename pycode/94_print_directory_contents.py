"""
写一个函数接收参数，返回该文件夹中的文件路径以及包含文件夹中文件的路径

"""
import os


class Solution:
    def print_directory_contents(self, sPath):
        """
        这个函数接受文件夹的名称作为输入参数，
        返回该文件夹中文件的路径，
        以及其包含文件夹中文件的路径。

        """
        for sChild in os.listdir(sPath):
            sChildPath = os.path.join(sPath, sChild)
            if os.path.isdir(sChildPath):
                print_directory_contents(sChildPath)
            else:
                print(sChildPath)

if __name__ == "__main__":
    # 地址写绝对路径
    path = "/Users/home/Program/leetcode/pycode"
    s = Solution()
    s.print_directory_contents(path)

"""
冒泡排序
原理

冒泡排序(Bubble Sort)是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。


步骤

冒泡排序算法的运作如下：

1、比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2、对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3、针对所有的元素重复以上的步骤，除了最后一个。
3、持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
参考资料: https://www.cnblogs.com/huang-yc/p/9774287.html
"""

import time


class Solution:
    # 冒泡排序
    def bubble_sort(self, list):
        length = len(list)
        # 第一级遍历
        for index in range(length):
            # 第二级遍历
            for j in range(1, length - index):
                # print("index:", index, "j:", j, "length - index:", length - index)
                if list[j - 1] > list[j]:
                    # 交换两者数据，这里没用temp是因为Python特性元组。
                    list[j - 1], list[j] = list[j], list[j - 1]
        return list

    # 有标志位的冒泡排序，如果本身是有序的，就不需要多次排序了，一次即可
    def bubble_sort_flag(self, list):
        lenght = len(list)
        for index in range(lenght):
            # 标志位
            flag = True
            for j in range(1, lenght - index):
                if list[j - 1] > list[j]:
                    list[j - 1], list[j] = list[j], list[j - 1]
                    flag = False
            if flag:
                return list
        return list

    def quick_sort(self, list):
        less = []
        pivotlist = []
        more = []
        #递归出口
        if len(list) <= 1:
            return list
        else:
            # 将第一个值作为基准
            pivot = list[0]
            for i in list:
                # 将比较值小的放到less数列
                if i < pivot:
                    less.append(i)
                # 将比较值大的值放到more数列
                elif i > pivot:
                    more.append(i)
                # 将和基准相同的值保存在基准数列
                else:
                    pivotlist.append(i)
            #对less数列和more数列继续进行排序
            less = self.quick_sort(less)
            more = self.quick_sort(more)
            return less + pivotlist + more


if __name__ == "__main__":
    list = [7, 2, 3, 8, 5, 6, 4, 10]
    s = Solution()
    print(s.bubble_sort(list))

    start = time.time()
    print(s.quick_sort(list))
    end = time.time()
    print(end-start)
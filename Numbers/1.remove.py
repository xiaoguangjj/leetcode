"""
删除列表中偶数
要求：不占用额外空间,一层循环
"""
lis = [1, 3, 4, 6, 67, 2, 12, 5, 4]


def is_odd(num):
    if num % 2 != 0:
        return True
    else:
        return False


def remove(lis):
    list1 = filter(lambda x: True if x % 2 else False, lis)
    return list1


def remove1(lis):
    return [x for x in lis if x % 2 !=0 ]


def remove2(lis):
    list1 = filter(is_odd, lis)
    return list(list1)

# 注意一个错误写法：
# 当出现两个连续的偶数时，删除其中一个，下一个会被隔过去。
# 例如[1, 3, 4, 6, 67, 2, 12, 5] 删除4时，指针在下标2处，6前移一位，占据下标2的位置，遍历指针指到3，那么6就被隔过去了。
def remove3(lis):
    for i in lis:
        if i % 2 == 0:
            lis.remove(i)
    return lis

if __name__ == "__main__":
    a = remove3(lis)
    print(a)

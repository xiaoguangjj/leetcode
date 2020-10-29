# -*- encoding: UTF-8 -*-

# 实现一个简单的迭代器
def test():
    for i in range(10):
        yield i + 100
        if i >= 1:
            return


if __name__=="__main__":
    for i in test():
        print(i)
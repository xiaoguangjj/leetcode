# -*- coding:utf-8 -*-

#排序问题，
# iteritems()以迭代器对象返回字典键值对，
# d[0]按照键值key排序，d[1]按照值value排序。
#reverse=False升序，reverse=False降序
def test():
    dic  = {'a':1,'b':2,'d':3,'c':4}
    dict = sorted(dic.iteritems(),key=lambda d:d[0],reverse=False)
    # print dic.iteritems(),dic.items()
    ff = float(12.123456789123456789)
    print ff

if __name__ == '__main__':
    test()
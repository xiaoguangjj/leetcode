# -*- coding: UTF-8 -*-


def test(a, b, *args, **kwargs):
    if args:
        print('args:',args)
    if kwargs:
        print('kwargs:',kwargs)

if __name__=='__main__':
    #args传递 已经定义的参数，中实参之外的参数
    #kwargs 只接收，未定义的参数
    test(1,2,3,x=1,y=2)

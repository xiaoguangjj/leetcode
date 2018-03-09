# -*-encoding:UTF-8 -*-

#装饰器实现 单例模式

def fun1(fun):
    print 'fun1 action'
    return fun

@fun1
def fun2():
    print 'fun2 action'

if __name__=="__main__":
    fun2()

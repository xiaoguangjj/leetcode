
def fun1(fun):
    print 'fun1 action'
    return fun

@fun1
def fun2():
    print 'fun2 action'

if __name__=="__main__":
    fun2()

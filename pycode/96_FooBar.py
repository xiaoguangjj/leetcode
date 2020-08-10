"""
1115. 交替打印FooBar
我们提供一个类：

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
两个不同的线程将会共用一个 FooBar 实例。其中一个线程将会调用 foo() 方法，另一个线程将会调用 bar() 方法。

请设计修改程序，以确保 "foobar" 被输出 n 次。



示例 1:

输入: n = 1
输出: "foobar"
解释: 这里有两个线程被异步启动。其中一个调用 foo() 方法, 另一个调用 bar() 方法，"foobar" 将被输出一次。
示例 2:

输入: n = 2
输出: "foobarfoobar"
解释: "foobar" 将被输出两次。

"""
import threading
empty=threading.Semaphore(1) # empty信号量初始值设为1  空缓冲区数量
full = threading.Semaphore(0) # full 信号量初始值设为0  满缓冲区数量
'''信号量为0时，不可被减，同时信号量不设上限
所以需要两个信号量empty、full共同监测两个边界[0,1]'''


def printFoo():
    print("foo")


def printBar():
    print("bar")


class FooBar:
    def __init__(self, n):
        self.n = n

    def foo(self, printFoo):
        for i in range(self.n):
            empty.ecquire() # empty-1，申请一个空缓冲区，有空位时应执行生产者活动
            printFoo()
            full.release() # full+1，释放一个满缓冲区

    def bar(self, printBar):
        for i in range(self.n):
            full.acquire()  # full-1, 申请一个满缓冲区，当缓冲区有商品时才能实现消费者行为
            printBar()
            empty.release()  # empty+1，释放一个空缓冲区


if __name__ == "__main__":
    f = FooBar(2)
    f.bar(printBar())
    f.foo(printFoo())

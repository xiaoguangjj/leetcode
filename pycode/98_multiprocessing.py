# 创建并开启进程的两种方法

# 方法一 直接调用
import time, json
import random
from multiprocessing import Process, Lock, Queue, Pipe, JoinableQueue, Manager,Semaphore, Event,Pool
import os
from socket import *
import requests


def run(name):
    print('%s running' %name)
    time.sleep(random.randrange(1,5))
    print('%s running end' %name)


p1 = Process(target=run,args=('anne',))
p2 = Process(target=run,args=('alice',))
p3 = Process(target=run,args=('lisa',))
p4 = Process(target=run,args=('dei',))

p1.start()
p2.start()
p3.start()
print('主线程')


# 方法二 继承式调用


class Run(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('%s running' % self.name)
        time.sleep(random.randrange(1, 3))
        print('%s running end' % self.name)


p1 = Run('anne')
p2 = Run('alex')
p3 = Run('ab')
p4 = Run('hey')
p1.start()  # start会自动调用run
p2.start()
p3.start()
p4.start()
print('主线程')

# Process对象的join方法


class Run(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name
        print('%s running' % self.name, os.getpid(), os.getppid())

    def run(self):
        print('%s running' % self.name, os.getpid(), os.getppid())  # getpid()获取当前进程id，getppid()获取父进程 id
        time.sleep(random.randrange(1, 3))
        print('%s running end' % self.name)


p1 = Run('anne')
p2 = Run('alex')
p3 = Run('ab')
p4 = Run('hey')
p1.start()  # start会自动调用run
p2.start()
p3.start()
p4.start()
p1.join()  # 等待p1进程停止
p2.join()
p3.join()
p4.join()
print('主线程')


# 守护进程
# 1）守护进程会在主进程代码执行结束后就终止
# 2）守护进程内无法再开启子进程，否则抛出异常：AssertionError:


class Run(Process):
    def __init__(self, name):
        self.name = name
        super().__init__()

    def run(self):
        print('%s is piaoing' % self.name)
        time.sleep(random.randrange(1, 3))
        print('%s is piao end' % self.name)


p = Run('anne')
p.daemon = True  # 一定要在p.start()前设置，设置p为守护进程，禁止p创建子进程，并且父进程代码执行结束
p.start()
print('主')

# 主进程代码进行完毕，守护进程就会结束


def foo():
    print(123)
    time.sleep(1)
    print("end123")


def bar():
    print(456)
    time.sleep(3)
    print("end456")


p1 = Process(target=foo)
p2 = Process(target=bar)

p1.daemon = True
p1.start()
p2.start()
print("main---------")

# 并发运行，效率高，但竞争同一打印终端，带来了打印错乱


def work():
    print('%s is running' %os.getppid())
    time.sleep(2)
    print('%s is done' %os.getpid())


if __name__ == '__main__':
    for i in range(3):
        p = Process(target=work)
        p.start()
        

# 由并发变成了串行，牺牲了运行效率，但避免了竞争


def work(lock):
    lock.acquire()
    print('%s is running' % os.getpid())
    time.sleep(2)
    print('%s is done' % os.getpid())
    lock.release()


if __name__ == '__main__':
    lock = Lock()
    for i in range(3):
        p = Process(target=work, args=(lock, ))
        p.start()


def search():
    dic = json.load(open('/Users/home/Documents/a.txt'))
    print('剩余票数%s' % dic['count'])


def get():
    dic = json.load(open('/Users/home/Documents/a.txt'))
    time.sleep(0.1)  # 模拟读数据的网络延迟
    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(0.2)  # 模拟写数据的网络延迟
        json.dump(dic, open('/Users/home/Documents/a.txt', 'w'))
        print('购票成功')


def task(lock):
    search()
    get()


if __name__ == '__main__':
    lock = Lock()
    for i in range(100):  # 模拟并发100个客户端抢票
        print('客户编号：%s' % i)
        # p = Process(target=task, args=(lock,))
        # p.start()
        task(lock)

# 购票行为由并发变成了串行，牺牲了运行效率，但保证了数据安全

def search():
    dic=json.load(open('/Users/home/Documents/a.txt'))
    print('剩余票数 %s' % dic['count'])

def get():
    dic=json.load(open('/Users/home/Documents/a.txt'))
    time.sleep(0.1)  # 模拟读数据的网络延时
    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(0.2) # 模拟写数据的网络延迟
        json.dump(dic, open('/Users/home/Documents/a.txt', 'w'))
        print('购票成功')

def task(lock):
    search()
    lock.acquire() # 获取锁
    get()
    lock.release() # 释放锁


if __name__=='__main__':
    lock = Lock()
    for i in range(100): # 模拟并发100个客户端抢票
        p=Process(target=task,args=(lock,))
        p.start()
# Queue():创建共享的进程队列，Queue是多线程安全的队列，可以使用Queue实现多线程之间的数据传递
q = Queue(3)

# put ,get , put_nowait,get_nowait,full,empty
q.put(3)
q.put(3)
q.put(3)
print(q.full())  # 满了

print(q.get())
print(q.get())
print(q.get())
print(q.empty()) # 空了

#  生产者消费者模式


def consumer(q):
    while True:
        res = q.get()
        if res is None: break  # 收到结束信号则结束
        time.sleep(random.randint(1,3))
        print('\033[41;45m%s 吃 %s\033[0m' % (os.getpid(), res))


def producer(q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res = '包子%s' %i
        q.put(res)
        print('\033[41;44m%s 生产了 %s\033[0m' % (os.getpid(), res))
    q.put(None)  # 发送结束信号


if __name__ == '__main__':
    q = Queue()
    # 生产者们：即厨师们
    p1 = Process(target=producer,args=(q,))

    # 消费者们：即吃货们
    c1 = Process(target=consumer,args=(q,))

    # 开始
    p1.start()
    c1.start()
    print('主')

#  结束信号None，不一定要由生产者发，主线程里同样可以发，但主进程需要等生产者结束后才应该发送该信号


def consumer(q):
    while True:
        res = q.get()
        if res is None: break  # 收到结束信号则结束
        time.sleep(random.randint(1,3))
        print('\033[45m%s 吃 %s\033[0m' %(os.getpid(), res))


def producer(q):
    for i in range(2):
        time.sleep(random.randint(1,3))
        res = '包子%s' %i
        q.put(res)
        print('\033[44m%s 生产了 %s\033[0m' %(os.getpid(), res))


if __name__=='__main__':
    q = Queue()
    # 生产者们
    p1 = Process(target=producer, args=(q,))

    # 消费者们
    c1 = Process(target=consumer, args=(q,))

    # 开始
    p1.start()
    c1.start()

    p1.join()
    q.put(None)  # 发送结束信号
    print('主')


def consumer(q):
    while True:
        res=q.get()
        if res is None:break  #收到结束信号则结束
        time.sleep(random.randint(1,3))
        print('\033[45m%s 吃 %s\033[0m' %(os.getpid(), res))


def producer(name, q):
    for i in range(2):
        time.sleep(random.randint(1,3))
        res = '%s%s' %(name,i)
        q.put(res)
        print('\033[44m%s 生产了 %s\033[0m' %(os.getpid(), res))


if __name__ == '__main__':
    q = Queue()

    # 生产者们
    p1 = Process(target=producer,args=('包子', q))
    p2 = Process(target=producer,args=('油条', q))
    p3 = Process(target=producer,args=('馒头', q))

    # 消费者们
    c1 = Process(target=consumer, args=(q,))
    c2 = Process(target=consumer, args=(q,))

    # 开始
    p1.start()
    p2.start()
    p3.start()
    c1.start()

    p1.join()  # 必须保证生产者全部生产完毕，才应该发送结束信号
    p2.join()
    p3.join()
    q.put(None)  # 有几个消费者就应该发送几次结束信号None
    q.put(None)  # 发送结束信号
    print('主')


def consumer(q):
    while True:
        res = q.get()
        time.sleep(random.randint(1,3))
        print('\033[45m%s 吃 %s\033[0m' %(os.getpid(), res))
        q.task_done()  # 此方法发信号


def producer(name, q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res = '%s%s' %(name, i)
        q.put(res)
        print('\033[44m%s 生产了 %s\033[0m' %(os.getpid(),res))
    q.join()


if __name__=='__main__':
    q = JoinableQueue()
    # 生产者们
    p1 = Process(target=producer,args=('包子', q))
    p2 = Process(target=producer,args=('骨头', q))
    p3 = Process(target=producer,args=('油条', q))

    # 消费者们
    c1 = Process(target=consumer, args=(q,))
    c2 = Process(target=consumer, args=(q,))
    c1.daemon = True  # 守护进程，进程结束直接结束
    c2.daemon = True

    # 开始
    p_1 = [p1, p2, p3, c1, c2]
    for p in p_1:
        p.start()

    p1.join()  # 带执行join（）的进程结束后再继续执行主进程
    p2.join()
    p3.join()
    print('主')


# 管道


def consumer(p,name):   # 消费者
    left, right = p
    left.close()
    while True:
        try:
            baozi = right.recv()
            print('%s 收到包子：%s' % (name, baozi))
        except EOFError:
            right.close()
            break


def producer(seq, p):   # 生产者
    left, right=p
    right.close()
    for i in seq:
        left.send(i)
        time.sleep(1)
    else:
        left.close()


if __name__ == '__main__':
    left, right = Pipe()
    c1 = Process(target=consumer, args=((left, right), 'c1'))
    c1.start()

    seq = (i for i in range(10))
    producer(seq, (left, right))

    right.close()
    left.close()

    c1.join()
    print('主线程')


def adder(p, name):
    server, client = p
    # client.close()
    while True:
        try:
            x, y = server.recv()
        except EOFError:
            server.close()
            break
        res = x+y
        server.send(res)
    print('server done')


if __name__ == '__main__':
    server, client = Pipe()

    c1 = Process(target=adder, args=((server, client), 'c1'))
    c1.start()

    server.close()

    client.send((10, 20))
    print('client recv:', client.recv())
    client.close()

    c1.join()
    print('主进程')

# 注意：send()和recv()方法使用pickle模块对对象进行序列化


def work(d, lock):
    with lock: # 不加锁而操作共享数据。肯定会出现数据混乱
        d['count']-=1


if __name__ == '__main__':
    lock = Lock()
    with Manager() as m:
        dic = m.dict({'count':100})
        p_1 = []
        for i in range(100):
            p = Process(target=work, args=[dic, lock])
            p_1.append(p)
            p.start()
        for p in p_1:
            p.join()  # 阻塞直到结束
        print(dic)


# 信号量

def go_wc(sem,user):
    sem.acquire()  # 锁住进程
    print('%s 占到一个位置' % user)
    time.sleep(random.randint(1, 3))
    sem.release()  # 解锁进程


if __name__ == '__main__':
    sem = Semaphore(5)
    p_1 = []
    for i in range(13):
        p=Process(target=go_wc,args=(sem,'user%s' %i,))
        p.start()
        p_1.append(p)

    for i in p_1:
        i.join()
    print('============>')


# 事件
# 事件处理的机制：全局定义了一个“Flag”，如果“Flag”值为 False，那么当程序执行 event.wait 方法时就会阻塞，
# 如果“Flag”值为True，那么event.wait 方法时便不再阻塞。
# clear:将"Flag"设置为False
# set:将"Flag"设置为True


def car(e, n):
    while True:
        if not e.is_set():  # False
            print('\033[31m红灯亮\033[0m，car%s等着' %n)
            e.wait()
            print('\033[32m车%s 看见绿灯亮了\033[0m' %n)
            time.sleep(random.randint(3,6))
            if not e.is_set():
                continue
            print('走你,car', n)
            break


def police_car(e,n):
    while True:
        if not e.is_set():  # False
            print('\033[31m红灯亮\033[0m，car%s等着' % n)
            e.wait(1)
            print('灯的是%s，警车走了,car %s' %(e.is_set(),n))
            break


def traffic_lights(e, inverval):
    while True:
        time.sleep(inverval)
        if e.is_set():
            e.clear()  # e.is_set()   ---->False
        else:
            e.set()    # e.is_set()   ---->True


if __name__ == '__main__':
    e = Event()
    for i in range(10):
        p = Process(target=car, args=(e, i,))
        p.start()

    for i in range(5):
        p = Process(target=police_car, args=(e, i,))
        p.start()

    t = Process(target=traffic_lights, args=(e, 10))
    t.start()
    print('===========>')

#  进程池


def work(n):
    print('%s run' %os.getpid())
    time.sleep(3)
    return n**2


if  __name__ == '__main__':
    p = Pool(3)
    res_l = []
    for i in range(10):
        res=p.apply(work,args=(i,))
        res_l.append(res)
    print(res_l)


#  使用线程池（异步调用, apply_async）


def func(msg):
    print("msg:", msg)
    time.sleep(1)
    return msg


if __name__ == "__main__":
    pool = Pool(processes = 3)
    res_l = []
    for i in range(10):
        msg = "hello %d" % (i)
        res = pool.apply_async(func, (msg,))  # 异步运行，维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
        res_l.append(res)
    print("==============================>")

    pool.close()  # 关闭进程池，防止进一步操作。如果所有操作持续挂起，它们将在工作进程终止前完成
    pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print(res_l)  # 看到的是<multiprocessing.pool.ApplyResult object at 0x10357c4e0>对象组成的列表,而非最终的结果,
    # 但这一步是在join后执行的,证明结果已经计算完毕,剩下的事情就是调用每个对象下的get方法去获取结果
    for i in res_l:
        print(i.get())  # 使用get来获取apply_aync的结果,如果是apply,则没有get方法,因为apply是同步执行,立刻获取结果,也根本无需get


#  二：使用线程池（同步调用, apply）


def func(msg):
    print("msg:", msg)
    time.sleep(0.1)
    return msg


if __name__ == "__main__":
    pool = Pool(processes=3)
    res_l = []
    for i in range(10):
        msg = "hello %d" % (i)
        res = pool.apply(func,(msg,))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
        res_l.append(res)  # 同步执行，即执行完一个拿到结果，再去执行另外一个
    print("=================>")
    pool.close()
    pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束

    print(res_l)  # 看到的就是最终的结果组成的列表
    for i in res_l:
        print(i)

#  使用进程池维护固定数目的进程

# server 端
server = socket(AF_INET,SOCK_STREAM)  # IPv4 网络协议的套接字类型，提供面向连接的稳定数据传输，SOCK_STREAM 套接字
server.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)  # SOL_SOCKET 套接字描述符，SO_REUSEADDR是让端口释放后立即就可以被再次使用
server.bind(('127.0.0.1', 8080))
server.listen(5)


def talk(conn, client_addr):
    print('进程pid: %s' % os.getpid())
    while True:
        try:
            msg = conn.recv(1024)
            if not msg:break
            conn.send(msg.upper())
        except Exception:
            break


if __name__ == '__main__':
    p = Pool()
    while True:
        conn, client_addr = server.accept()
        p.apply_async(talk,args=(conn,client_addr))
        # p.apply(talk,args=(conn,client_addr))  # 同步的话，则同一时间只有一个客户端能访问


# client 端
client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

while True:
    msg = input('>>: ').strip()
    if not msg: continue

    client.send(msg.encode('utf-8'))
    msg = client.recv(1024)
    print(msg.decode('utf-8'))


# 回调函数
# 需要回调函数的场景：进程池中任何一个任务一旦处理完了，就立即告知主进程：我好了额，你可以处理我的结果了。


def get_page(url):
    print('<进程%s> get %s' %(os.getpid(),url))
    respone = requests.get(url)
    if respone.status_code == 200:
        return {'url': url, 'text': respone.text}


def pasrse_page(res):
    print('<进程%s> parse %s' %(os.getpid(), res['url']))
    parse_res = 'url:<%s> size:[%s]\n' % (res['url'], len(res['text']))
    with open('/Users/home/Docunments/a.txt', 'a') as f:
        f.write(parse_res)


if __name__ == '__main__':
    urls = [
        'https://www.baidu.com',
        'https://www.python.org',
        'https://www.openstack.org',
        'https://help.github.com/',
        'http://www.sina.com.cn/'
    ]
    p = Pool(3)
    res_l = []
    for url in urls:
        res = p.apply_async(get_page, args=(url,), callback=pasrse_page)
        res_l.append(res)

    p.close()
    p.join()
    print([res.get() for res in res_l])  # 拿到的是get_page的结果,其实完全没必要拿该结果,该结果已经传给回调函数处理了


# 如果在主进程中等待进程池中所有任务都执行完毕后，再统一处理结果，则无需回调函数


def work(n):
    time.sleep(1)
    return n**2


if __name__=='__main__':
    p = Pool()

    res_l=[]
    for i in range(10):
        res=p.apply_async(work,args=(i,))
        res_l.append(res)

    p.close()
    p.join()  # 等待进程池中所有进程执行完毕

    nums = []
    for res in res_l:
        nums.append(res.get())  # 拿到所有结果
    print(nums)  # 主进程拿到所有的处理结果,可以在主进程中进行统一进行处理

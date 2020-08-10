"""
有A.txt 和 B.txt 两个文件，使用多个进程分别读取这两个文件
"""

import time
import random
from multiprocessing import Process


def run1(name):
    # print('%s running' %name)
    # time.sleep(random.randrange(1,3))
    # print('%s running end' % name)
    with open('/Users/home/Documents/a.txt', encoding='utf-8') as f:
        print(f.read())


def run2(name):
    # print('%s running' %name)
    # time.sleep(random.randrange(1,3))
    # print('%s running end' % name)
    with open('/Users/home/Documents/b.txt', encoding='utf-8') as f:
        print(f.read())


p1=Process(target=run1,args=('1',))
p2=Process(target=run2,args=('2',))

p1.start()
p2.start()
print('主线程')
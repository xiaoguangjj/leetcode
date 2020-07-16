# -*-encoding:UTF-8 -*-

#生产者消费者模式

def consumer():
    while True:
        v = yield
        print "consume: ", v

def producer(c):
    for i in range(10, 13):
        c.send(i)


if __name__=="__main__":
    # c = consumer()  #   创建消费者
    # c.send(None)    #   启动消费者
    # producer(c)     #   生产者发送数据
    # c.close()       #   关闭消费者
    a = {1:2}
    print a[1]

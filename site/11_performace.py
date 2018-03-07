# -*- coding: UTF-8 -*-
from io import StringIO
import time

#计算运行时间
loop_count = 800000

def m1():
    start_time = time.time()
    out_str = ''
    for num in xrange(loop_count):
        out_str += 'chaomeng'
    print time.time() - start_time
    return out_str

def m2():
    start_time = time.time()
    str_list = []
    for num in xrange(loop_count):
        str_list.append('chaomeng')
    out_str = ''.join(str_list)
    print time.time() - start_time
    return out_str

def m3():
    start_time = time.time()
    file_str = StringIO()
    # file_str = BytesIO()
    for num in xrange(loop_count):
        file_str.write(u'chaomeng')
    out_str = file_str.getvalue()
    print time.time() - start_time
    return out_str

def m4():
    start_time = time.time()
    out_str = ''.join(['chaomeng' for num in xrange(loop_count)])
    # print time.time() - start_time
    return out_str

if __name__ == '__main__':
    # import profile
    # profile.run('m1()')
    # profile.run('m2()')
    # profile.run('m3()')
    # profile.run('m4()')
    # m1()
    # m2()
    # m3()
    print(m4())

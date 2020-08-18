"""
一个大小为100G的文件，要读取文件中的内容

"""

"""
方法一：
利用open（）系统自带方法生成的迭代对象
"""

"""
with open('/Users/home/Documents/a.txt', encoding='utf-8') as f:
    for line in f:
        print(line)
"""

"""
方法二：
将文件切成小段，每次处理完小段内容后，释放内存
这里会使用yield生产自定义可迭代对象，即generator,每一个带有yield的函数就是一个generator
"""


def read_in_block(file_path):
    BLock_SIZE = 1024
    with open(file_path, encoding='utf-8') as f:
        while True:
            block = f.read(BLock_SIZE)  # 每次读取固定长度到内存缓存区
            if block:
                yield block
            else:
                return  # 如果读取到文件末尾，则退出


file_path = "/Users/home/Docunments/a.txt"
for block in read_in_block(file_path):
    print(block)

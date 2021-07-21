import math
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor


PRIMES = [112272535095293] * 100


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def single_thread():
    for number in PRIMES:
        is_prime(number)


def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


if __name__ == "__main__":

    start = time.time()
    single_thread()
    end = time.time()
    print("single_thread, cost", end - start, "seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi_thread, cost", end - start, "seconds")

    start = time.time()
    multi_process()
    end = time.time()
    print("multi_process, cost", end - start, "seconds")

    """
    执行结果：
    single_thread, cost 57.102088928222656
    multi_thread, cost 50.913933992385864
    multi_process, cost 28.768413066864014
    
    结论：
    cpu密集型，执行速度:  多进程 > 多线程 > 单线程 
    """
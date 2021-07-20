import threading
import time

lock = threading.Lock()


class Account:
    def __init__(self, balance):
        self.balance = balance


def draw(account, amount):
    # 1、若没有lock，没有time.sleep时，有时间出问题，有时候不出问题
    # 2、若没有lock，有time.sleep时，线程a阻塞，执行b-800=200，再执行-800一定出错
    with lock:
        if account.balance > amount:
            time.sleep(0.1)
            print(threading.current_thread().name, "取钱成功")

            account.balance -= amount
            print(threading.current_thread().name, "余额", account.balance)

        else:
            print(threading.current_thread().name, "取钱失败，余额不足")


if __name__ == "__main__":
    account = Account(1000)
    ta = threading.Thread(name="ta",target=draw, args=(account,800))
    tb = threading.Thread(name="tb", target=draw, args=(account, 800))

    ta.start()
    tb.start()
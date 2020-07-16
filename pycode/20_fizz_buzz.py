# -*-encoding:UTF-8 -*-

# outputs the string representation of numbers from 1 to n.
# 3的倍数 用Fizz替代，5的倍数用Buzz替代


def Fizz(n):
    """

    :param n:
    :return:
    """
    a = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 != 0:
            i = "Fizz"
        elif i % 5 == 0 and i % 3 != 0:
            i = "Buzz"
        elif i% 15 == 0:
            i = "FizzBuzz"

        a.append(i)

    return a


def fizzBuzz(n):
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]

if __name__=="__main__":
    n = 35
    # print Fizz(n)

    # print fizzBuzz(n)

"""fib function"""


def fib(n: int) -> int:
    '''
    Fib
    '''
    if n == 1 or n == 2:
        return n-1
    res = fib(n-1) + fib(n-2)
    return res


print(fib(10))

from datetime import datetime
from decors import decorator_param, decorator


@decorator
def general(n):
    numbers = [item for item in range(1, n)]
    return numbers



@decorator_param(path='main.log')
def general(n):
    numbers = [item for item in range(1, n)]
    return numbers

general(5)
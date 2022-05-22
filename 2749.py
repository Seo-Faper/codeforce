import math
def fibo(n):
    # 공식을 활용한 버전
    # 상수시간이므로 O(1)
    root5 = pow(5, 0.5)
    ratio = (1 + root5) / 2
    return int((pow(ratio, n) - pow(1 - ratio, n)) / root5) % 1000000
n = int(input())
print(fibo(n))


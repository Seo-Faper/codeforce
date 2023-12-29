'''
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]


'''
import sys
import re
from collections import deque
def solution():
    p = sys.stdin.readline().replace("\n", "")
    n = int(sys.stdin.readline())
    numbers = sys.stdin.readline().replace("\n","")[1:-1].split(",")
    numbers = list(filter(len, numbers))
    #print("number 배열 : ",end='')
    #print(numbers)
    t = 0
    for i in p:
        if i =='R':
            t +=1
        elif i == 'D' and numbers:
          #  print(numbers)
           # print("!")
            numbers.pop(-(t%2))
        else:
            print("error")
            return
    if t%2 != 0 : numbers.reverse()

    print(str(numbers).replace(" ", "").replace("'",""))
T = int(input())
for i in range(T):
    solution()
import random
from time import time

random.seed(10000)


s = ['e', 'l', 'h', 'l', 'o']
l = [*range(len(s))]

random.shuffle(l)
print(s)
print(l)
d = [0]*len(s)
for i, x in enumerate(l):
    print(str(i)+" -> "+str(x))
    d[x] = s[i]
print(d)

import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque()

for i in range(n):
    command = sys.stdin.readline()[:-1]

    if command.startswith("push_front"):
        q.appendleft(command.split(" ")[1])
    elif command.startswith("push_back"):
        q.append(command.split(" ")[1])
    elif command =="pop_back":
        if q:
            print(q.pop())
        else: print(-1)
    elif command == "pop_front":
        if q:
            print(q.popleft())
        else: print(-1)
    elif command == "size":
        print(len(q))
    elif command == "empty":
        if q: print(0)
        else: print(1)
    elif command == "front":
        if q:
            print(q[0])
        else: print(-1)
    else:
        if q:
            print(q[len(q)-1])
        else: print(-1)
'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
import sys
n = int(sys.stdin.readline())
q = []
front = 0
back = -1
for i in range(n):
    command = sys.stdin.readline()[:-1]
    if command.startswith("push"):
        q.append(command.split(" ")[1])
        back+=1
    elif command == "pop":
        if back-front != -1:
            print(q[front])
            front +=1
        else: print(-1)
    elif command == "size":
        print(back-front+1)
    elif command == "empty":
        if back-front != -1: print(0)
        else: print(1)
    elif command == "front":
        if back-front != -1:
            print(q[front])
        else: print(-1)
    else:
        if back-front != -1:
            print(q[back])
        else: print(-1)
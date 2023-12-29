N = int(input())
for i in range(1,N+1):
    for j in reversed(range(1,N-i+1)):
        print(' ',end='')
    for j in range(i):
        print('* ',end='')
    print()
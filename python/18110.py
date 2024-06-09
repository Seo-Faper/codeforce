import sys
input = sys.stdin.readline
def round_x(number):
    if number - int(number) >= 0.5:
        return int(number) + 1
    else:
        return int(number)
N = int(input())
if N == 0: print(0)
else:
    level = sorted([int(input()) for _ in range(N)])
    cut = round_x(( N*0.3 ) / 2)
    if cut != 0:
        level = level[cut:-cut]
    print(level)
    print(round_x(sum(level)/len(level)))
import sys
while True:
    S = sys.stdin.readline().replace("\n","")
    if S =="END": break
    print(S[::-1])
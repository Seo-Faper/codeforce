import sys
input = sys.stdin.readline
def main():
    n = int(input())
    
    count = n // 5
    
    remainder = n % 5
    
    if remainder == 0:
        print(count)
    elif remainder == 1 or remainder == 3:
        print(count + 1)
    elif remainder == 2:
        if count < 2:
            print(-1)
        else:
            print(count + 2)
    elif remainder == 4:
        if count < 1:
            print(-1)
        else:
            print(count + 2)

if __name__ == "__main__":
    main()


def split_array(arr):
    a = []
    b = []
    arr = sorted(arr,reverse=True)
    a.append(arr[0])
    arr = arr[1:]
    for i in arr:
        for j in a:
            if i % j == 0:
                a.append(i)
                break
            else:
                b.append(i)
                break
 #   print(arr)
    return b, a

def main():
    t = int(input())  # 테스트 케이스 수

    for _ in range(t):
        n = int(input())  # 배열의 길이
        p = list(map(int, input().split()))  # 배열 요소

        a, b = split_array(p)
        if len(a) >= 1 and len(b) >= 1:
            print(len(a), len(b))
            print(" ".join(map(str, a)))
            print(" ".join(map(str, b)))
        else:
            print(-1)
        
if __name__ == "__main__":
    main()

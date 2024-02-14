n = int(input())
for i in range(n):
    a = input()
    b = input()
    ans = 0
    for j in range(len(a)):
        if a[j] != b[j]: ans +=1
    print("Hamming distance is "+str(ans)+".")
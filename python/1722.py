def find_kth_permutation(n, k):
    fact = [1] * n
    for i in range(1, n):
        fact[i] = fact[i - 1] * i
    numbers = list(range(1, n + 1))
    k -= 1 
    ans = []
    for i in range(n, 0, -1):
        index = k // fact[i - 1]
        ans.append(numbers.pop(index))
        k %= fact[i - 1]
    return ans

def find_permutation_rank(n, arr):
    fact = [1] * n
    for i in range(1, n):
        fact[i] = fact[i - 1] * i
    rank = 1
    for i in range(n):
        smaller_count = 0
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                smaller_count += 1
        rank += smaller_count * fact[n - i - 1]
    return rank

N = int(input())
l = list(map(int, input().split()))
if l[0] == 1:
    k = l[1]
    print(*find_kth_permutation(N, k))
else:
    arr = l[1:]
    print(find_permutation_rank(N, arr))

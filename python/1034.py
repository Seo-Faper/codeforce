
"""
01
10
10 
에서 2번째 행의 0을 키게 되면 해당 열의 모든 비트가 반전되어서

00
11
11
이 되므로, 최대로 켜진 행의 개수는 2개가 된다.

이걸 어떻게 알 수 있을까?

어떤 자리의 비트를 키는 횟수는 k번 정의 된다.
즉, 반드시 k번의 열 반전이 일어난다.

한 비트라도 바꾸게 되면 어차피 모든 행이 바뀌게 되므로
동일한 행의 비트의 개수가 최대값이 될 가능성이 높다.

10이 2개 있기 때문에 10만 11로 바꿀 수 있으면 2개가 되듯

한 줄씩 입력을 받을 때 동일한 비트의 개수를 기록해 주고
가장 큰 비트의 0의 개수를 세었을 때, k보다 작거나 같으면
해당 비트는 모두 1로 바꿀 수 있음을 의미한다.
만약 k보다 크면 다음 많은 비트의 0의 개수를 세면 된다.

1000 이 3개 , k가 4면 
반드시 바꿔야 하기 때문에
k를 3번 써서 1111을 만들었더라도
k 1회가 남았기 때문에 1111을 만들 수 없다.
즉, 각 비트의 0의 개수를 p 라고 했을 때

p%2 == k%2 and p <= k를 만족해야 한다.

둘 다 짝수던지, 둘 다 홀수던지 해야 모두 1로 만들 수 있다.

0 | 1 -> 0 -> 1 
총 3번 필요

00 | 01 -> 11
총 2번 필요

"""

n,m = map(int, input().split())
bits = dict()
lights = [input() for _ in range(n)]
c = int(input())
for i in lights:
    if i in bits:
        bits[i] += 1
    else:
        bits[i] = 1
ans = 0
for k,v in bits.items():
    p = k.count('0')
    if p % 2 == c % 2 and p <= c:
        ans = max(ans, v)
print(ans)
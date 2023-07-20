N, M = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

pointA = 0
pointB = 0
ans = []

while pointA < N and pointB < M:
    if A[pointA] < B[pointB]:
        ans.append(A[pointA])
        pointA += 1
    else:
        ans.append(B[pointB])
        pointB += 1


while pointA < N:
    ans.append(A[pointA])
    pointA += 1

while pointB < M:
    ans.append(B[pointB])
    pointB += 1

print(*ans)

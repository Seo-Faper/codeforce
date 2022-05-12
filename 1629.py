def fpow(C, n, m):
	if n == 1:
		return C
	else:
		x = fpow(C, n//2,m)
		if n % 2 == 0:
			return x * x % m
		else:
			return x * x * C % m


A,B,C = map(int, input().split())
print(fpow(A,B,C) % C )

# 2147483647
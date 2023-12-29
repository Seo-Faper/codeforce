def long_division(A, B, N):
    quotient = []
    remainder = A
    for _ in range(1000001): 
        digit = remainder // B
        quotient.append(str(digit))
        remainder = (remainder - digit * B) * 10
      #  print(digit,end='')
    return "".join(quotient[N])

A,B,N = map(int,input().split())

result = long_division(A, B, N)
print(result)

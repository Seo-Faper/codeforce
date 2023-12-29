import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollard_rho(N):
    if N % 2 == 0:
        return 2

    x, y, d = 2, 2, 1
    f = lambda x: (x**2 + 1) % N

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), N)

    return d

def find_longest_consecutive_sequence(N):
    # 주어진 자연수 N의 최대 소인수를 구함
    max_prime_factor = pollard_rho(N)

    # 연속된 수열의 시작값을 결정 (N의 최대 공약수의 배수)
    start_value = max_prime_factor

    # 연속된 수열의 길이를 구함
    max_length = 1
    current_length = 1

    while True:
        # 다음 값이 N으로 나누어 떨어지는지 확인하여 연속된 수열의 길이를 계산
        if (start_value + max_prime_factor) % N == 0:
            current_length += 1
        else:
            current_length = 1

        # 연속된 수열의 길이를 최대로 확장
        max_length = max(max_length, current_length)

        # 연속된 수열의 끝에 도달하면 종료
        if current_length == max_prime_factor:
            break

        # 다음 연속된 수열의 시작값으로 이동
        start_value += max_prime_factor

    return max_length

# 예시 사용
N = 1000000000000000000  # 10^18
result = find_longest_consecutive_sequence(N)
print(result)  # 출력: 해당 자연수에 대한 가장 긴 연속된 수열의 길이

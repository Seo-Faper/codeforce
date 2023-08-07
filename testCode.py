def round_kth_digit(n, k):
    num_str = str(n)
    
    if k >= len(num_str):
        return n
    
    digit_value = int(num_str[k])
    
    if digit_value >= 5:
        return n + 10 ** (len(num_str) - k)
    else:
        return n - (n % (10 ** (len(num_str) - k)))

n = int(input("자연수 입력: "))
k = int(input("반올림할 자리 입력: "))

result = round_kth_digit(n, k)
print("반올림 결과:", result)

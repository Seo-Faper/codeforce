def solution(s):
    ans = len(s)+1
    for i in s:
        if i =='1': ans+=2
        elif i=='0': ans+=4
        else: ans+=3
    return ans
while True:
    n = input()
    if n == '0' : break
    print(solution(n))
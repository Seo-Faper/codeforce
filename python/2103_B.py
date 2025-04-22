for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    init = "0"
    # 1) 기본 이동 비용 계산
    #   I: 첫 글자가 init("0")와 다르면 1, 같으면 0
    I = 1 if s[0] != init else 0
    #   T: 인접 문자가 달라질 때마다 1씩 추가
    T = sum(1 for i in range(1, n) if s[i] != s[i-1])
    M = I + T

    # 2) 접두사 뒤집기로 줄일 수 있는 최대량
    best_pref = 0
    for r in range(n):
        # 경계점 r<->r+1 전후 비교
        if r < n-1:
            orig = int(s[r] != s[r+1])
            newb = int(s[0] != s[r+1])
        else:
            orig = 0
            newb = 0
        deltaT = orig - newb
        deltaI = I - (1 if s[r] == '1' else 0)
        best_pref = max(best_pref, deltaT + deltaI)

    # 3) 접미사 뒤집기로 줄일 수 있는 최대량
    best_suf = 0
    for l in range(1, n):
        orig = int(s[l-1] != s[l])
        newb = int(s[l-1] != s[-1])
        best_suf = max(best_suf, orig - newb)

    # 4) 내부 뒤집기로 줄일 수 있는 최대량 (동일한 전환 쌍이 두 번 이상 있으면 2)
    cnt01 = sum(1 for i in range(1, n) if s[i-1]=='0' and s[i]=='1')
    cnt10 = sum(1 for i in range(1, n) if s[i-1]=='1' and s[i]=='0')
    best_internal = 2 if (cnt01 >= 2 or cnt10 >= 2) else 0

    # 5) 최종 최대 감소량
    best_delta = max(0, best_pref, best_suf, best_internal)
    print(n + M - best_delta)

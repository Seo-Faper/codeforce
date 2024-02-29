T = int(input())  # 테스트 케이스의 수
for _ in range(T):
    n = int(input())  # 문자열의 길이
    s = [input() for _ in range(2)]  # 두 문자열 입력 받기
    
    # 사전 순으로 가장 앞서는 문자열과 그 개수를 저장할 변수
    min_str = ''
    count = 1
    
    # 두 문자열을 한 번씩만 순회하며 최소 문자열 생성
    for i in range(n):
        if s[0][i] < s[1][i]:  # 첫 번째 행의 문자가 더 작은 경우
            min_str += s[0][i]
        elif s[0][i] > s[1][i]:  # 두 번째 행의 문자가 더 작은 경우
            min_str += s[1][i]
        else:  # 두 문자가 같은 경우, 두 가지 선택지 모두 가능
            min_str += s[0][i]  # 같으므로 어느 것을 선택해도 동일
            count *= 2  # 선택지가 두 배로 늘어남
    
    # 최종적으로 만들어진 최소 문자열과 그 개수 출력
    print(min_str)
    print(count)

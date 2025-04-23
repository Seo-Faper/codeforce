def decrypt(k, cipher):
    # 행(row) 개수 계산
    rows = len(cipher) // k

    # zigzag 형태로 문자열을 채울 2차원 리스트 초기화
    matrix = [[''] * k for _ in range(rows)]
    idx = 0

    # 암호문을 행 단위로 zigzag 방식으로 채우기
    for i in range(rows):
        if i % 2 == 0:
            # 짝수 행: 왼쪽→오른쪽
            for j in range(k):
                matrix[i][j] = cipher[idx]
                idx += 1
        else:
            # 홀수 행: 오른쪽→왼쪽
            for j in range(k - 1, -1, -1):
                matrix[i][j] = cipher[idx]
                idx += 1

    # 복원된 원문: 열 단위로 위→아래, 왼쪽→오른쪽
    result = []
    for j in range(k):
        for i in range(rows):
            result.append(matrix[i][j])

    return ''.join(result)


if __name__ == "__main__":
    k = int(input().strip())
    cipher = input().strip()
    print(decrypt(k, cipher))

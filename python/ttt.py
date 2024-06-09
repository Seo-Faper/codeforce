import base64

def decode_base64_50_times(encoded_str):
    for _ in range(50):
        encoded_str = base64.b64decode(encoded_str)
    return encoded_str

# 파일에서 문자열 읽기
with open('./python/theflag', 'r') as file:
    encoded_str = file.read().strip()  # 파일에서 문자열 읽기 및 공백 제거

# 50번 디코딩
decoded_str = decode_base64_50_times(encoded_str)

# 결과 출력 (필요에 따라 출력 형식 조정 가능)
print(decoded_str.decode('utf-8'))  # 바이너리를 utf-8 문자열로 디코딩

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

# 파일 읽기
def read_file(file_path):
    with open(file_path, 'rb') as f:
        return f.read()

# 파일 쓰기
def write_file(file_path, data):
    with open(file_path, 'wb') as f:
        f.write(data)

# AES 암호화 함수
def encrypt_file(input_file, output_file, key):
    data = read_file(input_file)
    
    # 패딩을 추가하여 데이터 길이를 16의 배수로 맞춤
    pad_len = 16 - len(data) % 16
    data += bytes([pad_len] * pad_len)
    
    # 16바이트 초기화 벡터 생성
    iv = get_random_bytes(16)
    
    # AES 암호화 객체 생성 (모드: CBC)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # 데이터 암호화
    encrypted_data = cipher.encrypt(data)
    
    # 초기화 벡터와 암호화된 데이터 저장
    write_file(output_file, iv + encrypted_data)
    print(f"암호화된 파일이 {output_file}에 저장되었습니다.")

# 메인 함수
def main(input_file, output_file):
    key = b'key_be_cool_fore'  # 16바이트 길이의 키

    encrypt_file(input_file, output_file, key)

if __name__ == "__main__":
    input_file = "p01.db"  # 입력 파일 경로
    output_file = "encrypted_file.bin"  # 암호화된 출력 파일 경로
    main(input_file, output_file)

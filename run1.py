from Crypto.Cipher import AES

# 파일 읽기
def read_file(file_path):
    with open(file_path, 'rb') as f:
        return f.read()

# 파일 쓰기
def write_file(file_path, data):
    with open(file_path, 'wb') as f:
        f.write(data)

# AES 복호화 함수
def decrypt_file(input_file, output_file, key):
    data = read_file(input_file)
    
    # 초기화 벡터와 암호화된 데이터 분리
    iv = data[:16]
    encrypted_data = data[16:]
    
    # AES 복호화 객체 생성 (모드: CBC)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # 데이터 복호화
    decrypted_data = cipher.decrypt(encrypted_data)
    
    # 패딩 제거
    pad_len = decrypted_data[-1]
    decrypted_data = decrypted_data[:-pad_len]
    
    # 복호화된 데이터 저장
    write_file(output_file, decrypted_data)
    print(f"복호화된 파일이 {output_file}에 저장되었습니다.")

# 메인 함수
def main(input_file, output_file):
    key = b'key_be_cool_fore'  # 16바이트 길이의 키

    decrypt_file(input_file, output_file, key)

if __name__ == "__main__":
    input_file = "encrypted_file.bin"  # 암호화된 입력 파일 경로
    output_file = "p1_decrypted_file.db"  # 복호화된 출력 파일 경로
    main(input_file, output_file)

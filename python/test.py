def transform_bytes(filename, new_filename):
    with open(filename, 'rb') as file:
        content = file.read()

    transformed_content = bytearray()

    # 파일을 8바이트 블록으로 처리
    for i in range(0, len(content), 8):
        block = content[i:i+8]
        if len(block) == 8:
            # 첫 4바이트의 엔디안 반전
            first_part = block[:4][::-1]
            # 두 번째 4바이트의 엔디안 반전 및 순서 변경
            second_part = block[4:][::-1]
            # 변환된 블록을 결과에 추가
            transformed_content += first_part + second_part
        else:
            # 마지막 블록이 8바이트 미만인 경우, 그대로 추가
            transformed_content += block

    # 변환된 내용을 새 파일에 저장
    with open(new_filename, 'wb') as new_file:
        new_file.write(transformed_content)
    print(f"Transformed file saved as {new_filename}")

# 예제 사용
filename = "./python/test"  # 원본 파일 경로
new_filename = "newtest.jpg"  # 변환될 파일의 새 경로
transform_bytes(filename, new_filename)

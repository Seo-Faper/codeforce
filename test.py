import pyewf

# e01 파일 경로
e01_file_path = 'path/to/your/file.e01'

# 검색할 파일 이름
target_file_name = 'example.txt'

def find_file_in_e01(e01_path, target_name):
    # E01 파일 열기
    ewf_handle = pyewf.handle()
    ewf_handle.open(e01_path)

    # 이미지 정보 가져오기
    image_info = ewf_handle.get_header_information()

    # 이미지 섹터 단위로 파일 검색
    for sector_number in range(image_info.get_number_of_sectors()):
        sector_data = ewf_handle.read_sector(sector_number)

        # 섹터 데이터에서 파일 이름 검색
        if target_name.encode('utf-8') in sector_data:
            print(f"File '{target_name}' found in sector {sector_number}")

    # E01 파일 닫기
    ewf_handle.close()

# 특정 파일 검색
find_file_in_e01(e01_file_path, target_file_name)

import ctypes, struct
from ctypes import wintypes

# 기본 상수 정의
GENERIC_READ      = 0x80000000
FILE_SHARE_READ   = 0x00000001
FILE_SHARE_WRITE  = 0x00000002
OPEN_EXISTING     = 3

FSCTL_GET_NTFS_VOLUME_DATA = 0x00090064
FSCTL_GET_NTFS_FILE_RECORD = 0x00090068

# NTFS 볼륨 정보 구조체 (_pack_=1을 지정하여 Windows API 레이아웃과 일치)
class NTFS_VOLUME_DATA_BUFFER(ctypes.Structure):
    _pack_ = 8  # 8바이트 정렬 사용 (없어도 기본 정렬은 8일 가능성이 높음)
    _fields_ = [
        ("VolumeSerialNumber", ctypes.c_ulonglong),
        ("NumberSectors", ctypes.c_ulonglong),
        ("TotalClusters", ctypes.c_ulonglong),
        ("FreeClusters", ctypes.c_ulonglong),
        ("BytesPerSector", ctypes.c_ulong),
        ("BytesPerCluster", ctypes.c_ulong),
        ("BytesPerFileRecordSegment", ctypes.c_ulong),
        ("ClustersPerFileRecordSegment", ctypes.c_ulong),
        ("MftValidDataLength", ctypes.c_ulonglong),
        ("MftStartLcn", ctypes.c_ulonglong),
        ("Mft2StartLcn", ctypes.c_ulonglong),
        ("MftZoneStart", ctypes.c_ulonglong),
        ("MftZoneEnd", ctypes.c_ulonglong)
    ]

# 입력 버퍼: NTFS_FILE_RECORD_INPUT_BUFFER (보통 문제 없지만, 필요시 _pack_ 지정 가능)
class NTFS_FILE_RECORD_INPUT_BUFFER(ctypes.Structure):
    _fields_ = [
        ("FileReferenceNumber", ctypes.c_ulonglong)
    ]

def read_volume_data(handle):
    buf_size = 4096  # 충분한 크기의 버퍼 할당
    buf = ctypes.create_string_buffer(buf_size)
    bytes_returned = wintypes.DWORD(0)
    res = ctypes.windll.kernel32.DeviceIoControl(
        handle,
        FSCTL_GET_NTFS_VOLUME_DATA,
        None,
        0,
        buf,
        buf_size,
        ctypes.byref(bytes_returned),
        None
    )
    print("DeviceIoControl res:", res)
    if res == 0:
        raise ctypes.WinError()
    vol_data = NTFS_VOLUME_DATA_BUFFER.from_buffer_copy(buf)
    return vol_data

def get_mft_record(handle, file_ref, record_size):
    output_size = record_size + 4096 
    class NTFS_FILE_RECORD_OUTPUT_BUFFER(ctypes.Structure):
        _fields_ = [
            ("FileRecordLength", wintypes.DWORD),
            ("FileRecordBuffer", ctypes.c_byte * output_size)
        ]
    input_buffer = NTFS_FILE_RECORD_INPUT_BUFFER(FileReferenceNumber=file_ref)
    output_buffer = NTFS_FILE_RECORD_OUTPUT_BUFFER()
    bytes_returned = wintypes.DWORD(0)
    res = ctypes.windll.kernel32.DeviceIoControl(
        handle,
        FSCTL_GET_NTFS_FILE_RECORD,
        ctypes.byref(input_buffer),
        ctypes.sizeof(input_buffer),
        ctypes.byref(output_buffer),
        ctypes.sizeof(output_buffer),
        ctypes.byref(bytes_returned),
        None
    )
    if res == 0:
        raise ctypes.WinError()
    return bytes(output_buffer.FileRecordBuffer)[:output_buffer.FileRecordLength]

def parse_data_runs(data_runs):
    runs = []
    offset = 0
    current_lcn = 0
    while offset < len(data_runs):
        header = data_runs[offset]
        offset += 1
        if header == 0:
            break
        length_size = header & 0x0F
        offset_size = (header >> 4) & 0x0F
        run_length = int.from_bytes(data_runs[offset:offset+length_size], byteorder="little")
        offset += length_size
        run_offset_bytes = data_runs[offset:offset+offset_size]
        offset += offset_size
        run_offset = int.from_bytes(run_offset_bytes, byteorder="little", signed=True)
        current_lcn += run_offset
        runs.append((current_lcn, run_length))
    return runs

def read_mft():
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.CreateFileW(r"\\.\C:", GENERIC_READ, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0, None)
    if handle == wintypes.HANDLE(-1).value:
        raise ctypes.WinError()
    print("[DEBUG] 볼륨 핸들 열림:", handle)
    
    vol_data = read_volume_data(handle)
    print("[DEBUG] BytesPerFileRecordSegment:", vol_data.BytesPerFileRecordSegment,
          "BytesPerCluster:", vol_data.BytesPerCluster,
          "MftStartLcn:", vol_data.MftStartLcn)
    record_size = vol_data.BytesPerFileRecordSegment
    mft_record_bytes = get_mft_record(handle, 0, record_size)
    print("[DEBUG] $MFT 파일 레코드 길이:", len(mft_record_bytes))
    
    data_run_offset = None
    pos = 0
    while pos < len(mft_record_bytes) - 4:
        attr_type = struct.unpack_from("<I", mft_record_bytes, pos)[0]
        if attr_type == 0x80:
            non_res_flag = mft_record_bytes[pos+8]
            if non_res_flag != 0:
                data_runs_relative_offset = mft_record_bytes[pos+0x40]
                data_run_offset = pos + data_runs_relative_offset
                break
        attr_length = struct.unpack_from("<I", mft_record_bytes, pos+4)[0]
        if attr_length == 0:
            break
        pos += attr_length

    if data_run_offset is None:
        print("[DEBUG] $MFT 레코드에서 데이터런을 찾지 못함")
        kernel32.CloseHandle(handle)
        return []

    print("[DEBUG] 데이터런 오프셋:", data_run_offset)
    end_offset = data_run_offset
    while end_offset < len(mft_record_bytes) and mft_record_bytes[end_offset] != 0:
        end_offset += 1
    data_runs = mft_record_bytes[data_run_offset:end_offset]
    print("[DEBUG] 데이터런 바이트:", data_runs)
    
    runs = parse_data_runs(bytearray(data_runs))
    print("[DEBUG] 파싱된 데이터런:", runs)

    mft_data = bytearray()
    for lcn, length in runs:
        offset = lcn * vol_data.BytesPerCluster
        size = length * vol_data.BytesPerCluster
        print(f"[DEBUG] 데이터런 읽기: LCN={lcn}, 클러스터수={length}, offset={offset}, size={size}")
        if ctypes.windll.kernel32.SetFilePointerEx(handle, ctypes.c_longlong(offset), None, 0) == -1:
            raise ctypes.WinError()
        buf = ctypes.create_string_buffer(size)
        bytes_read = wintypes.DWORD(0)
        res = ctypes.windll.kernel32.ReadFile(handle, buf, size, ctypes.byref(bytes_read), None)
        if res == 0:
            raise ctypes.WinError()
        mft_data.extend(buf.raw[:bytes_read.value])
    
    kernel32.CloseHandle(handle)
    print("[DEBUG] 전체 읽은 MFT 데이터 크기:", len(mft_data))
    
    mft_records = []
    for i in range(0, len(mft_data), record_size):
        rec = mft_data[i:i+record_size]
        if len(rec) < record_size:
            break
        if rec[0:4] != b'FILE':
            continue
        mft_records.append(rec)
    print("[DEBUG] 파싱된 MFT 레코드 수:", len(mft_records))
    return mft_records

if __name__ == "__main__":
    try:
        print("[DEBUG] MFT 읽기 시작")
        records = read_mft()
        print("[DEBUG] MFT 읽기 완료")
        for rec in records:
            print(rec[:100].hex())
    except Exception as e:
        print("오류 발생:", e)

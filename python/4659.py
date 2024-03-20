import re
def is_valid(s):
    # 모음 하나를 반드시 포함
    if not re.search('[aeiou]', s):
        return False
    # 모음이 3개 혹은 자음이 3개 연속으로 오는 것을 체크
    if re.search('[aeiou]{3,}', s) or re.search('[bcdfghjklmnpqrstvwxyz]{3,}', s):
        return False
    # 같은 글자가 연속적으로 두 번 오는 것을 체크 (ee, oo 제외)
    if re.search(r'(?!ee|oo)(.)\1', s):
        return False
    return True

while True:
    s = input()
    if s =='end':break
    if is_valid(s):
        print("<"+s+">"+" is acceptable.")
    else:
        print("<"+s+">"+" is not acceptable.")
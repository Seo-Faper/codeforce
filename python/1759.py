from itertools import combinations

l,c = map(int,input().split()) # l : 암호길이(1모음, 2 자음)  c: 사용한 알파벳 갯수(이중 ㅣ개를 조합)
word = sorted(list(map(str,input().split())))  #오름차순으로 정렬

m = ['a','e','i','o','u']


def cnt(password):  #튜플을 인자로 받음, 모음 자음 갯수를 원소로 하는 리스트 반환
    result = []
    mm = 0  # 모음 갯수
    zz = 0  # 자음 갯수
    for i in range(l):
        if password[i] in m:
            mm += 1
        else:
            zz += 1
    result.append(mm)
    result.append(zz)
    return result

example = list(combinations(word,l))  # 모든 경우

final = [] # 모든 경우를 cnt함수에 넣은 결과가 들어간 리스트
for i in range(len(example)):
    final.append(cnt(example[i]))

finals = []  # 모음이 1개이상, 자음이 2개 이상인 조건을 만족하는 경우를 저장하는 리스트
for i in range(len(final)):
    if final[i][0] >= 1 and final[i][1] >= 2:
        finals.append(list(example[i]))  # 튜플을 리스트로 변경
for i in range(len(finals)):
    print("".join(finals[i]))
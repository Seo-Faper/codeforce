O = {'-':0,'\\':1,'(':2,'@':3,'?':4,'>':5,'&':6,'%':7,'/':-1}


while True:
    case = input()
    if case == '#': break

    ans = 0
    for i in range(len(case)):

        ans+=8**(len(case)-1-i)*O[case[i]]
    print(ans)
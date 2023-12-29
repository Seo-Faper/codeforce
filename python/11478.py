
S = input()


S1 = set()

for i in range(0,len(S)):
    for j in range(0,len(S)):
        if i+j < len(S):
            S1.add(S[j:i+j+1])
print(len(S1))
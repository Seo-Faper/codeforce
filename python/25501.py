def recursion(s, l, r):
    global index
    index +=1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):

    return recursion(s, 0, len(s)-1)

# print('ABBA:', isPalindrome('ABBA'))
# print('ABC:', isPalindrome('ABC'))

for i in range(int(input())):
    
    index = 0 
    print(isPalindrome(input()),index)
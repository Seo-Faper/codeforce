n = int(input())
f = int(input())
temp = (n//100)*100
while(True):  
    if(temp%f == 0) :
        result = temp % 100; 
        if(result < 10): 
            print("0" + str(result))
        else: print(result)
        break
    temp+=1
 
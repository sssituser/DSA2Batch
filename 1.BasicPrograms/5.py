num = int(input('Enter a number : ')) # 678
res ="""""" 
while num>0:
    digit = num%10 
    print(digit,end=" ") 
    res +=str(digit)+","
    num=num//10
res = res[:-1]+"."
print(res)
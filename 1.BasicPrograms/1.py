def getnums(start,end):
    res=''
    for i in range(start,end+1):
        res=res+str(i)+","
    return res[0:-1]+"."

def sumofnnums(n):
    sum=0
    for i in range(1,n+1):
        sum +=i
    return sum
print(sumofnnums(5))
print(sumofnnums(10))

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *=i
    return fact
num = 5
print(f'{num} factorial is : {factorial(num)}')
num = 6
print(f'{num} factorial is : {factorial(num)}')
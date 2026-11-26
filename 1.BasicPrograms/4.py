num = int(input('Enter a number  : '))
#num = 5678
num  = str(num)
res =''
for i in range(len(num)):
    res += str(num[i])+","
res = res[:-1]+"."
print(res)

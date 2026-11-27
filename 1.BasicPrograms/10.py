'''
 getfactors

'''

def getfactors(num:int):
    li=list()
    for i in range(1,num+1):
        if num%i==0:
            li.append(i)
    return li



def getfactorscount(num:int):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    return count
num = 8
print(f'{num} facctors : {getfactors(num)} and count is : {getfactorscount(num)}')
num = 12
print(f'{num} facctors : {getfactors(num)} and count is : {getfactorscount(num)}')

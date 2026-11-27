'''
create a console application which generates list of 
armstrong numbrers for the  given range.
Example :
start = 1     end = 500
Armstrong List : 1,2,3,4,5,6,7,8,9,....153,370,371,407.
=========================steps==========
input start=1  end= 500
ArmstrongList
Armstrong
1 = 1pow1 => 1
153 = > 1cube+5cube+3cube = 153
1634 => 1pow4 + 6pow4+3pow4+4pow4 => 1634
9474 > 9p4+4p4+7p4+4p4 => 9474
123 = 1+8+27=>36

1.No of Digits count - pow
2.Separate the digit 
3.find the power of the digits 
4.sum of the powers
5.compare num number sum if equal armstrong



'''
def digitcount(num:int):
    count = 0;
    while num>0:
        digit = num%10
        count+=1
        num//=10
    return count

def isarmstrong(num:int): # num = 153
    power = digitcount(num)
    copy = num
    sum = 0
    while copy>0: 
        digit = copy%10 
        sum+= digit**power 
        copy//=10
    return num==sum

def getarmstrongs(start:int,end:int):#1,500
    res = ''
    for i in range(start,end+1):
        if isarmstrong(i):
            res += str(i)+","
    return res[:-1]+"."

print(getarmstrongs(1,100000))
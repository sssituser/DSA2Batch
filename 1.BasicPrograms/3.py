# lis = [321,456,789,315,725]
#        [ 3 ,  6 ,  9 ,  5 ,  7]
#        [9,7,6,5,3]
#         97653
# steps : list of numbers need find max digit from each number in list and store\
# another list, sort list maxdigits list in desc, convert maxdigit list into  number

def getmaxdigit(num): 
    max = num%10  
    while num>0: 
          digit = num%10 
          if digit>max:
               max=digit
          num = num//10 
    return max
     
def getmaxdigitlist(li): #[345,678]
     maxdigitlilst =[]
     for num in li:
          maxdigitlilst.append(getmaxdigit(num))   
     return maxdigitlilst

def sortlistdesc(li):
     li.sort(reverse=True)
     return li

def listtonum(li):#  [5,4,3,7]
     res = 0
     for num in li:
          res = res*10+num
     return res

def getmaxnum(li):
     return  listtonum(sortlistdesc(getmaxdigitlist(li)))

lis = [321,456,789,315,725] # 97653

print(getmaxnum(lis))

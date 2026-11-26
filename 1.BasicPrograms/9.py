# create a console application to generate list of palindromes for the given range
# 100   1000  101,121,131,.....999.
from simple import *
def palinlist(start,end):
    res = ''
    for i in range(start,end+1):
        if ispalindrome(i):
            res += str(i)+","
    return res[:-1]+"."
print(palinlist(1000,10000000))


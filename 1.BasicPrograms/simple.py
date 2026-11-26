#Create a console application to check given number is palindrome or not
# take num
# reverse the number
# compare the number
from sample import reverse
def ispalindrome(num:int): # 123
    return reverse(num)==num

num = 123
print(f'{num} is Palindrome : {ispalindrome(num)}')

num = 121
print(f'{num} is Palindrome : {ispalindrome(num)}')
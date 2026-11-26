def reverse(num:int):
    rev = 0
    while num>0:
        digit = num%10
        rev = rev*10+digit
        num//=10
    return rev
num = 123
print(f'Reverse of {num} is {reverse(num)}')

num = 456
print(f'Reverse of {num} is {reverse(num)}')
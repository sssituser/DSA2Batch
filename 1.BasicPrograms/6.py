num = int(input('Enter a number : ')) # num = 576
# max = num%10 
# while num>0: 
#     digit = num%10 
#     if digit>max: 
#         max = digit
#     num//=10 
# print(f'{max} is max')


sum = 0
while num>0:
    digit = num%10
    sum += digit
    num//=10
print(f'Digit  sum is : {sum}')


prod = 1
while num>0:
    digit = num%10
    prod *= digit
    num//=10
print(f'Digit  Product is : {sum}')
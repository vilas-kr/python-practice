# Write a program to reverse a number

n = int(input('Enter a number : '))
rev = 0
while(n != 0):
    rem = n % 10
    rev = rev * 10 + rem
    n //= 10
print(f'Reversed given interger is : {rev}')
    
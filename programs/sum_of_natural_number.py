# Write a program to find the sum of numbers from 1 to n
n = int(input('Enter a number : '))
sum = 0
for i in range(1, n):
    sum += i
print(f'The sum of {n} natural number is : {sum}')
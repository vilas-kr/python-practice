# Write a program to reverse a string without using splicing

s = input('Enter a string : ')
rev_str = ''
for i in range(len(s)):
    rev_str += s[len(s)-1-i]

print(f'Reverse string is : {rev_str}')

'''
Given an integer, Check whether it is a palindrome. A palindrome number
is a number that remains the same when its digits are reversed.

Sample Case 1
input:
123

output:
Not Palindrome

Sample case 2
input:
12321

output:
Palindrome
'''
import sys

# Read input from standard input
data = sys.stdin.read().strip()

def solve(input_data):
    num = input_data.split("\n")[0]

    # check condition
    if num == num[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
        
# call the function
solve(data)
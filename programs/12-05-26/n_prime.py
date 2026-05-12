'''
First N primes

description given two positive integers N and M,
print the first N prime numbers greater than M

input format:

Sample Case 1
input:
5 10

output:
11 13 17 19 23

Sample Case 2
input:
3 20

output:
23 29 31
'''


import sys

# Read input from standard input
input_data = sys.stdin.read().strip()

def check_prime(n: int) -> bool:
    if n < 1:
        return False
    
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
        
    return True

def solve(input_data):
    # split input into lines
    lines = input_data.split("\n")
    
    n, m = tuple(map(int, lines[0].split(" ")))
    count = 0
    
    while count < n:
        if check_prime(m):
            print(m, end=" ")
            count += 1
        m += 1
        
# call the function
solve(input_data)
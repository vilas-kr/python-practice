'''
Rotate array

input:  
7 3
1 2 3 4 5 6 7

output:
5 6 7 1 2 3 4

'''
import sys

input_data = sys.stdin.read().strip()
def solve (input_data):
    lines = input_data.split("\n") # Split input into lines
    
    #User writes their logic here
    k = int (lines [0].split() [1])
    arr = list(map(int, lines [1].split()))
    result = rotate (arr, k)
    
    for num in result:
        print (num, end="")
        
def rotate(arr: list [int], k: int) -> list[int]:
    k = k % len (arr)
    return arr[-k:] + arr[:-k]

# Call the function
solve (input_data)
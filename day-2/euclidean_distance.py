import sys
import math

'''Command line arguments'''
x = int(sys.argv[1])
y = int(sys.argv[2])

def euclidean_distance(x, y):
    '''Parameter
    x , y : int 
        points
    output : float
        Calculate Euclidean distance from origin'''
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

print(f"Euclidean Distance ({x}, {y}) from origin is {euclidean_distance(x, y)}")
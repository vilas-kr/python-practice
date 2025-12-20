import sys
import math

a = int(input("Enter value of A : "))
b = int(input("Enter value of B : "))
c = int(input("Enter value of C : "))

def cal_quadratic(a, b, c):
    '''
    Parameter
    a, b, c : int
        value of equation
    output : float
        root 1, root 2
    '''
    delta = math.pow(b, 2) - (4 * a * c)
    if delta > 0 : 
        root1 = (-b + math.sqrt(delta)) / ( 2 * a)
        root2 = (-b - math.sqrt(delta)) / ( 2 * a)
        return root1, root2
    elif delta == 0 :
        root = -b / (2 * a)
        return root, root
    else :
        return "No real roots", "No real roots"
    
root1, root2 = cal_quadratic(a, b, c)
print(f"Root 1 of X = {root1} \nRoot 2 of X = {root2}")
def overflow_detector(inflow):
    '''
    Parameter
    ---------
    inflow : list of int
        inflow per minute in liter
    
    Returns
    -------
    overflow : int
        overflow minute
    '''
    capacity = 1000
    for i, j in enumerate(inflow):
        capacity -= j
        if capacity < 0 :
            return i+1
    return -1
        
n = int(input("Enter minutes : "))
print("Enter the flow : ")
inflow = [int(i) for i in input().split()]
print(overflow_detector(inflow))
        
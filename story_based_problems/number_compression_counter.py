def compression_counter(num):
    '''
    Parameter
    ---------
    num : int
        Any number
    
    Returns 
    -------
    count : int
        count how many times it can be divisible by 2 until it becomes odd
    '''
    count = 0
    #avoid infite loop
    if num == 0 :
        return count
    
    while True :        
        if num % 2 != 0 :
            return count
        count += 1
        num //= 2
    
print(compression_counter(int(input("Enter a number : "))))
            
        
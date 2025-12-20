def binary_to_decimal(num):
    '''
    Parameter 
    ---------
    num : int
        Positive integer
    
    Return
    ------
    binary : string
        binary Representation of given num
    '''
    binary = ''
    while num > 0 :
        rem = num % 2
        binary += str(rem)
        num = num // 2
    return binary[::-1]

print(binary_to_decimal(int(input("Enter a number to convert it to binary : "))))

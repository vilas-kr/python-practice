def binary_to_decimal(num):
    '''
    Parameter 
    ---------
    num : string
        binary representation in string
    
    Return
    ------
    decimal : int
        convert num to decimal
    '''
    decimal = 0
    power = 0

    for digit in reversed(num):
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal

print(binary_to_decimal(input("Enter binary : ")))

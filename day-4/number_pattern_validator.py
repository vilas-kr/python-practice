def number_pattern_validator(num):
    '''
    Parameter
    ---------
    num : int
        An integer num
        
    Returns
    -------
    status : boolean
        - True -> digits of num are strictly increasing left to right
        - False -> otherwise
    '''
    # convert num into digits
    digits = num_to_digits(num)
    for i in range(len(digits)-1) :
        if digits[i+1] <= digits[i] : 
            return False
    
    return True
    
def num_to_digits(num):
    '''
    Parameter
    ---------
    num : int
        An integer num
    
    Returns
    -------
    digits : list of int
        convert num into digits
    '''
    digits = []
    while num != 0 : 
        rem = num % 10
        digits.append(rem)
        num //= 10
    return digits[::-1]

print(number_pattern_validator(int(input("Enter Number : "))))
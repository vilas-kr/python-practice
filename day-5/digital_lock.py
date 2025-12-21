from palindrom import num_to_digits
def sum_of_digits(num):
    '''
    Parameter
    ---------
    num : int
        An integer
        
    Returns
    -------
    total_sum : int
        total sum of digits in num
    '''
    
    #convert num to digits
    digits = num_to_digits(num)
    total_sum = 0
    for i in digits:
        total_sum += i
    return total_sum

def digital_lock(num):
    '''
    Parameter
    ---------
    num : int
        An integer
    
    Returns
    -------
    final_digit : int
        single digit obtained after 
        repeatedly subtracting sum of digits
    '''
    while abs(num) > 9:
        num -= sum_of_digits(num)
        
    return num

print(digital_lock(int(input("Enter a number : "))))
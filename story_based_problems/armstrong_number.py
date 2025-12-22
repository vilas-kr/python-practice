from number_pattern_validator import num_to_digits

def armstrong_number_checker(num):
    '''
    Parameter
    ---------
    num : int
        An integer
    
    Returns
    -------
    status : boolean
        - True -> num is armstrong number
        - False -> num is not armstrong number
    '''
    #convert num to digits
    digits = num_to_digits(num)
    total_sum = 0
    
    #Calculate sum of cubes of digit
    for i in digits:
        total_sum += i ** 3
        
    if total_sum == num :
        return True
    else :
        return False

n = int(input("Enter a number : "))
if armstrong_number_checker(n) :
    print("YES")
else :
    print("NO")

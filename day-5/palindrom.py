def check_palindrome(num):
    '''
    Parameter
    ---------
    num : int
        An integer
    
    Returns
    -------
    status : boolean
        - True -> num is palindrome
        - False -> num is not palindrome
    '''
    #convert num into digits
    digits = num_to_digits(num)
    i = 0
    j = len(digits) - 1
    while i < j : 
        if digits[i] != digits[j] : 
            return False
        i += 1
        j -= 1
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

n = int(input("Enter a number : "))
if check_palindrome(n) : 
    print("PALINDROME")
else : 
    print("NOT PALINDROME")
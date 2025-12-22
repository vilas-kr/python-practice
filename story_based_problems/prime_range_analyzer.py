def count_prime(a, b):
    '''
    Parameter
    ---------
    a : int
        Starting range of the number
    b : int 
        Ending range of a number (inclusive b)
    
    Return 
    ------
    prime_count : int
        Total number of prime numbers from A to B
    '''
    prime_count = 0
    for i in range(a, b+1) :
        if is_prime(i) : 
            prime_count += 1
    return prime_count

def is_prime(num):
    '''
    Parameter
    ---------
    num : int
        Any number
        
    Return
    ------
    flag : boolean
        - Ture -> Number is prime
        - False -> Number is not prime
    '''
    #Negative numbers and 1 is neither prime nor composite
    if num <= 1 :
        return False
    i = 2
    while i*i <= num :
        if num % i == 0 :
            return False
        i += 1
    return True

print(count_prime(int(input("Enter starting range : ")), int(input("Enter ending range : "))))

        
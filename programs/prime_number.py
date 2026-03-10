# Program to check if a number is prime

def check_prime(n: int):
    '''
    Check prime number or not
    Args:
        n: any integer
    Returns:
        - True : given number is prime 
        - False: given number is not prime
    '''
    if n <= 1:
        return False
    
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

if __name__ == '__main__':
    num = int(input('Enter a number : '))
    if check_prime(num):
        print(f'{num} is prime number')
    else:
        print(f'{num} is not a prime number')
    
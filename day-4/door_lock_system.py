def verify_lock(lock_pin, current_pin):
    '''
    Parameter
    ---------
    lock_pin : int
        lock pin
    current_pin : int
        user entered pin
        
    Returns
    -------
    status : boolean
        - True -> lock pin matches current pin
        - False -> otherwise
    '''
    if lock_pin == current_pin :
        return True
    else :
        return False
    
def lock_attempt(lock_pin):
    '''
    Parameter
    ---------
    lock_pin : int
        actual pin of door lock
    
    Prints
    ------
    - ACCESS GRANTED -> pin is correct
    - LOCKED -> after 3 unsuccessful attempt
    '''
    attempt = [int(input()) for i in range(3)]
    for i in attempt :
        if verify_lock(lock_pin, i) :
            print('ACCESS GRANTED')
            return 
    print('LOCKED')
    
lock_attempt(int(input("Enter lock pin : ")))
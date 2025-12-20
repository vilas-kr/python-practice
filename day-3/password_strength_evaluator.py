def password_strength_evaluator(password):
    '''
    Parameter
    ---------
    password : string
        Password in string
    output
    ------
    stauts : string
        - Strong -> password contains more than 8 characters 
                    and at least one digit and uppercase
        - Weak -> other than
    '''
    if len(password) >= 8 and has_digit(password) and has_uppercase(password) :
        return "Strong"
    else : 
        return "Weak"

def has_digit(password) :
    '''
    Parameter
    ---------
    password : string
    
    Returns
    -------
    status : boolean
        - True -> password octains digit
        - False -> password does not contain digit
    '''
    for i in password : 
        if '0' <= i <= '9' :
            return True
    return False

def has_uppercase(password) :
    '''
    Parameter
    ---------
    password : string
    
    Returns
    -------
    status : boolean
        - True -> password octains uppercase
        - False -> password does not contain uppercase
    '''
    for i in password : 
        if 'A' <= i <= 'Z' :
            return True
    return False

print(password_strength_evaluator("Vilas1234"))
        
    
    
    
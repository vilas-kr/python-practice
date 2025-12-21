def ticket_calculator(distance, age) :
    '''
    Parameter
    ---------
    distance : int
        total travel distance in kilometers
    age : int 
        age of passanger
        
    Returns
    -------
    fare : float
        total fare after discount
    '''
    # 2 rupees per kilometer
    fare = distance * 2
    if age < 12 :
        fare -= fare * 0.5
    elif age >= 65 : 
        fare -= fare * 0.3
    
    return fare

fare = ticket_calculator(int(input("Enter travel distance : ")), int(input("Enter Age of passanger : ")))
print(fare) 
    
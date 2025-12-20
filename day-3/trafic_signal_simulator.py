def trafic_signal(time):
    '''
    Parameter
    ---------
    time : int
        second between 1 to 90
    
    Returns
    -------
    status : string
        - RED -> time between 1 to 30
        - YELLOW -> time between 31 to 45
        - GREEN -> time between 46 to 90
    '''
    time = time % 90
    if time == 0:
        time = 90
    
    if 1 <= time <= 30 :
        return "RED"
    elif 31 <= time <= 45 :
        return "YELLOW"
    else :
        return "GREEN"
    
print(trafic_signal())
        
    
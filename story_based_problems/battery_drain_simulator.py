def battery_drain_cal(drain_per_minute):
    '''
    Parameter
    ---------
    drain_per_minute : int
        Specify how much battery drain per minute in percentage
    
    Returns
    -------
    minutes : int
        how long 100% battery lost in minutes
    '''
    battery = 100
    minutes = 0
    while battery > 0 :    
        minutes += 1
        battery -= drain_per_minute
    return minutes

print(battery_drain_cal(int(input("Enter how much battery drain per minute in percentage : "))))
    
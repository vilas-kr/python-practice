def cal_bill(unit):
    '''
    Parameter
    ---------
    unit : int
        total electricity usage in units
        
    Output
    -------
    bill : float
        total Bill amount according to policy
    '''
    cur_unit = unit
    bill = 0
    
    #Negative units
    if cur_unit <= 0:
        return 0.0
    
    #first 100 units
    if cur_unit <= 100:
        bill = cur_unit * 3.0
        cur_unit -= cur_unit
    else : 
        bill = 100 * 3.0
        cur_unit -= 100
        
    #second 100 units
    if cur_unit <= 100:
        bill += cur_unit * 5.0
        cur_unit -= cur_unit
    else : 
        bill += 100 * 5.0
        cur_unit -= 100
    
    #remaining units
    if cur_unit > 0 :
        bill += cur_unit * 8.0
    
    #Add 10% surge charge for more than 300 units
    if unit > 300 : 
        bill += bill * 0.1
    
    return bill
    
print(cal_bill(250))
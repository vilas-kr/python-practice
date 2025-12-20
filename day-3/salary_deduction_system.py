def salary_deduction(salary, late_days, absent_days) :
    '''
    Parameter
    ---------
    salary : float
        total salary of the employee
    late_days : int
        total late days in a month
    absent_days : int
        total absent days in a month
        
    Return
    ------
    salary : float
        Calculated salary base on conditions
    '''
    if late_days > 10 : 
        salary -= salary * 0.1
    elif late_days > 5:
        salary -= salary * 0.05
    
    if absent_days > 2 : 
        salary -= salary * 0.05
        
    return salary

print(salary_deduction(40000, 3,  1))
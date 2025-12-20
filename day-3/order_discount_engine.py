def order_discount(amount):
    '''
    Parameter
    ---------
    amount : float
        Total order amount
    
    Returns
    -------
    amount : float
        final amount after discount
    '''
 
    if amount >= 5000 : 
        amount -= amount * 0.2
    elif amount >= 3000 : 
        amount -= amount * 0.1
    elif amount >= 1000 :
        amount -= amount * 0.05
    else :
        pass
    
    return amount

print(order_discount(int(input("Enter order amount : "))))
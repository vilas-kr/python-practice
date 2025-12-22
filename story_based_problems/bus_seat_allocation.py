def check_seat(req):
    '''
    Parameter
    ---------
    req : list of int
        list of request seat
    
    Returns
    -------
    status : list of boolean
        - True -> seat available
        - False -> seat not available
    '''
    seats = 40
    status = []
    for i in req :
        if seats-i >= 0:
            status.append(True)
            seats -= i
        else :
            status.append(False)
    return status

n = int(input("Enter total number of request : "))
request = [int(input()) for i in range(n)]
request = check_seat(request)
for i in request :
    if i :
        print("CONFIRMED")
    else :
        print("WAITLISTED")
        
    
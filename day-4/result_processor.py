def result_processor(marks):
    '''
    Parameter
    ---------
    marks : list of int
        marks of subjects between 0 to 100
    
    Returns
    -------
    status : string
        - FAIL -> any marks is less then 35
        - DISTINCTION -> if average marks is >= 75
        - PASS -> average marks is < 75
    '''
    #check if any subject marks is lessthen 35
    total_marks = 0
    for i in marks :
        if i < 35 :
            return 'FAIL'
        else : 
            total_marks += i
        
    #check if average marks is greater then
    if total_marks/len(marks) >= 75 : 
        return 'DISTINCTION'
    else :
        return 'PASS'
    
print("Enter marks : ")
marks = [int(i) for i in input().split()]
print(result_processor(marks))
    
    
     
        
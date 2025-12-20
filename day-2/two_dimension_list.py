def datatype():
    choice = int(input(f"Enter which datatype your want to store in array\nEnter 1 for integer\nEnter 2 for float\n"
                    "Enter 3 for boolean\nEnter your choice : "))
    match choice:
        case 1 : user_input(int)
        case 2 : user_input(float)
        case 3 : user_input(bool)
        case _ : print("Invalid input")
        
def user_input(inputType):
    rows = int(input("Enter number of rows : "))
    cols = int(input("Enter number of columns : "))
    print("Enter values : ")
    array = []
    if inputType is bool :
        for i in range(rows):
            col = []
            for j in range(cols):
                val = input()
                if val == 'true' or val == 'True' or val == 'T' or val == 't' or val == '1' or val == 'TRUE' :
                    col.append(True)
                else : 
                    col.append(False)
            array.append(cols)
    else: 
        for i in range(rows):
            col = []
            for j in range(cols):
                col.append(inputType(input()))
            array.append(col)
    print(array) 
    
datatype()     


    
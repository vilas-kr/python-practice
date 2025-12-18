num = int(input("Enter number : "))
if(num == 1):
    print("No prime factor")
elif(num <= 0):
    print("Invalid input")
else:
    i = 2
    while(i*i <= num):
        if(num%i == 0):
            print(i, end=", ")
            num = num//i
        else:
            i += 1
    if(num != 0):
        print(num)    
    
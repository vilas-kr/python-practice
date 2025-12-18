num = int(input("Enter N : "))
if(num <= 0):
    print("Hormonic number defined only for positive numbers")
else:
    sum = 0
    for i in range(1, num+1):
        sum = sum + 1/i
    print(f"{sum :.4f}")
    
    
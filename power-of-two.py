num = int(input("Enter number : "))
if(num <= 0 or num > 31):
    print("Entered Number is out of range")
else:
    for i in range(num+1):
        print(f"2 ^ {i:<2d} = {2 ** i}")
year = int(input("Enter year : "))
while(len(str(year)) != 4):
    year = int(input("Please enter valid year : "))
if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

    
    
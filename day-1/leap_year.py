year = input("Enter the year : ")
while(len(year) != 4):
    year = input("Please enter valid year : ")
year = int(year)
if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

    
    
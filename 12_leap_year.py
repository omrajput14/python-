# Check leap year
year = 2000
if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year")
elif (year % 4 ==0) and (year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

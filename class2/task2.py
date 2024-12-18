years = int(input("Enter number of years: "))
unit = input("""Select your choice: 
1 - Days
2 - Weeks
3 - Hours
""")


if unit == "1":
    print(years*365)
elif unit == "2":
    print(Weeks*52)
elif unit == "3":
    print(365*24*years)
else:
    print("Value is incorrect")
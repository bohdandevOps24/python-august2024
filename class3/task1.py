#limit = int(input("enter the your age: "))
age = int
age1 = 13
age2 = 18


while True:
    limit = int(input("enter the your age: "))
    if limit > 0 and limit <  age1:
        print("Sorry you are not allow to pass")
    elif limit >= age1 and limit <= age2:
        print("Please call your legal guerdian")
    elif limit > age2:
        print("You are welcome")
    else:
    print("Denied")



    
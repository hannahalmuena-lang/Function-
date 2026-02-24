def myhan():
    print("SELECT OPERATION:")
    print("\n[1]Add")
    print("\n[2]Subtract")
    print("\n[3]Multiply")
    print("\n[4]Divide\n")

    user = int(input("Enter Choices: ")) 
    if user == 1:
        a = int(input("enter 1st number: "))
        b = int(input("enter 2nd number: "))
        result = a+b
        print("Result is: ",result)

    elif user == 2:
        a = int(input("enter 1st number: "))
        b = int(input("enter 2nd number; "))
        result = a-b
        print("Result is: ",result)

    elif user == 3:
        a = int(input("enter 1st number: "))
        b = int(input("enter 2nd number: "))
        result = a*b
        print("Result is: ",result)

    elif user == 4:
        a = int(input("enter 1st number: "))
        b = int(input("enter 2nd number: "))
        result = a/b
        print("Result is: ",result)
    else:
        print("wrong password")
    myhan()
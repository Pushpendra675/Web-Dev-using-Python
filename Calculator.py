def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if(b==0):
        print("Cannot Divide By zero!!")
    else:
        return a/b
    
while True:

    print("\n===== Calculator =====")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Quit")
    
    choice = int(input("Enter the operation Choice(1-4):"))
    


    num1 = int(input("\nEnter first number:"))
    num2 = int(input("Enter second number:"))
    
    if choice==1:
        print("Result =",sum(num1,num2))
    elif choice==2:
        print("Result =",sub(num1,num2))
    elif choice==3:
        print("Result =",mul(num1,num2))
    elif choice==4:
        print("Result =",div(num1,num2))
    elif choice==5:
        print("Quit the Calc Successfully.")
    else:
        print("Invalid choice!")

print("\n")
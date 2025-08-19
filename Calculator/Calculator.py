# Calculator Project

#---------------------

# Functions perform addition, subtraction, multiplication, and division + Return solutions that will be captured by variable
def addition(n1,n2):
    return n1+n2
def subtraction(n1,n2):
    return n1-n2
def multiplication(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2

def calculator():
    entry1=int(input("Enter the first number: "))
    entry2=int(input("Enter the second number: "))
    operation=input("Enter the operation(+,-,*,/): ")
    print("\n")

    if operation=="+":
        result=addition(entry1,entry2)
        print(f"The final result: {result}")
    elif operation=="-":
        result=subtraction(entry1,entry2)
        print(f"The final result: {result}")
    elif operation=="*":
        result=multiplication(entry1,entry2)
        print(f"The final result: {result}")
    elif operation=="/":
        result=division(entry1,entry2)
        print(f"The final result: {result}")
    else:
        print("Wrong operation!")
    print("\n")

calculator() # Works the calculator for the first time

use_again=input("Do you want to go again?(yes/no): ").lower()
while use_again=="yes":
    calculator()
    use_again = input("Do you want to go again?(yes/no): ").lower()
    if use_again=="no":
        print("\n")
        print("Thanks for trying out this calculator!")
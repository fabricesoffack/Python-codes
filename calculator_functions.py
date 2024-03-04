# function

def calculator (number1,number2,operation):
        if operation=="division":
            if number2==0:
                print(f"enter numbers different than 0 for this operation to work")
            else:
                return number1/number2
        elif operation =="multiplication":
             return number1 * number2
        elif operation =="substraction":
             return number1 - number2
        elif operation =="addition":
             return number1 + number2

# Main program

number1=float(input("Enter a number: "))
number2=float(input("Enter another number: "))
operation=input("Choose an operator between \naddition, \nsubstraction, \nmultiplication \nor division\n\n ")

#calling the function
print(f"\nThe {operation} of {number1} and {number2} is {calculator(number1,number2, operation)}")
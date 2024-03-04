# function

def check_even_odd(user_number):
    if user_number %2 == 0:
        return f"{user_number} is an even number"
    else:
        return f"{user_number} is an odd number"

# main program
    
user_number = int(input("Your number is: "))

print(check_even_odd(user_number))

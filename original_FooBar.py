# using while-loop

n = 0  # initializing
while n <= 14:
    n = n+1 
    if n %3 == 0 and n %5 == 0:
        print("FooBar")
    elif n %3 ==0:
        print("Foo")
    elif n %5 == 0:
        print("Bar")
    else:
        print(n) # if not a multiple of 3 or 5 within the range

# using for-loop

# for number in range (1, 16):    
#     if number %3 == 0 and number %5 == 0:
#         print("FooBar")
#     elif number %3 ==0:
#         print("Foo")
#     elif number %5 == 0:
#         print("Bar")
#     else:
#         print(number) # if not a multiple of 3 or 5 within the range

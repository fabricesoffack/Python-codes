

number = int(input("give me a number between 0-50: "))

if number >= 0 and number <= 50:
    if number %5 == 0 and number %7 == 0:
        print("FooBar")
    elif number %7 == 0:
        print("Bar")
    elif number %5 ==0:
        print("Foo")
    else:
        print(None) # if not a multiple of 5 or 7 within the range
else:
    print("not applicable") # if the number is not in the range of 0 to 50

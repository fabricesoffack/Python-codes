
def multiply_even_numbers(numbers):
    
    """
    args:
    numbers (list of integers) : all numbers are integers

    Returns:
    product = 1
    By initializing "product" to 1, we ensure that when we start multiplying the even numbers, the initial value of "product" does not affect the result.

    product = product * num
    because we are multiplying the current value of "product" by "num", and then assigning the result back to product

    """
    product = 1

    for num in numbers: 
        if num %2 == 0: 
            product = product*num
    return product

numbers = [ 8, 9, 11, 20, 32, 101, 100]

# call the function  
print(multiply_even_numbers(numbers))
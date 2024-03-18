
def sales():
    """
    Generate a receipt for the order below and save it to a file named "receipt.txt

    Args:
    - order (dict): A dictionary containing items as keys and prices as their respective values.
    - receipt.txt (str): The filename where the order will be saved.

    Returns:
    - the function does not return any value
    """    
# Using the .values() method to get all the values from the dictionary  
    order = {"tomato":30, "thyne":4.50, "garlic":7.5, "onions":4, "fish":9.99}        
    total_items = sum(order.values())
    try:
# using the .items() method to iterate over a dictionary to access both keys and values within a loop
        with open("receipt.txt", "w") as grocery_cart:
            for item, price in order.items():
                grocery_cart.write(f"{item}:{price}\n")
            grocery_cart.write(f"\ntotal = {total_items}")
        print(f"Receipt generated successfully and saved to {'receipt.txt'}")
    except FileNotFoundError:
        print(f"we cannot find your file {'receipt.txt'}")    
    except PermissionError:
        print(f"Error: Permission denied while writing to {'receipt.txt'}")
    except Exception as e:
        print(f"An error occurred: {e}")
#  call the function from the main
sales()

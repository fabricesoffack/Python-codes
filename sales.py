
def sales():
        
# Using the .values() method to get all the values from the dictionary  
    order = {"tomato":30, "thyne":4.50, "garlic":7.5, "onions":4, "fish":9.99}        
    total_items = sum(order.values())

    with open("receipt.txt", "w") as grocery_cart:
# using the .items() method to iterate over a dictionary to access both keys and values within a loop

            for item, price in order.items():
                grocery_cart.write(f"{item}:{price}\n")
            grocery_cart.write(f"\ntotal = {total_items}")
                        
#  call the function from the main
sales()

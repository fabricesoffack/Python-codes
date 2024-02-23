
# The use of max() and min() build-in function

lists = [[3,4,5,6], [-1,-2,-3,-4], [0,0,0,0,], []]
max_value = max([3,4,5,6], [-1,-2,-3,-4], [0,0,0,0,], [])
min_value = min([3,4,5,6], [-1,-2,-3,-4], [0,0,0,0,], [])

# lst is a variable name that typically stands for "list" or "sequence". 
# It represents a list object or any other iterable object
# if the list lst is empty, it evaluates to False. 
# If the list contains any elements, it evaluates to True.
# "if lst" is a conditional statement that checks whether the variable lst evaluates to True

for lst in lists:
    if lst:
        max_value = max(lst)    
        min_value = min(lst)
        print(f"{max_value} {min_value}")
    else:
        print("None")




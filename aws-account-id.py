# using the "find()" method to identify the account_id
arn = "arn:iam::123456789012:user/Development/product_1234/*"

# The start index begins after "iam::" 
start_index = arn.find("iam::") + 5

# The end index closes the end of the count
end_index = arn.find(":user")

# Extract the account ID using the identified indices
account_id = arn[start_index:end_index] 

print(f"the aws account id is: {account_id}")


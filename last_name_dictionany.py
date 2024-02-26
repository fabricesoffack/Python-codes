d = {
    "employees": [
        {"firstName": "John", "lastName": "Doe"},
        {"firstName": "Anna", "lastName": "Smith"},
        {"firstName": "Peter", "lastName": "Jones"}
    ],
    "owners": [
        {"firstName": "Jack", "lastName": "Petter"},
        {"firstName": "Jessy", "lastName": "Petter"}
    ]
}

# Get the list of employees
employees = d["employees"]

# Get the last name of the second employee
second_employee_last_name = employees[1]["lastName"]

print(f"Last name of the second employee: {second_employee_last_name}")



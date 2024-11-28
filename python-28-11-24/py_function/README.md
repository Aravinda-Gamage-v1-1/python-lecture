### Arbitrary arguments
Mainly there are two types.
1. Arbitrary positional arguments (*args)
2. Arbitrary keyword arguments (**kwargs)

Arbitrary positional arguments

def employee_info(name, **kwargs):
    # Printing the employee name
    print(f"Employee Name: {name}")
    
    # Iterating through the keyword arguments and printing each key-value pair
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
    # Returning a dictionary containing all the employee details
    employee_details = {"name": name}
    employee_details.update(kwargs)
    return employee_details

# Example usage
details = employee_info("John Doe", age=30, department="IT", position="Developer")
print(details)

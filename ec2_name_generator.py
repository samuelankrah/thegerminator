import random
import string

def generate_unique_name(department, length=8):
    """
    Generate a unique name based on the department name and a random alphanumeric string.
    
    :param department: str, name of the department.
    :param length: int, length of random alphanumeric string. Default value is 8.
    :return: str, unique name.
    """
    
    # Generate a random string of letters and digits with the given length.
    random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    # Return the formatted unique name combining department and random part.
    return f"{department}_{random_part}"

def main():
    # List of allowed departments in lowercase for easy comparison.
    allowed_departments = ["marketing", "accounting", "finops"]

    # Get the number of EC2 instance names the user wants.
    num_of_instances = int(input("Enter the number of EC2 instances you want names for: "))
    
    # Get the department name and convert it to lowercase for easy comparison.
    department = input("Enter your department name: ").lower()

    # Check if the department is allowed.
    if department not in allowed_departments:
        print("You should not use this Name Generator. Only Marketing, Accounting, and FinOps Departments are allowed.")
        return

    # Generate and print unique names for the specified number of instances.
    for _ in range(num_of_instances):
        print(generate_unique_name(department))

# Check if this script is being run as the main module.
if __name__ == "__main__":
    # If so, execute the main function.
    main()

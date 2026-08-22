def sanitize_name(first_name, last_name):
    
    first_name = first_name.strip()
    last_name = last_name.strip()

    full_name = f"{first_name} {last_name}".title()

    return full_name

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print("Clean name:", sanitize_name(first_name, last_name))

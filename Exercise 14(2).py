phonebook = {}
def add_contact():
    name = input("Enter name: ").strip()
    number = input("Enter contact number: ").strip()

    if name in phonebook:
        print("Contact already exists!")
        print("Existing number:", phonebook[name])
    else:
        phonebook[name] = number
        print("Contact added successfully!")

def display_contacts():
    if not phonebook:
        print("Phonebook is empty.")
        return

    print("\n========== PHONEBOOK ==========")

    for name, number in phonebook.items():
        print(f"Name   : {name}")
        print(f"Number : {number}")
        print("-------------------------------")

def main():
    while True:
        print("\n========== MENU ==========")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Exit")
        print("==========================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            display_contacts()

        elif choice == "3":
            print("Thank you for using Phonebook!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

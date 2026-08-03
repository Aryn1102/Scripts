contacts ={}

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact by Name")
        print("4. Search Contact by Phone Number")
        print("5. Update Contact")
        print("6. Delete Contact")
        print("7. Prevent Duplicates")
        print("8. Add Additional Information")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            search_by_phone()
        elif choice == '5':
            update_contact()
        elif choice == '6':
            delete_contact()
        elif choice == '7':
            prevent_duplicates()
        elif choice == '8':
            input_name = input("Enter contact name to add information: ")
            if input_name in contacts:
                info(contacts[input_name])
            else:
                print("Contact not found.")
        elif choice == '9':
            print("Exiting the contact book.")
            break
        else:
            print("Invalid choice. Please try again.")

def add_contact():
    input_name = input("Enter contact name: ")
    input_phone = int(input("Enter contact phone number: "))
    contacts[input_name] = {"phone": input_phone}
    add_info = input("Do you want to add additional information about the contact? (yes/no): ")
    if add_info.lower() == "yes":
        info(contacts[input_name])

def view_contacts():
    for name, contact_info in contacts.items():
        print(f"{name}: {contact_info['phone']} email: {contact_info.get('email', 'N/A')} address: {contact_info.get('address', 'N/A')}")

def search_contact():
    input_name = input("Enter contact name to search: ")
    if input_name in contacts:
        print(f"{input_name}: {contacts[input_name]}")
    else:
        print("Contact not found.")

def delete_contact():
    input_name = input("Enter contact name to delete: ")
    if input_name in contacts:
        del contacts[input_name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

def update_contact():
    input_name = input("Enter contact name to update: ")
    if input_name in contacts:
        new_phone = int(input("Enter new phone number: "))
        contacts[input_name]["phone"] = new_phone
        print("Contact updated.")
    else:
        print("Contact not found.")

def prevent_duplicates():
    input_name = input("Enter contact name: ")
    if input_name in contacts:
        print("Contact already exists.")
    else:
        input_phone = int(input("Enter contact phone number: "))
        contacts[input_name] = {"phone": input_phone}
        print("Contact added.")

def info(contact):
    input_info = input("Enter the type of additional information about the contact: ")
    input_value = input(f"Enter the {input_info}: ")
    contact[input_info] = input_value

def search_by_phone():
    input_phone = int(input("Enter contact phone number to search: "))
    found = False
    for name, contact_info in contacts.items():
        if contact_info['phone'] == input_phone:
            print(f"{name}: {contact_info['phone']}")
            found = True
            break
    if not found:
        print("Contact not found.")

if __name__=="__main__":
    main()
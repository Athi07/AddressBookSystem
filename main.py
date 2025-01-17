from addressbook import AddressBook

print("Welcome to Address Book Program!")

address_book = AddressBook()

while True:
    print("\nChoose Option: ")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Exit")

    option = int(input("Enter Option: "))

    if option == 1:
        address_book.add_contact()
    
    elif option == 2:
        address_book.display_contacts()
    
    else:
        break
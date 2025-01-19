from addressbook import AddressBook

print("Welcome to Address Book Program!")

address_book = dict()

while True:
    print("\nChoose Option: ")
    print("1. Add a new Address Book")
    print("2. Select an Address Book")
    print("3. Display all Address Books")
    print("4. Exit")

    option = int(input("Enter Option: "))

    if option == 1:
        ab_name = input("Enter the name of the address book: ")
        if ab_name in address_book:
            print("This address book already exists!")
        else:
            address_book[ab_name] = AddressBook()
            print(f"Address book with name {ab_name} created!")

    elif option == 2:
        name = input("Enter the name of the address book: ")
        if name not in address_book:
            print(f"No address book found with the name {name}!")
        else:
            select = address_book[name]
            while True:
                    print(f"\nAddress Book: {name}")
                    print("1. Add Contact")
                    print("2. Display Contacts")
                    print("3. Edit Contact")
                    print("4. Delete Contact")
                    print("5. Back to Address Book Menu")

                    choice = int(input("Choose option: "))

                    if choice == 1:
                        select.add_contact()

                    elif choice == 2:
                        select.display_contacts()

                    elif choice == 3:
                        select.edit_contact()

                    elif choice == 4:
                        select.delete_contact()

                    elif choice == 5:
                        break

                    else:
                        print("Invalid Option!")

    elif option == 3:
        if len(address_book) == 0:
            print("No Address Books Found!")
        
        else:
            for book in address_book:
                print(f"\n{book}")

    elif option == 4:
        break
    
    else:
        print("Invalid Option!")
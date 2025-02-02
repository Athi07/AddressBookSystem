from addressbook import AddressBook

print("Welcome to Address Book Program!")

address_book = dict()

while True:
    print("\nChoose Option: ")
    print("1. Add a new Address Book")
    print("2. Select an Address Book")
    print("3. Display all Address Books")
    print("4. Search by City")
    print("5. Search by State")
    print("6. Number of Contacts living in the same city")
    print("7. Number of Contacts living in the same state")
    print("8. Sort Entries in Address Book alphabetically by name")
    print("9. Sort Entries in Address Book using city, state or zipcode.")
    print("10. Save Address Book to a file")
    print("11. Load Address Book from a file")
    print("12. Save address book as CSV")
    print("13. Load address book from CSV")
    print("14. Save address book as JSON")
    print("15. Load address book as JSON")
    print("16. Exit")

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
        res = []
        search = "city"
        city = input("Enter the name of the city to search: ")
        for book, abook in address_book.items():
            for contact in abook.search_city_state(city, search):
                res.append(contact)

        if len(res) != 0:
            for contact in res:
                print(contact)
                print()

        else:
            print(f"No contacts found with the city name {city}")

    elif option == 5:
        res = []
        search = "state"
        state = input("Enter the name of the state to search: ")
        for book, abook in address_book.items():
            for contact in abook.search_city_state(state,search):
                res.append(contact)

        if len(res) != 0:
            for contact in res:
                print(contact)
                print()
        
        else:
            print(f"No contacts found with the state name {state}")
    
    elif option == 6:
        res = []
        search = "city"
        city = input("Enter the name of the city to search: ")
        for book,abook in address_book.items():
            for contact in abook.search_city_state(city, search):
                res.append(contact)
        print(f"The number of contacts existing with the city name {city} are: {len(res)}")

        if len(res) == 0:
            print(f"No contacts found with the city name {city}")

    elif option == 7:
        res = []
        search = "state"
        state = input("Enter the name of the state to search: ")
        for book,abook in address_book.items():
            for contact in abook.search_city_state(state, search):
                res.append(contact)
        print(f"The number of contacts existing with the state name {state} are: {len(res)}")

        if len(res) == 0:
            print(f"No contacts found with the state name {state}")

    elif option == 8:
        name = input("Enter the name of the address book you want to sort: ")
        if name in address_book:
            address_book[name].sort_contacts_by_name()
        else:
            print(f"No address book found with name {name}")

    elif option == 9:
        name = input("Enter the name of the address book you want to sort: ")
        if name in address_book:
            select = address_book[name]
            print("\Sort by: ")
            print("1. City")
            print("2. State")
            print("3. Zip Code")

            choice = int(input("Choose option: "))

            if choice == 1:
                select.sort_contacts_by_fields("City")
            elif choice == 2:
                select.sort_contacts_by_fields("State")
            elif choice == 3:
                select.sort_contacts_by_fields("Zip")
            else:
                print("Invalid option!")
        
        else:
            print(f"No address book found with the name {name}")

    elif option == 10:
        name = input("Enter the name of the address book to save: ")
        if name in address_book:
            filename = input("Enter the filename to store: ")
            address_book[name].save_file(filename)
        else:
            print(f"No address book found with the name {name}")
            
    elif option == 11:
        name = input("Enter the name of the address book to load into: ")
        filename = input("Enter the filename to load into: ")
        if name not in address_book:
            address_book[name] = AddressBook()
            address_book[name].load_file(filename)

    elif option == 12:
        name = input("Enter the name of the address book to save: ")
        if name in address_book:
            filename = input("Enter the filename to save as (CSV): ")
            address_book[name].save_to_csv(filename)
        else:
            print(f"No address book found with the name {name}")

    elif option == 13:
        name = input("Enter the name of the address book to load into: ")
        filename = input("Enter the filename to load from (CSV): ")
        if name not in address_book:
            address_book[name] = AddressBook()
        address_book[name].load_from_csv(filename)

    elif option == 14:
        name = input("Enter the name of the address book to save: ")
        if name in address_book:
            filename = input("Enter the filename to save as (JSON): ")
            address_book[name].save_to_json(filename)
        else:
            print(f"No address book found with the name {name}")

    elif option == 15:
        name = input("Enter the name of the address book to load into: ")
        filename = input("Enter the filename to load from (JSON): ")
        if name not in address_book:
            address_book[name] = AddressBook()
        address_book[name].load_from_json(filename)

    elif option == 16:
        break

    else:
        print("Invalid Option!")
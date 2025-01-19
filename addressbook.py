from contacts import Contacts

class AddressBook:
    def __init__(self):
        self.contacts_list = []

    def add_contact(self):
        while True:
            self.first = input("Enter First Name: ")
            self.last = input("Enter Last Name: ")
            # Duplicate contact
            for i in self.contacts_list:
                if i.first == self.first and i.last == self.last:
                    print("This contact already exists!")
                    return
            self.address = input("Enter Address: ")
            self.city = input("Enter City: ")
            self.state = input("Enter State: ")
            self.zip = input("Enter Zip Code: ")
            self.phone = input("Enter Phone Number: ")
            self.email = input("Enter Email ID: ")

            new_contact = Contacts(self.first, self.last, self.address, self.city, self.state, self.zip, self.phone, self.email)

            self.contacts_list.append(new_contact)

            additional = input("Do you want to add another contact (Yes/No): ").lower()
            if additional == 'no':
                break

    def display_contacts(self):
        if len(self.contacts_list) == 0:
            print("No Contacts available")
        
        else:
            for contact in self.contacts_list:
                print(contact)
                print()

    def find_contact(self, first_name, last_name):
        for contact in self.contacts_list:
            if contact.first == first_name and contact.last == last_name:
                return contact
        else:
            return None
        
    def edit_contact(self):
        
        first_name = input("Enter the first name of the contact: ")
        last_name = input("Enter the last name of the contact: ")

        contact = self.find_contact(first_name, last_name)

        if contact is None:
            print("No contact found with this first and last name!")
        else:
            print("Contact found!")
            #Select field to edit
            print("\nSelect the field you want to edit: ")
            print("1. Address")
            print("2. City")
            print("3. State")
            print("4. Zip Code")
            print("5. Phone Number")
            print("6. Email ID")

            option = int(input("Choose option: "))

            if option == 1:
                contact.address = input("Enter the new address: ")

            elif option == 2:
                contact.city = input("Enter the new City details: ")

            elif option == 3:
                contact.state = input("Enter the new State details: ")

            elif option == 4:
                contact.zip = input("Enter the new Zip Code details: ")

            elif option == 5:
                contact.phone = input("Enter the new Phone Number details: ")

            elif option == 6:
                contact.email = input("Enter the new Email ID details: ")

            else:
                print("Invalid Choice!")

        print("Contact Updated!")

    def delete_contact(self):

        first_name = input("Enter the first name of the contact: ")
        last_name = input("Enter the last name of the contact: ")

        contact = self.find_contact(first_name,last_name)

        if contact is None:
            print("Contact not found!")

        else:
            print("Contact Found!")
            for _ in self.contacts_list:
                if contact in self.contacts_list:
                    self.contacts_list.remove(contact)
                    print("Contact Deleted!")
                

from contacts import Contacts

class AddressBook:
    def __init__(self):
        self.contacts_list = []

    def add_contact(self):
        self.first = input("Enter First Name: ")
        self.last = input("Enter Last Name: ")
        self.address = input("Enter Address: ")
        self.city = input("Enter City: ")
        self.state = input("Enter State: ")
        self.zip = input("Enter Zip Code: ")
        self.phone = input("Enter Phone Number: ")
        self.email = input("Enter Email ID: ")

        new_contact = Contacts(self.first, self.last, self.address, self.city, self.state, self.zip, self.phone, self.email)

        self.contacts_list.append(new_contact)

    def display_contacts(self):
        if len(self.contacts_list) == 0:
            print("No Contacts available")
        
        else:
            for contact in self.contacts_list:
                print(contact)
    
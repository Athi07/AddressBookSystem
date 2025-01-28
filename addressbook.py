import csv
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
                

    def search_city_state(self, location, search):
        match = []
        for contact in self.contacts_list:
            if (search == "city" and contact.city.lower() == location.lower()) or (search == "state" and contact.state.lower() == location.lower()):
                match.append(contact)

        return match

    def sort_contacts_by_name(self):
        self.contacts_list.sort(key = lambda contact: (contact.first.lower(), contact.last.lower()))
        print("Contacts sorted alphabetcally by name!")
        self.display_contacts()

    def sort_contacts_by_fields(self, field):
        if field.lower() == "city":
            self.contacts_list.sort(key = lambda contact: (contact.city.lower()))
        elif field.lower() == "state":
            self.contacts_list.sort(key = lambda contact: (contact.state.lower()))
        elif field.lower() == "zip":
            self.contacts_list.sort(key = lambda contact: (contact.zip))

        if field.lower() not in ["city","state","zip"]:
            print("Invalid field!, Please choose city, state or zip")
            return
        
        print(f"Contacts sorted by {field}")
        self.display_contacts()

    def save_file(self, filename):
        with open(filename,'w') as file:
            for contact in self.contacts_list:
                file.write(f"{contact.first},{contact.last},{contact.address},{contact.city},{contact.state},{contact.zip},{contact.phone},{contact.email}\n")
        print(f"Address Book saved to filename {filename}!")
    
    def load_file(self,filename):
        with open(filename,'r') as file:
            self.contacts_list = []
            for line in file:
                data = line.strip().split(",")
                if len(data) == 8:
                    contact = Contacts(*data)
                    self.contacts_list.append(contact)
                else:
                    print(f"There are some fields missing in this file {filename}.")
            print(f"Address Booked loaded successfully from {filename}!")

    def save_to_csv(self,filename):
        with open(filename,'w',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['First Name','Last Name','Address','City','State','Zip','Phone','Email'])
            for contact in self.contacts_list:
                writer.writerow([contact.first,contact.last,contact.address,contact.city,contact.state,contact.zip,contact.phone,contact.email])
            print(f"Address Book saved as {filename}!")

    def load_from_csv(self,filename):
        with open(filename,'r') as csvfile:
            reader = csv.DictReader(csvfile)
            self.contacts_list = []
            for row in reader:
                contact = Contacts(row['First Name'],row['Last Name'],row['Address'],row['City'],row['State'],row['Zip'],row['Phone'],row['Email'])
                self.contacts_list.append(contact)
            print(f"Address book loaded from file {filename}!")
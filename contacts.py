class Contacts:
    def __init__(self, firstname, lastname, address, city, state, zip, phone_no, email):
        self.first = firstname
        self.last = lastname
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone_no
        self.email = email
        
    def __str__(self):
        return (f"Name: {self.first} {self.last}\n"
                f"Address: {self.address}, {self.city}, {self.state}, {self.zip}\n"
                f"Phone: {self.phone}\nEmail: {self.email}")
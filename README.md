# Address Book System

An Address Book System in Python that allows users to manage contacts by creating, reading, updating, and deleting information. It also supports saving and loading contacts as CSV and JSON files for persistence.

## Features

- Add, edit, delete, and display contacts.
- Save and load the address book as CSV files.
- Save and load the address book as JSON files.
- Validate email and phone numbers.

## Requirements

- Python 3.6+

## Project Structure

```plaintext
AddressBookSystem/
|-- main.py               # Entry point for the application
|-- addressbook.py        # AddressBook class implementation
|-- contacts.py           # Contacts class implementation
|-- README.md             # Documentation file
```

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Athi07/AddressBookSystem.git
   ```
2. Navigate to the project directory:
   ```bash
   cd AddressBookSystem
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## How to Use

### Main Menu Options

1. **Add a Contact**: 
   Enter details such as first name, last name, address, city, state, zip code, phone number, and email.

2. **Edit a Contact**:
   Modify existing contact details by specifying the contact name.

3. **Delete a Contact**:
   Remove a contact from the address book.

4. **Display Contacts**:
   View all contacts in the address book.

5. **Save to CSV File**:
   Save the current address book to a CSV file.

6. **Load from CSV File**:
   Load contacts from an existing CSV file.

7. **Save to JSON File**:
   Save the current address book to a JSON file.

8. **Load from JSON File**:
   Load contacts from an existing JSON file.

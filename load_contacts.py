import csv

def load_all_contacts():
    """Load contacts from the CSV file."""
    contacts = []
    try:
        with open('contacts.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append({
                    'name': row['Name'],
                    'email': row['Email'],
                    'phone': row['Phone'],
                    'address': row['Address']
                })
    except FileNotFoundError:
        print("No previous contacts found. Starting with an empty contact list.")
    return contacts

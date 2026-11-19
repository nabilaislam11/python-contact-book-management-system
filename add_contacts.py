import save_contacts

def add_contactss(contacts):
    name = input("Enter Name: ").strip()
    if not name.isalpha():
        print("Error: The contact's name must be a string.")
        return contacts

    email = input("Enter Email: ").strip()
    phone = input("Enter Phone Number: ").strip()
    if not phone.isdigit():
        print("Error: The phone number must be an integer.")
        return contacts

    for contact in contacts:
        if contact['phone'] == phone:
            print("Error: This phone number is already assigned to another contact.")
            return contacts

    address = input("Enter Address: ").strip()
    new_contact = {'name': name, 'email': email, 'phone': phone, 'address': address}
    contacts.append(new_contact)
    print("Contact added successfully!")
    save_contacts.save_to_file(contacts)
    return contacts

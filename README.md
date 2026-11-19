# Contact Book Management System

A modular **Python command-line application** for managing contact records with CSV persistence.

## Features

- Add contact details (name, email, phone, and address)
- Search contacts by name, email, or phone number
- View saved contacts in a formatted table
- Update individual contact records
- Delete contacts by selection
- Preserve records in a CSV file across application sessions
- Validate phone number input and prevent duplicate phone entries

## Run locally

Requires Python 3.9+ and no third-party packages.

```bash
git clone https://github.com/nabilaislam11/python-contact-book-management-system.git
cd python-contact-book-management-system
python main.py
```

Choose an option from the menu to manage contacts. Data is saved to `contacts.csv` in the current project directory.

## Run tests

```bash
python -m unittest discover -s tests -v
```

The [GitHub Actions workflow](.github/workflows/python-tests.yml) compiles the Python modules and runs seven regression tests covering CSV persistence, addition, duplicate detection, updating, searching, deleting, and empty contact lists.

## Project structure

| File | Responsibility |
| --- | --- |
| `main.py` | Interactive command-line menu |
| `add_contacts.py` | Add new contact records |
| `search_contacts.py` | Search contact records |
| `update_contacts.py` | Modify saved contact records |
| `view_all_contacts.py` | Display contacts |
| `delete_all_contact.py` | Remove selected contacts |
| `load_contacts.py` | Read CSV storage |
| `save_contacts.py` | Write CSV storage |
| `contacts.csv` | Local contact data |
| `tests/` | Automated regression tests |
| `ContactBook.rar` | Original project archive |

## Technologies

Python · Standard Library · CSV file handling · unittest

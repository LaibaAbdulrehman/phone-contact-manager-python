contacts = {}   # Hash Map (Dictionary)

def add_contact():
    name = input("Enter name: ")
    number = input("Enter number: ")
    contacts[name] = number
    print("\nContact Added Successfully!")
    

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"Contact Found: {name} -> {contacts[name]}")
    else:
        print("Contact Not Found")


def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact Deleted Successfully!")
    else:
        print("Contact Not Found")
    
def display_contacts():
    if len(contacts) == 0:
        print("Contact List Empty")
    else:
        print("\n---- Contact List ----")
        for name, number in contacts.items():
            print(name, " -> ", number)
    

while True:
    print("\n==== Phone Contact Management ====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show All Contacts")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        delete_contact()
    elif choice == 4:
        display_contacts()
    elif choice == 5:
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice! Try Again.")

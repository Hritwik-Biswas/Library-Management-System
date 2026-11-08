import json
import os

FILE_NAME = "library.json"

# ---------------- FILE HANDLING ---------------- #
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# ---------------- CORE FUNCTIONS ---------------- #
def add_book():
    data = load_data()
    
    book_id = input("Enter Book ID: ")
    
    # Check duplicate
    for book in data:
        if book["id"] == book_id:
            print("❌ Book ID already exists!\n")
            return
    
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    
    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "issued": False,
        "issued_to": ""
    }
    
    data.append(book)
    save_data(data)
    print("✅ Book added successfully!\n")

def view_books():
    data = load_data()
    
    if not data:
        print("No books available.\n")
        return
    
    print("\n📖 BOOK LIST")
    print("-" * 50)
    for b in data:
        print(f"ID: {b['id']}")
        print(f"Title: {b['title']}")
        print(f"Author: {b['author']}")
        print(f"Issued: {'Yes' if b['issued'] else 'No'}")
        if b['issued']:
            print(f"Issued To: {b['issued_to']}")
        print("-" * 50)

def search_book():
    data = load_data()
    keyword = input("Enter Book ID or Title: ").lower()
    
    found = False
    for b in data:
        if keyword in b["id"].lower() or keyword in b["title"].lower():
            print("\n✅ Book Found")
            print(b)
            found = True
    
    if not found:
        print("❌ Book not found.\n")

def issue_book():
    data = load_data()
    book_id = input("Enter Book ID to issue: ")
    
    for b in data:
        if b["id"] == book_id:
            if b["issued"]:
                print("❌ Book already issued!\n")
                return
            
            name = input("Enter student name: ")
            b["issued"] = True
            b["issued_to"] = name
            
            save_data(data)
            print("✅ Book issued successfully!\n")
            return
    
    print("❌ Book not found.\n")

def return_book():
    data = load_data()
    book_id = input("Enter Book ID to return: ")
    
    for b in data:
        if b["id"] == book_id:
            if not b["issued"]:
                print("❌ This book was not issued!\n")
                return
            
            b["issued"] = False
            b["issued_to"] = ""
            
            save_data(data)
            print("✅ Book returned successfully!\n")
            return
    
    print("❌ Book not found.\n")

def delete_book():
    data = load_data()
    book_id = input("Enter Book ID to delete: ")
    
    for b in data:
        if b["id"] == book_id:
            data.remove(b)
            save_data(data)
            print("✅ Book deleted successfully!\n")
            return
    
    print("❌ Book not found.\n")

# ---------------- MENU ---------------- #
def menu():
    while True:
        print("\n" + "="*45)
        print("📚 LIBRARY MANAGEMENT SYSTEM")
        print("="*45)
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")
        
        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            print("Thank you for using the system!")
            break
        else:
            print("❌ Invalid choice!\n")

# ---------------- MAIN ---------------- #
if __name__ == "__main__":
    menu()
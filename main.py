library = [
    {"title": "The Great Gatsby", 
     "author": "F. Scott Fitzgerald", 
     "year": 1925, 
     "available": True},

    {"title": "To Kill a Mockingbird", 
     "author": "Harper Lee", 
     "year": 1960, 
     "available": True},

    {"title": "1984", 
     "author": "George Orwell", 
     "year": 1949, 
     "available": True}
]

def exit_program():
    print("Thank you for using the Library Management System.")
    print("Goodbye!")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            search_book()
        elif choice == "5":
            remove_book()
        elif choice == "6":
            exit_program()
            break
        else:
            print("Invalid option. Please choose a number between 1 and 6.")

def display_menu():
    print ("""
==========================
Library Management System
==========================
1. Add Book
2. View Books
3. Borrow Book
4. Search Book
5. Remove Book
6. Exit
""")
    return
    
def add_book():
    # author = input("Enter the book author: ").strip()
    # year = int(input("Enter the publication year: "))
    while True:
            title = input("Enter the book title: ").strip()

            if title == "":
                print("Title cannot be empty. Please enter a valid title.")
            else:
                break

    while True:
            author = input("Enter the book author: ").strip()

            if author == "":
                print("Author cannot be empty. Please enter a valid author.")
            else:
                break
    
    while True:
            try:
                year = int(input("Enter the publication year: "))

                if year < 0:
                    print("Year cannot be negative. Please enter a valid year.")
                    continue
                
                break

            except ValueError:
                print("Invalid input. Please enter a valid year.")
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "available": True
    }

    for existing_book in library:
        if existing_book["title"].strip().lower() == title.strip().lower() and existing_book["author"].strip().lower() == author.strip().lower():
            print(f"Book '{title}' already exists in the library.")
            return
        
    library.append(book)
    print(f"Book '{title}' by {author} ({year}) added successfully!")

def view_books():
    if not library:
        print("No books available in the library.")
        return

    count = len(library)
    if count == 1:
        print("There is 1 book available in the library.")
    else:
        print(f"There are {count} books available in the library.")

    for i, book in enumerate(library, start=1):
        availability = "Yes" if book["available"] else "No"
        print(f"{i}. {book['title']} by" )
        print(f" Author: {book['author']}")
        print(f" Year: {book['year']}")
        print(f" Available: {availability}")
        print()

def search_book():
    title = input("Enter the book title to search: ").strip().lower()
    for book in library:
        if book["title"].strip().lower() == title: 
            availability = "Yes" if book["available"] else "No"
            print(f"Book '{book['title']}' found!")
            print(f"Author: {book['author']}")
            print(f"Year: {book['year']}")
            print(f"Available: {availability}")
            return
    print(f"Book '{title}' not found in the library.")

def borrow_book():
    while True:
        title = input("Enter the book title to borrow: ").strip().lower()
        for book in library:
            if book["title"].strip().lower() == title:
                if book["available"]:
                    book["available"] = False
                    print(f"You have successfully borrowed '{book['title']}'.")
                else:
                    print(f"Sorry, '{book['title']}' is currently not available.")
                return
        print(f"Book '{title}' not found in the library. Please try again.")

def remove_book():
    title = input("Enter the book title to remove: ").strip().lower()
    for index, book in enumerate(library):
        if book["title"].strip().lower() == title:
            del library[index]
            print(f"Book '{book['title']}' removed successfully!")
            return
    print(f"Book '{title}' not found in the library.")

main()

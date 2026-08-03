import json
import sys

books={}

def main():
    while True:
        print("1. Add book")
        print("2. View book")
        print("3. Search book")
        print("4. Issue book")
        print("5. return book")
        print("6. Delete book")
        print("7. Show available books")
        print("8. Show issued books")
        print("9. Save data")
        print("10. Load data")
        choice = int(input("Enter your Choice"))
        if choice == 1:
            add_book()
        elif choice == 2:
            view_books()
        elif choice == 3:
            search_book()
        elif choice == 4:
            issue_book()
        elif choice == 5:
            return_book()
        elif choice == 6:
            delete_book()
        elif choice ==7:
            show_available_books()
        elif choice == 8:
            show_issued_books()
        elif choice == 9:
            save_data()
        elif choice == 10:
            load_data()
        elif choice == 11:
            sys.exit()

def add_book():
    book_id = input("Enter the book ID")
    title =  input("Enter the title")
    author = input("Enter the name of the author")
    genre = input("Enter the genre of the book")
    year = int(input("Enter the year of the book"))
    available = True
    issued_to = None
    if book_id in books:
        print("Book already exists")
    books[book_id] = {"Title": title, "Author": author, "Genre": genre, "Year": year, "Available": available, "Issued to": issued_to}

def view_books():
    for book_id, book in books.items():
        print(f"ID: {book_id}, Title: {book['Title']}, Author: {book['Author']}")

def search_book():
    book_id = input("Enter the book ID or name to search")
    found=False
    for books_id, item in books.items():
        if book_id == books_id or book_id == item['Title']:
            found=True
            print(f"{book_id} found.")
            break
    if not found:
        print(f"book {book_id} not found.")

def issue_book():
    name = input("Enter the student name")
    book_id = input("Enter the book id")
    for books_id, item in books.items():
        if books_id == book_id:
            if item["Available"]:
                item["Available"] = False
                item["Issued to"] = name
                break
            else:
                print("Item not available")
    

def return_book():
    book_id = input("Enter the book id")
    if book_id in books:
        books[book_id]["Available"] = True
        books[book_id]["Issued to"] = None

def delete_book():
    book_id = input("Enter the book id")
    if book_id in books:
        del books[book_id]
        print("Successfully deleted")
    else:
        print("Book not Found")

def show_available_books():
    for book_id, book in books.items():
        if book["Available"]:
            print(book.items())

def show_issued_books():
    for book_id, book in books.items():
        if not book["Available"]:
            print(book.items())

def save_data():
    with open("library.json", "w") as f:
        json.dump(books, f, indent=4)
    print("Data Saved")

def load_data():
    global books
    with open("library.json", "r") as f:
        books = json.load(f)

if __name__=="__main__":
    main()
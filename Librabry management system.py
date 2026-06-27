from datetime import datetime, timedelta
# LIBRARY DATABASE
library = {}
# ADD BOOK
def add_book():
    isbn = input("Enter ISBN: ").strip()

    if isbn in library:
        print("Error: ISBN already exists!")
        return

    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()

    library[isbn] = {
        "title": title,
        "author": author,
        "available": True,
        "borrower": None,
        "student_id": None,
        "issue_date": None,
        "due_date": None,
        "waiting_list": []
    }
print("Book Added Successfully!")
# ==========================
# ISSUE BOOK
# ==========================
def issue_book():
    isbn = input("Enter ISBN: ").strip()
    if isbn not in library:
        print("Book not found!")
        return
    book = library[isbn]

    if book["available"]:

        student_id = input("Enter Borrower ID: ").strip()
        borrower = input("Enter Your Name: ").strip()

        issue_date = datetime.now()
        due_date = issue_date + timedelta(days=7)

        book["available"] = False
        book["borrower"] = borrower
        book["student_id"] = student_id
        book["issue_date"] = issue_date
        book["due_date"] = due_date

        print("\nBook Issued Successfully!")
        print("Title :", book["title"])
        print("Due Date :", due_date.strftime("%d-%B-%Y"))
    else:
        print("\nBook Already Issued!")

        name = input("Enter your name for waiting list: ")

        book["waiting_list"].append(name)

        print("Added to waiting list.")
# ==========================
# RETURN BOOK
# ==========================
def return_book():
    isbn = input("Enter ISBN: ").strip()

    if isbn not in library:
        print("Book not found!")
        return
    book = library[isbn]

    if book["available"]:
        print("Book is already available.")
        return

    today = datetime.now()
    fine = 0
    if today > book["due_date"]:
        overdue_days = (today - book["due_date"]).days
        fine = overdue_days * 2

    print("\nBook Returned Successfully!")

    if fine > 0:
        print("Fine Amount: Rs.", fine)

    book["available"] = True
    book["borrower"] = None
    book["student_id"] = None
    book["issue_date"] = None
    book["due_date"] = None

    if book["waiting_list"]:
        next_person = book["waiting_list"].pop(0)
        print("Next Waiting Student:", next_person)


# ==========================
# SEARCH BOOK
# ==========================
def search_book():
    keyword = input(
        "Enter Title/Author/ISBN: "
    ).strip().lower()

    found = False

    for isbn, book in library.items():

        if (keyword in isbn.lower() or
            keyword in book["title"].lower() or
            keyword in book["author"].lower()):

            found = True

            print("\n------------------------")
            print("ISBN:", isbn)
            print("Title:", book["title"])
            print("Author:", book["author"])

            status = (
                "Available"
                if book["available"]
                else "Issued"
            )

            print("Status:", status)

            if not book["available"]:
                print("Borrower:", book["borrower"])

    if not found:
        print("No matching book found.")
# ==========================
# VIEW CATALOG
# ==========================
def view_catalog():
    if not library:
        print("No books available.")
        return
    print("\n============== LIBRARY CATALOG ==============")
    print(
        f"{'ISBN':<18}"
        f"{'TITLE':<25}"
        f"{'AUTHOR':<20}"
        f"{'STATUS':<12}"
    )

    print("-" * 75)

    for isbn, book in library.items():

        status = (
            "Available"
            if book["available"]
            else "Issued"
        )

        print(
            f"{isbn:<18}"
            f"{book['title']:<25}"
            f"{book['author']:<20}"
            f"{status:<12}"
        )

    available = sum(
        1 for b in library.values()
        if b["available"]
    )

    issued = len(library) - available
    print("\nTotal Books :", len(library))
    print("Available   :", available)
    print("Issued      :", issued)
# ==========================
# EXPORT TO FILE
# ==========================
def export_catalog():

    with open("library_report.txt", "w") as file:

        file.write(
            "========== LIBRARY REPORT ==========\n\n"
        )

        for isbn, book in library.items():

            status = (
                "Available"
                if book["available"]
                else "Issued"
            )

            file.write(f"ISBN: {isbn}\n")
            file.write(
                f"Title: {book['title']}\n"
            )
            file.write(
                f"Author: {book['author']}\n"
            )
            file.write(
                f"Status: {status}\n"
            )
            file.write("-" * 40 + "\n")
    print("Catalog exported to library_report.txt")
# ==========================
# LOAD SAMPLE DATA
# ==========================
def load_sample_books():
    sample_books = [
        ("978001", "Python Programming", "John Smith"),
        ("978002", "Data Structures", "Mark Lee"),
        ("978003", "Database Systems", "Thomas Roy"),
        ("978004", "Machine Learning", "Andrew Ng"),
        ("978005", "Operating Systems", "Silberschatz"),
        ("978006", "Swami","Ranjit Desai"),
        ("978009", "Shriman yogi","Babasaheb purandare")
    ]
    for isbn, title, author in sample_books:

        library[isbn] = {
            "title": title,
            "author": author,
            "available": True,
            "borrower": None,
            "student_id": None,
            "issue_date": None,
            "due_date": None,
            "waiting_list": []
        }
# ==========================
# MAIN MENU
# ==========================
def main():

    load_sample_books()

    while True:

        print("\n====== LIBRARY MANAGEMENT SYSTEM ======")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Search Book")
        print("5. View All Books")
        print("6. Export Catalog")
        print("7. Exit")

        try:
            choice = int(
                input("Enter choice: ")
            )
            if choice == 1:
                add_book()

            elif choice == 2:
                issue_book()

            elif choice == 3:
                return_book()

            elif choice == 4:
                search_book()

            elif choice == 5:
                view_catalog()

            elif choice == 6:
                export_catalog()

            elif choice == 7:
                print("Thank You!")
                break
            else:
                print("Invalid Choice")

        except ValueError:
            print(
                "Please enter a valid number."
            )
if __name__ == "__main__":
    main()
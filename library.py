library = {
    "name": "CodeClan Library",
    "books": [
        {
            "author": "George RR Martin",
            "title": "A Song of Ice and Fire"
        },
        {
            "author": "J R. R. Tolkien",
            "title": "The Hobbit"
        },
        {
            "author": "Paul Barry",
            "title": "Head-First Python"
        },
        {
            "author": "Allen B. Downey",
            "title": "Think Python: How to Think Like a Computer Scientist"
        },
        {
            "author": "Eric Matthes",
            "title": "Python Crash Course"
        }
    ]
}

# TODO - Print welcome statement including library name
print("Welcome to " + library["name"])

option = ""
while option != "q":
    print("Options:")
    print("1 - List all books")
    print("2 - Search for a book by title")
    print("3 - Add a book")
    print("4 - Remove a book")
    print("5 - Update a book")
    print("q - Quit")
    option = input("What would you like to do? \n")

    if option == "1":
        print("Listing all books...")
        # TODO - List all books
        print(library["books"])
            # it's got to be a number but if i say [n0] then it prints that one repeatedly

    if option == "2":
        print("Searching for a book by title...")
        # TODO - Search for a book by title
        title = input("Please enter the title of the book you are looking for... ")
        if title == library["books"][title]:
            print("Yes, we have " + library["books"][title] + "in the library")
        else: print("We don't have that book unfortunately")
        # USER INPUT
            # 

    if option == "3":
        print("Adding a book...")
        # TODO - Add a book
        Author = input("Please enter the name of the author of the book you wish to add")
        library["books"]

    if option == "4":
        print("Removing a book...")
        # TODO - Remove a book

    if option == "5":
        print("Updating a book...")
        # TODO - Update a book

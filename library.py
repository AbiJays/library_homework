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
    # formatted string

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
        for book in library["books"]:
            title = book["title"]
            author = book["author"]
            print(f"{title} by {author}")


    if option == "2":
        print("Searching for a book by title...")
        # TODO - Search for a book by title
        searching_title = input("Please enter the title of the book you are looking for... ")
        
        book_found = False
        
        for book in library["books"]:
            # this specifies books so then you can specify titles
            if book["title"] == searching_title:
                # here i specify titles
                book_found = True
        
        if book_found == True:
            print(f"Yes, we have {searching_title}  in the library")
        else: 
            print("We don't have that book unfortunately")


    if option == "3":
        print("Adding a book...")
        # TODO - Add a book
        # {"title": "whatever", "author": "whoever"}
        input_title = input("Please enter the name of the book you wish to add ")
        input_author = input("Please enter the name of the author of the book you wish to add ")
        new_book = {"title": input_title, "author": input_author}

        library["books"].append(new_book)

    if option == "4":
        print("Removing a book...")
        # TODO - Remove a book
        input_title_to_remove = input("What is the title of the book? ")
        input_author_to_remove = input("What is the author of the book? ")
        library["books"].remove({
            "title": input_title_to_remove,
            "author": input_author_to_remove
            })
        input_title_to_remove = input("What book do you want to remove? ")
        books_to_keep = []
        for book in library["books"]:
            if book["title"] != input_title_to_remove:
                books_to_keep.append(book)
        library["books"] = books_to_keep



    if option == "5":
        print("Updating a book...")
        # TODO - Update a book
        title_to_update = input("Enter title: ")
        # first find the book 
        # then loop through to see if its there. 
        # if none, title isn't found, 
        # if book to update found 
        # grab new title, 
        # grab new author 
        # set book to update
        book_to_update = None
        for book in library["books"]:
            if book["title"].lower() == title_to_update.lower():
                book_to_update = book
        if book_to_update != None:
            new_title = input("Enter a new title for this book: ")
            new_author = input("Enter a new author for this book: ")
            book_to_update["title"] = new_title or book_to_update["title"]
            book_to_update["author"] = new_author or book_to_update["author"]
        else:
            print(f"{title_to_update} not found")
        # truthy = not really true but truthy so it works with boolean 
class BookingOperations:
    def __init__(self):
        self.library = []

    def add_book(self, title, author, genre, publication_date, availability=True):
        book = {
            'title': title,
            'author': author,
            'genre': genre,
            'publication_date': publication_date,
            'availability': availability
        }
        self.library.append(book)
        print(f"Book '{title}' has been added to the library.")

    def borrow_book(self, title, user_id, user_operations):
        for book in self.library:
            if book['title'].lower() == title.lower() and book['availability']:
                for user in user_operations.users:
                    if user['user_id'] == user_id:
                        book['availability'] = False
                        user['list_of_books_borrowed'].append(title)
                        print(f"'{title}' has been borrowed by user ID {user_id}.")
                        return
                print(f"User ID {user_id} not found.")
                return
        print(f"Book '{title}' is either not available or not found.")

    def return_book(self, title, user_id, user_operations):
        for user in user_operations.users:
            if user['user_id'] == user_id:
                if title in user['list_of_books_borrowed']:
                    for book in self.library:
                        if book['title'].lower() == title.lower() and not book['availability']:
                            book['availability'] = True
                            user['list_of_books_borrowed'].remove(title)
                            print(f"'{title}' has been returned by user ID {user_id}.")
                            return
        print(f"Book '{title}' could not be returned. Check if it was borrowed by user ID {user_id}.")

    def search_books(self, search_term):
        results = [
            book for book in self.library
            if search_term.lower() in book['title'].lower() or
               search_term.lower() in book['author'].lower() or
               search_term.lower() in book['genre'].lower()
        ]
        if results:
            for book in results:
                print(book)
        else:
            print(f"No books found for '{search_term}'.")

    def display_books(self):
        if not self.library:
            print("The library has no books.")
        else:
            for book in self.library:
                status = "Available" if book['availability'] else "Not available"
                print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, "
                      f"Publication Date: {book['publication_date']}, Status: {status}")


class AuthorOperations:
    def __init__(self):
        self.authors = []

    def add_author(self, author, biography):
        author_entry = {
            'author': author,
            'biography': biography
        }
        self.authors.append(author_entry)
        print(f"Author '{author}' has been added.")

    def view_author_details(self, author_name):
        for author in self.authors:
            if author['author'].lower() == author_name.lower():
                print(f"Author: {author['author']}, Biography: {author['biography']}")
                return
        print(f"Author '{author_name}' not found.")

    def display_all_authors(self):
        if not self.authors:
            print("No authors found.")
        else:
            for author in self.authors:
                print(f"Author: {author['author']}, Biography: {author['biography']}")


class UserOperations:
    def __init__(self):
        self.users = []

    def add_new_user(self, name, user_id):
        user = {
            'user_id': user_id,
            'name': name,
            'list_of_books_borrowed': []
        }
        self.users.append(user)
        print(f"User ID {user_id} ('{name}') has been added.")

    def view_user_details(self, user_id):
        for user in self.users:
            if user['user_id'] == user_id:
                print(f"User ID: {user_id}, Name: {user['name']}, Borrowed Books: {user['list_of_books_borrowed']}")
                return
        print(f"User ID {user_id} not found.")

    def display_all_users(self):
        if not self.users:
            print("No users found.")
        else:
            for user in self.users:
                print(f"User ID: {user['user_id']}, Name: {user['name']}")

from Library_System import BookingOperations,AuthorOperations,UserOperations
from MySQL_Library_Connection import connect_database
booking = BookingOperations()
user_op = UserOperations()
author_op = AuthorOperations()

def main():
    while True:
        try:
            print("Welcome to the Library Management System!")
            print("If You Do Not Have A User ID You Should Make One First!!")
            print("MAIN MENU:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit")
            choice = int(input("Enter A Choice 1-4: "))
        except Exception as e:
            print(f"An Error Occurred: {e}")
            if choice == 4:
                print("Exiting System......")
                break
    
        try:
            if choice == 1:
                print("Booking Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books\n6. Return to main menu")
                user_choice1 = int(input("Enter A Choice 1-6: "))


                if user_choice1 == 1:
                    title = input("Enter Book Title: ")
                    author = input("Enter Author: ")
                    genre = input("Enter The Genre: ")
                    publication_date = input("Enter The Publication date: ")
                    booking.add_book(title, author, genre, publication_date)
                elif user_choice1 == 2:
                    title = input("Enter The Book Title You Would Like To Borrow: ")
                    user_id = int(input("Enter User ID:"))
                    booking.borrow_book(title,user_id,user_op)
                elif user_choice1 == 3:
                    user_id = int(input("Enter User ID: "))
                    title = input("Enter The Book Title: ")
                    booking.return_book(title,user_id,user_op)
                elif user_choice1 == 4:
                    search_term = input("Enter Title or Genre or Author: ")
                    booking.search_books(search_term)
                elif user_choice1 == 5:
                    booking.display_books()
                elif user_choice1 == 6:
                    continue


            elif choice == 2:
                print("User Operations\n 1. Add New User\n2. View User Details\n3. Display All Users\n4. Return To Main Menu")
                user_choice2 = int(input("Enter Number 1-4: "))


                if user_choice2 == 1:
                    user_id = int(input("Enter id number"))
                    name = input("Enter Your Name: ")
                    list_books_borrowed = input("Enter Books Borrowed Separated By Commas: ")
                    user_op.add_new_user(name, user_id, list_books_borrowed)
                elif user_choice2 == 2:
                    user_id = int(input("Enter User ID:"))
                    user_op.view_user_details(user_id)
                elif user_choice2 == 3:
                    user_op.display_all_users()
                elif user_choice2 == 4:
                    continue

            elif choice == 3:
                print(f"Author Operations\n1. Add New Author\n2. View Author Details\n3. Display All Authors\n4. Return To MainMenu")
                user_choice3 = int(input("Enter Choice 1-4: "))
                if user_choice3 == 1:
                    author = input("Enter Author: ")
                    biography = input("Enter Authors Biography")
                    author_op.add_author(author, biography)
                elif user_choice3 == 2:
                    author_name = input("Enter Authors Name: ")
                    author_op.view_author_details(author_name)
                elif user_choice3 == 3:
                    author_op.display_all_authors()
                elif user_choice3 == 4:
                    continue



        except ValueError:
            print("Invalid Need To Be A Integer")

        






if __name__ == "__main__":
    main()

            


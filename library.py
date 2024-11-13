# A function that creates the string model of a repr and returns it
def my_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr

# A decorator that adds the repr function to each class that its attached
def add_repr(cls):
    cls.__repr__ = my_repr
    return cls

# A book class
@add_repr
class Book:
    def __init__(self, title: str, publication_year: int, number_of_copies: int):
        self.title = title.strip()
        self.year = publication_year
        self.copies = number_of_copies

    # Creates a property that returns False when the copies are at 0 and True when they're 1 or higher.
    @property
    def available(self):
        return self.copies > 0

# A user class
@add_repr        
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self._book_list = list()

# A library class
@add_repr
class Library:
    def __init__(self):
        self._book_list = []

    # Adds one or more books to the list. Must've already createad an instance
    def add_book_(self, *book: Book):
        for title in book:
            self._book_list.append(title)

    # Removes a book of the list by its tittle
    def remove_book(self, book_title: str):
        for book in self._book_list:
            if book.title.upper() == book_title.strip().upper():
                self._book_list.remove(book)
                print(f'{book.title} successifully removed... ')
                return

        print('Book not found...')

    # Searchs for a book by its title. If it is on the library booklist, it shows its data.
    def search_book(self, book_title: str):
        for book in self._book_list:
            if book.title.upper() == book_title.strip().upper():
                print(f'Book found...\nInfo:\nName: {book.title}\nPublication Year: {book.year}\nCopies: {book.copies}')
                return

        print('Was not possible to locate this book...')

    # Takes a copie of a book from the library and adds it to the user booklist
    def borrow_book(self, user: User, book_title: str):      
        for book in self._book_list:
            if book.title.upper() == book_title.strip().upper():
                if not book.available:
                    print(f'Any copies of {book.title} available...')
                    return

                user._book_list.append(book)
                book.copies -= 1
                print(f'1 copy of {book.title} borrowed with succes...')
                return

    # Returns a book from the user Booklist to the library
    def return_book(self, user: User, book_title: str, book_itself=None):
        if isinstance(book_itself, Book):
            for book in user._book_list:
                if book == book_itself:
                    user._book_list.remove(book)
                    book.copies += 1
                    print(f'{book.title} returned with succes...')
                    return

        for book in user._book_list:
            if book.title.upper() == book_title.strip().upper():
                user._book_list.remove(book)
                book.copies += 1
                print(f'{book.title} returned with succes...')
                return

        print('Was not possible to locate the book on the users list...')

    # Prints all the books information
    def list_books(self):
        print('-'*6)
        print('Info:')
        print('--'*40)
        for book in self._book_list:
            print(f'Name: {book.title:<25}Publication Year: {book.year:<20}Copies: {book.copies}\n')


# Just for testing purpose
if __name__ == '__main__': #Usage example on python console
    b1 = Library()

    user = User('Ryan', 1342)

    the_little_prince = Book('The Little Prince', 1943, 1)
    romeo_and_juliet = Book('Romeo and Juliet', 1597, 2)
    abc_for_kids = Book('ABC for kids', 2022, 5)
    lotr1 = Book('Lord of the rings 1', 1954, 1)


    b1.add_book_(the_little_prince, romeo_and_juliet, abc_for_kids, lotr1)
    b1.search_book('Pequen')
    b1.list_books()

    b1.borrow_book(user, 'Lord of the rings 1')

    b1.list_books()

    print(lotr1.available)

    b1.return_book(user, '', lotr1)

    b1.list_books()

    print(lotr1.available)

    b1.list_books()

    print(lotr1)
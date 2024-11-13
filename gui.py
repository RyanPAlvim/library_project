import ttkbootstrap as ttk
import ttkbootstrap.constants as ttkc
from tkinter import messagebox
from library import Book, Library


def add_book():
    # Get inputs from entry fields
    title = entry_title.get()
    year = entry_year.get()
    copies = entry_copies.get()

    # Validate input data
    if title and year.isdigit() and copies.isdigit():
        # Create a new book object and add it to the library
        book = Book(title, int(year), int(copies))
        library.add_book_(book)

        # Clear entry fields after adding
        entry_title.delete(0, ttk.END)
        entry_year.delete(0, ttk.END)
        entry_copies.delete(0, ttk.END)

        # Update the book list in the UI
        update_book_list()
    else:
        label_status.config(text="Please enter valid data!", padding=5)
        label_status.after(3000, clear_status)  # Clear status after 3 seconds


def update_book_list():
    # Clear the existing book list in the Treeview
    for item in book_list.get_children():
        book_list.delete(item)

    # Add books from library to the Treeview
    for book in library._book_list:
        book_list.insert('', 'end', text='', values=(book.title, book.year, book.copies))


def remove_book(): 
    # Remove a book by title from the list and the Treeview
    title = entry_remove.get()
    for book in library._book_list[:]:
        if title == book.title:
            confirm = messagebox.askyesno(f'Removing {book.title}. Are you sure?')
            if confirm:
                library._book_list.remove(book)  # Remove the book
    entry_remove.delete(0, ttk.END)
    update_book_list()  # Update the UI


def clear_list(): 
    # Clear all books from the library
    if library._book_list == []:
        return
    confirm = messagebox.askyesno('Are you sure you want to clear the list? All data will be deleted!')
    if confirm:
        library._book_list.clear()  # Clear all books
        update_book_list()  # Update the UI


def clear_status():
    # Clear the status message after a few seconds
    label_status.config(text='', padding=0)


def focus_next_widget(event):
    # Focus on the next widget when Enter is pressed
    event.widget.tk_focusNext().focus()
    return 'break'


def create_window():
    global entry_title, entry_year, entry_copies, book_list, label_status, entry_remove

    # Create the main window with a dark theme
    window = ttk.Window(themename="darkly")  
    window.title("Library System")
    window.geometry("800x800")

    # Book title label and entry field
    label_title = ttk.Label(window, text="Book Title:", style=ttkc.INFO)
    label_title.pack(pady=5)
    entry_title = ttk.Entry(window, font=("Helvetica", 12))
    entry_title.pack(pady=5)
    entry_title.bind('<Return>', focus_next_widget)  # Bind Enter key to move focus

    # Publication year label and entry field
    label_year = ttk.Label(window, text="Publication Year:", style="info")
    label_year.pack(pady=5)
    entry_year = ttk.Entry(window, font=("Helvetica", 12))
    entry_year.pack(pady=5)
    entry_year.bind('<Return>', focus_next_widget)

    # Number of copies label and entry field
    label_copies = ttk.Label(window, text="Number of Copies:", style="info")
    label_copies.pack(pady=5)
    entry_copies = ttk.Entry(window, font=("Helvetica", 12))
    entry_copies.pack(pady=5)
    entry_copies.bind('<Return>', focus_next_widget)

    # Button to add a book
    add_button = ttk.Button(window, text="Add Book", command=add_book, style="success-outline", width=20)
    add_button.pack(pady=20)

    # Label and entry field for removing a book
    label_remove = ttk.Label(window, text='Remove Book Title:', style="info")
    label_remove.pack(pady=5)
    entry_remove = ttk.Entry(window, font=("Helvetica", 12))
    entry_remove.pack(pady=5)
    entry_remove.bind('<Return>', focus_next_widget)

    # Button to remove a book
    remove_button = ttk.Button(window, text='Remove Book', command=remove_book, style="danger-outline", width=20)
    remove_button.pack(pady=20)

    # Treeview to display the list of books
    columns = ('Title', 'Year', 'Copies')
    book_list = ttk.Treeview(window, columns=columns, show='headings')  # Treeview for books
    book_list.pack(pady=(10, 0))

    # Configure column headings
    book_list.heading('Title', text='Book Title')
    book_list.heading('Year', text='Publication Year')
    book_list.heading('Copies', text='Number of Copies')

    # Set column widths
    book_list.column('Title', anchor='center', width=200)
    book_list.column('Year', anchor='center', width=100)
    book_list.column('Copies', anchor='center', width=150)

    # Status label for showing messages (success or error)
    label_status = ttk.Label(window, text="", style="info")
    label_status.pack(pady=0)

    # Button to clear the entire list
    clear_button = ttk.Button(window, text='Clear List', command=clear_list, style="warning-outline", width=20)
    clear_button.pack(pady=5)

    window.mainloop()


library = Library()  # Initialize the library object

create_window()  # Run the function to create the window

print(library)  # Print the library object to console (for debugging)

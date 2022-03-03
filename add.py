import tel_book

def add_contact(book, name, number):
    book[name] = number
    tel_book.set_data(book)

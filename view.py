import tel_book
def data():
    # path = 'book.txt'
    # book = open(path, 'r')
    # for i in book:
    #     print(i)
    # book.close()
    book = tel_book.get_data()
    print(book)
    operation = input('Исползуйте операцию добавления контакта +, либо удаления -')
    name = input('Введите имя контакта')
    number_phone = input('Введите номер телефона')
    return operation, name, number_phone
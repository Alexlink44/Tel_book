book = {'Вы запустили' : 'Телефонная книга'}
import add
def get_data():
    global book
    return book

def set_data(new_data):
    global book
    book = new_data
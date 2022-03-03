import view
import add
import tel_book
def button_click():
    operation = view.data()
    if operation[0] == '+':
        add.add_contact(tel_book.get_data(), operation[1], operation[2])
    # elif operation[0] == '-':
    button_click()



button_click()
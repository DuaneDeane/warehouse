from os import system, name
from time import sleep
import datetime

def print_menu():
    print("-" * 50)
    print("Welcome to Warehouse [" + get_date_time() + "]")
    print("-" * 50)

    print('[1] - Add product to Catalog')
    print('[2] - Display catalog')
    print('[3] - Display products out of stock')
    print('[4] - Total stock Value')
    print('[5] - Cheapest Product')
    print('[6] - Delete Product')
    print('[7] - Update Product Price')
    print('[8] - Update Product Stock')
    print('[10] - 3 Most expensive products')
    print('[11] - Distinct categories')

    print('[s] - Save')
    print('[x] - Exit')

def get_date_time():
    now = datetime.datetime.now()
    return now.strftime("%x %X")

def print_header(text):
    clear()
    print('-' * 76)
    print(text)
    print('-' * 76)

def print_product_info(prod):
    print("| " + str(prod.id).rjust(3) + " | " + prod.title.ljust(25) + " | " + prod.category.ljust(12) + " | " + str(prod.stock).rjust(7) + " |  $" + str(prod.price).rjust(12) + " |")

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


print('\n'*10)
sleep(2)
clear()
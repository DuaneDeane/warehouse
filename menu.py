from os import system, name
from time import sleep

def print_menu():
    print("-" * 50)
    print("Welcome to Warehouse")
    print("-" * 50)

    print('[1] - Add product to Catalog')
    print('[2] - Display catalog')
    print('[3] - Display products out of stock')
    print('[4] - Total stock Value')
    print('[5] - Cheapest Product')
    print('[6] - Delete Product')
    print('[7] - Update Product Price')
    print('[8] - Update Product Stock')

    print('[s] - Save')
    print('[x] - Exit')

def print_header(text):
    clear()
    print('-' * 50)
    print(text)
    print('-' * 50)

def print_product_info(prod):
    print(str(prod.id) + "  " + prod.title + "  " + prod.category + "  " + str(prod.stock) + "  " + str(prod.price))

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


print('\n'*10)
sleep(2)
clear()
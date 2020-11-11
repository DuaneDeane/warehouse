"""
Program: Warehouse Control
Author: Duane Deane
Date: Nov. 2020
Functionality:
    - Register Products
        - id (auto generated)
        - title
        - category
        - stock
        - price
        
"""

# imports
from menu import clear, print_menu, print_header, print_product_info
from product import Product
import pickle

# global
catalog = []
next_id = 1

# functions


def serialize_data():
    try:
        writer = open('warehouse.data', 'wb')
        pickle.dump(catalog, writer)
        writer.close()
        print("** Data serialized!")
    except:
        print("** Error, data not saved.")


def deserialize_data():
    global next_id
    try:
        reader = open('warehouse.data', 'rb')
        temp_list = pickle.load(reader)
        reader.close()

        for prod in temp_list:
            catalog.append(prod)

        last = catalog[-1]
        next_id = last.id + 1

        how_many = len(catalog)
        print("** Read: " + str(how_many) + " products")

    except:
        print("** Error, no data file found")


def register_product():
    try:
        global next_id
        print_header("Register new Product")
        title = input('Please provide the title: ')
        category = input('Please provide the Category: ')
        stock = int(input('Please provide the initial stock: '))
        price = float(input('Please provide the price: '))

        if(len(title) < 1):
            print("Error: title should not be empty")

        product = Product(next_id, title, category, stock, price)
        next_id += 1
        catalog.append(product)

    except:
        print("** Error, review registration of product")


def delete_product():
    print_header("Deleted product")
    display_catalog()
    id = int(input("ID of item to delete: "))
    found = False
    for prod in catalog:
        if(prod.id == id):
            found = True
            catalog.remove(prod)
            print("** Item removed!")
    if(not found):
        print("** Incorrect ID, try again")


def display_catalog():
    print_header("Current Catalog")
    for prod in catalog:
        print_product_info(prod)


def display_no_stock():
    print_header("Out of stock")
    for prod in catalog:
        if(prod.stock == 0):
            print_product_info(prod)


def display_total_stock_price():
    print_header("Total stock price")
    total = 0
    for prod in catalog:
        total += (prod.price * prod.stock)
    print("Total stock value: $" + str(total))


def display_cheapest_product():
    print_header("Cheapest Price Product")

    cheapest = catalog[0]
    for prod in catalog:
        if(prod.price < cheapest.price):
            cheapest = prod
    print("Cheapest product is: ")
    print_product_info(cheapest)


def update_product_price():
    print_header("Update Price")
    display_catalog()
    id = int(input("Enter ID of item to update: "))
    found = False
    for prod in catalog:
        if(prod.id == id):
            prod.price = float(input("Enter new price: "))
            found = True
            #catalog.price(prod)
            print("** Price updated!")
    if(not found):
        print("** Incorrect ID, try again")


def update_product_stock():
    print_header("Update Stock")
    display_catalog()
    id = int(input("Enter ID of item to update: "))
    found = False
    for prod in catalog:
        if(prod.id == id):
            prod.stock = float(input("Enter new stock: "))
            found = True
            #catalog.stock(prod)
            print("** Stock updated!")
    if(not found):
        print("** Incorrect ID, try again")

    # instructions


deserialize_data()
input("Press Enter to continue...")

opc = ''
while(opc != 'x'):
    clear()
    print_menu()
    opc = input('Please select an option: ')

    if(opc == '1'):
        register_product()
        serialize_data()
    elif(opc == '2'):
        display_catalog()
    elif(opc == '3'):
        display_no_stock()
    elif(opc == '4'):
        display_total_stock_price()
    elif(opc == '5'):
        display_cheapest_product()
    elif(opc == '6'):
        delete_product()
        serialize_data()
    elif(opc == '7'):
        update_product_price()
        serialize_data()
    elif(opc == '8'):
        update_product_stock()
        serialize_data()
    elif(opc == 's'):
        serialize_data()

    input('Press Enter to continue...')

print('Good Byte')

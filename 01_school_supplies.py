#Turn code completion off when starting this assignment
# Do not use theany generative AI tool (built in orotherwise) to 
# complete this assignment

def load_catalog():
    catalog = {
        101: {"name": "Notebook", "category": "Paper", "price": 3.99},
        102: {"name": "Pen", "category": "Writing", "price": 1.50},
        103: {"name": "Pencil", "category": "Writing", "price": 0.75},
        104: {"name": "Eraser", "category": "Correction", "price": 0.99},
        105: {"name": "Sharpener", "category": "Accessories", "price": 1.25},
        106: {"name": "Ruler", "category": "Measuring", "price": 2.50},
        107: {"name": "Glue Stick", "category": "Adhesive", "price": 1.99},
        108: {"name": "Scissors", "category": "Cutting", "price": 4.99},
        109: {"name": "Highlighter", "category": "Writing", "price": 2.75},
        110: {"name": "Marker", "category": "Writing", "price": 3.49},
        111: {"name": "Stapler", "category": "Office Supplies", "price": 5.99},
        112: {"name": "Staples", "category": "Office Supplies", "price": 1.50},
        113: {"name": "Paper Clips", "category": "Office Supplies", "price": 2.00},
        114: {"name": "Binder", "category": "Organizing", "price": 6.50},
        115: {"name": "Sticky Notes", "category": "Paper", "price": 3.25},
        116: {"name": "Index Cards", "category": "Paper", "price": 2.99},
        117: {"name": "Whiteboard Marker", "category": "Writing", "price": 3.75},
        118: {"name": "File Folder", "category": "Organizing", "price": 4.50},
        119: {"name": "Calculator", "category": "Electronics", "price": 12.99},
        120: {"name": "Tape Dispenser", "category": "Adhesive", "price": 5.49}
    }
    return catalog

# Task 1
# Write a function named get_items and pass the catalog as the argument.
# The will prompt the user for  five item numbers and their  quantities
# and add them to a list.  As the user adds items and quantities to the list
# compute the extended price add it as another entry to the item's dictionary.
# If the user inputs a non-existing item number, it should raise an error
# when that error is raised, display a not-so-polite message and allow the user to continue
# Handle exceptions from negative or non-integer user inputs 

# return the list
def get_items(catalog):
    items = []
    for _ in range(3):
        new_item = {}
        while True:
            try:
                item_number = int(input("Enter item number [101 to 120]: "))
                selected_item = catalog[item_number]
            except KeyError:
                print('Invalid item number. Please try again')
            else:
                break
        new_item['item_number'] = item_number
        new_item['name'] = selected_item['name']
        new_item['category'] = selected_item['category']
        new_item['quantity'] = int(input(f"Enter quantity of {selected_item['name']}: "))
        new_item['price']= selected_item['price']
        new_item['extended_price'] = new_item['quantity']* new_item['price']
        items.append(new_item)
    return items


# Commit your code.  Write your commit message here....
# 

# Task 2
# Suppose thers is a buy-one-get-one free deal on paper category items.
# Write a function named bogo_deal.  The inputs are items, and catalog
# The returned list will be the item, and a new key value pair to each item 
#  that will hold the discount, and discounted amount
def bogo_deal(items, catalog, bogo_categories):
        # Write your code here
        for bogo_category in bogo_categories:
            for selected_item in items:
                print(selected_item)
                if selected_item['category'] == bogo_category:
                    if selected_item['quantity'] >= 2:
                        free_items = selected_item['quantity']//2
                        selected_item['discount'] = free_items * selected_item['price']
                        selected_item['discounted_amount'] = selected_item['price'] * (selected_item['quantity']-free_items)
                    else:
                        selected_item['discount'] = 0
                        selected_item['discounted_amount'] = selected_item['extended_price']
                else:
                    selected_item['discount'] = 0
                    selected_item['discounted_amount'] = selected_item['extended_price']
        return items

# Commit your code.  Write your commit message here....
# 

# Task 3
# Some shoppers use coupons to get discount
# one some items that are on sale
# The discount can be price discount like 50 cents off or 
# percentage discount like 20% off
# Write a function named coupon_sale that takes items, catalog and coupons
# as input, and updates the discounted price.
def coupon_sale(items, catalog, coupons):
    # write your code here
    for selected_item in items:
        slected_item_number = selected_item['item_number']
        if coupons[slected_item_number]:
            if coupons[slected_item_number]['discount'] == 'price':
                



    return items

# Commit your code.  Write your commit message here....
# 

# Task 3
# Print the updated item entries.  For each item, 
# print the item number, category, name, original price, and discounted price
# Print the number of items purchased, and total bill amount, total discount
# and total after discount
# Use the f formatter to align the data so that it appears clean
def print_bill(items):
    # Write your code here
    return "Done"
# Commit your code.  Write your commit message here....
# 

# Task 4
# Use the main block below
# add code for exception handling
# Exceptions can rise due to 

def main():
    catalog = load_catalog()
    items = get_items(catalog)
    print(items)
    bogo_categories = ['Paper']
    items = bogo_deal(items, catalog, bogo_categories)
    print(items)
    coupons = {108: {"discount":"price", "amount":0.50},
               110: {"discount":"percent", "amount":0.25}}
    items = coupon_sale(items, catalog, coupons)
    print_bill(items)

# Commit your code.  Write your commit message here....
# 

main()







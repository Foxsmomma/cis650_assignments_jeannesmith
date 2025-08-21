#Create a script that will
# prompt the user for number of items,
# then ask for item name, and item price for each item
# Then it will print the items, prices, number of items, and total price
# Make the output easy to read on the terminal.
# Do not use any data structures or any package for display

def numItems = input ("Please enter the number of items:")
itemPrint = ""
totalPrice = 0

for num in range(1, NumItems + 1):
    itemName = input("Please enter the name of item:")
    itemPrice = input("Please enter the item price")
    itemPrint = itemPrint + "Item: " + itemName + " Price: " + itemPrice + "\n"
    totalPrice += itemPrice

print itemPrint + "\nNumber of items: " + numItems + "\nTotal Price: " + totalPrice


#git commit -m 'updated 05_grocery_bill' and then
#git push

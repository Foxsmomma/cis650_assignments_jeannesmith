#Consider this data about icecreams and their popularity
ice_cream_popularity = [
    {"flavor": "Vanilla", "popularity": 59},
    {"flavor": "Chocolate", "popularity": 51},
    {"flavor": "Strawberry", "popularity": 43},
    {"flavor": "Cookies and Cream", "popularity": 43},
    {"flavor": "Butter Pecan", "popularity": 42},
    {"flavor": "Chocolate Chip Cookie Dough", "popularity": 44},  
    {"flavor": "Caramel", "popularity": 41},  
    {"flavor": "Coffee", "popularity": 32},
    {"flavor": "Peanut Butter", "popularity": 29}
]
# Write a script that shows a numbered list of the flavors, and asks the 
# user for their preference.  The script will then print "You are among xx percentage
# of people who like that yy flavor" .
# After completing this script, git commit with 'after_05_icecream' as the message 
# and git push the repo 

print("Flavor List:")
for i, flavor in enumerate(ice_cream_popularity):
    print(f"{i+1}.{flavor['flavor']}({flavor['popularity']}%)")
while True:
    try:
        uchoice= int(input("What number is your preference?"))
        if 1 <= uchoice <= len(ice_cream_popularity):
            break
    except ValueError: print("Not Found")
    

chosenflavor = ice_cream_popularity[uchoice-1]
icecream = chosenflavor ['flavor']
popularity = chosenflavor["popularity"]
print(f"Congrats! You are amoung the {popularity} % that love", (icecream))


import requests
from bs4 import BeautifulSoup
url = 'https://cataas.com/'
page = requests.get(url)
print(page)
soup = BeautifulSoup(page.content, 'html.parser')
links = soup.find_all('a')
for link in links:
  print(link)


soup.find_all('span')[0]
# display the title of page
#print(soup.title.text.strip())
for link in soup.find_all('a'):
  #print(link['href'])
  print(link.string, link['href'])
  #print(link.get('href'))
  

def list_cataas_variables():
    print("Cataas Query Variables:")
    print("- `/cat`: Returns a random cat image.")
    print("- `/cat/says/:text`: Adds text to a cat image. Replace `:text` with your desired text.")
    print("  Example: `/cat/says/Hello%20World`")
    print("- `/cat?filter=custom&r=:red&g=:green&b=:blue`: Filters a cat image by RGB values.")
    print("  Example: `/cat?filter=custom&r=255&g=0&b=0` (Red filter)")
    print("- `/cat?width=:width` or `/cat?height=:height`: Returns a random cat with specified width or height.")
    print("  Example: `/cat?width=300` or `/cat?height=200`")
    print("- `/cat?html=true`: Returns a random cat in an HTML page.")
    print("- `/cat?json=true`: Returns a random cat in a JSON object.")

def catpics(query_type,cat_input=None):
  cataasurl: "https://cataas.com/cat"
if query_type=="random":
  url=cataasurl
elif query_type=="gif":
   url=f"{cataasurl}/gif"
elif query_type=="tag":
   url=f"{cataasurl}/tag"
elif query_type=="says":
   url=f"{cataasurl}/says"
else:
   print("Invalid. Please try again")
   
def menu():
    cat_options = {
       "a": "random",
       "b":"gif",
       "c": "tag",
       "d":"says"
    }

while True:
   print("\nOptions:")
   print("a. random")
   print("b. gif")
   print("c. tag")
   print("d. says")
   print("e. Exit")

cat_input=input('Please enter a query')
if cat_input == "e":
   break
query_type= cat_options.get(cat_input)
if query_type:
   cat_input=None
if query_type=="tag":
      cat_input=input("What tag?")
elif query_type=="says":
      cat_input=input("What do you want to say?")
      get_cat_image(query_type,cat_input)
else:
    print("Please try again")


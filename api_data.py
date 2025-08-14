

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
  



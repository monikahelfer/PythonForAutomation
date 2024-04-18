from bs4 import BeautifulSoup
import requests

url = 'https://scrapingclub.com/exercise/list_basic/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
count = 1
items = soup.find_all('div', class_='w-full rounded border')
for i in items:
    # Strip removes white spaces, in this example it removes returns
    itemName = i.find('h4').text.strip('\n')
    itemPrice = i.find('h5').text
    # %s means a string that should be put inside other string in the print function, we can use it in quotes (' or ") and
    # after the closing quote we need to put % with the values that we want to put
    print('%s) Item Name: %s, Price: %s' % (count, itemName, itemPrice))
    # We add count only to list and count the items in an ordered list
    count = count + 1


pages = soup.find('nav', class_='pagination')
urls = []
links = pages.find_all('a')
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        x = link.get('href')
        urls.append(x)

for i in urls:
    newUrl = url + i
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='w-full rounded border')
    for i in items:
        # Strip removes white spaces, in this example it removes returns
        itemName = i.find('h4').text.strip('\n')
        itemPrice = i.find('h5').text
        # %s means a string that should be put inside other string in the print function, we can use it in quotes (' or ") and
        # after the closing quote we need to put % with the values that we want to put
        print('%s) Item Name: %s, Price: %s' % (count, itemName, itemPrice))
        # We add count only to list and count the items in an ordered list
        count = count + 1
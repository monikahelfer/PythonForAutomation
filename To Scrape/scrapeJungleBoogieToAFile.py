from bs4 import BeautifulSoup
import requests

f = open('./JungleBoogieScraped.txt', 'w')

url = 'https://www.jungleboogie.pl/kategoria-produktu/rosliny/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
count = 1
items = soup.find_all('div', class_='woocommerce-card__header')
for i in items:
    itemName = i.find('a', class_='woocommerce-LoopProduct-link').text.strip('\n')
    itemPrice = i.find('bdi').text
    f.write('%s) Plant name: %s, Price: %s\n' % (count, itemName, itemPrice))
    count = count + 1

pages = soup.find('ul', class_='page-numbers')
urls = []
links = pages.find_all('a', class_='page-numbers')
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        x = link.get('href')
        urls.append(x)

for i in urls:
    newUrl = url + i
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='woocommerce-card__header')
    for i in items:
        itemName = i.find('a', class_='woocommerce-LoopProduct-link').text.strip('\n')
        itemPrice = i.find('bdi').text
        f.write('%s) Plant name: %s, Price: %s\n' % (count, itemName, itemPrice))
        count = count + 1

f.close()
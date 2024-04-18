# Web scraping means taking data from web pages to process them
# At the beginning, we need to install requests, lxml, and beautifulsoup4 in the terminal

import requests # A module that allows sending HTTP requests using Python
from bs4 import BeautifulSoup # A Python library for pulling data out of HTML and XML files

# Webpage to scrape
url = 'https://quotes.toscrape.com/'

# Get the source code (HTML) of the website
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, 'lxml') # We want to use the lxml parser
quotes = soup.find_all('span', class_='text') # We want oto find in our HTML soup all spans with the text class because they contain quotes
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

# We add a loop to iterate and get the text and author of each quote
for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a', class_='tag') # There are several tags for each quote, for each div we want to find all a tags
    for quoteTag in quoteTags:
        print(quoteTag.text) # We use a loop to access the text of  each tag

# A loop for printing each quote (we use a loop because we want to print the text of each quote, we can't do it for all quotes)
#for quote in quotes:
#    print(quote.text) # Text lets us generate only the text inside the tags, without spans or any other HTML elements
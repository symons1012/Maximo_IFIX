"""Web scraping code example using Python Requests and Beautiful Soup

After importing requests and BeautifulSoup, the following code shows how to download
and scrape HTML of the Treehouse blog's home page, extract all URL links and print them
out to the console. """

import requests
from bs4 import BeautifulSoup

response = requests.get('http://blog.teamtreehouse.com')
soup = BeautifulSoup(response.text)

for link in soup.find_all('a'):
    print(link.get('href'))

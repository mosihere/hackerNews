import requests
from bs4 import BeautifulSoup
import re

# Send request to fetch data
response = requests.get('https://hckrnews.com/')

# Parse Needed Data with BS !
soup = BeautifulSoup(response.text, 'html.parser')

# Select a special tag that we need --> and use attributes to find that exactly
data = soup('a', attrs={'class':'link'})

# Print Data in a file
f = open('news.txt', 'w+')
counter = 0
for title in data:
    counter += 1
    print('%i:'%counter,title.text,title.get('href')) # title.get('href) will show the links
    print()                                           # title.text is just the text
from bs4 import BeautifulSoup
import requests

website = requests.get('https://oucc.dasa.ncsu.edu/coe-14cscbs-nosubplan-2177/').text

soup = BeautifulSoup(website, 'lxml')

article = soup.find('article')

entry_content = article.find('div', class_='entry-content')

#years = entry_content.h3.text
for table in entry_content.find_all('table'):
    classes = table.tbody
    print(classes.text)

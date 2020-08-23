from bs4 import BeautifulSoup
import requests
import csv

website = requests.get('https://oucc.dasa.ncsu.edu/coe-14cscbs-nosubplan-2177/').text

soup = BeautifulSoup(website, 'lxml')

article = soup.find('article')

entry_content = article.find('div', class_='entry-content')

#csv_file = open('ncsu_courses_scrape.csv','w')
#csv_writer =csv.writer(csv_file)
#csv_writer.writerow(['classes'])

file=  open("ncsu_courses_scrape.txt", 'w')
  
for table in entry_content.find_all('table', class_='table table-striped'):
    table_row = table.tbody.find_all('tr')
    for row in table_row:
        for x in row:
            try:
                #print(x.text)
                file.write(row.text)
            except:
                pass
        
file.close()
    
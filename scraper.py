"""  
By: Yaasir M.B
Date: 8/23/2020
This script scrapes North Carolina State University's website for the course requirements for their Computer Science (BS) degree.

"""

from bs4 import BeautifulSoup
import requests
import csv

# link to the website you want to scrape.
website = requests.get('https://oucc.dasa.ncsu.edu/coe-14cscbs-nosubplan-2177/').text
soup = BeautifulSoup(website, 'lxml')

# find the first article element in the website's html.
article = soup.find('article')
# find the div tag with the entry-content class.
entry_content = article.find('div', class_='entry-content')
  
# list that gets populated with all required courses and credits for those courses.
lines = []

# find all tables in the entry-content class.
for table in entry_content.find_all('table', class_='table table-striped'):
    # find all table rows in each table.
    table_row = table.tbody.find_all('tr')

    # iterate over each row (<tr>) in each table.
    for row in table_row:
        # iterate over each table data tag (<td>) in every table row. This includes both the courses and their credits. 
        for course in row:
            try:
                # I'm adding the '.text' at the end to get rid of the html tags.
                lines.append(course.text)
            except:
                pass


file =  open("ncsu_courses_scrape.txt", 'w')

for line in lines:
    file.write(line)
    file.write('\n')

file.close()

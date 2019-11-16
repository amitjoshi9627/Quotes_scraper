from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://quotes.toscrape.com/').text
soup = BeautifulSoup(source, 'lxml')

for i in soup.find_all('span', class_='tag-item'):

    tag_link = 'http://quotes.toscrape.com/' + i.a['href']
    tag_source = requests.get(tag_link).text
    tag_soup = BeautifulSoup(tag_source, 'lxml')

    file_name = tag_soup.h3.a.text+'.csv'
    csv_file = open('./Quotes/'+file_name, 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Quote', 'Author'])

    print("Tag:", i.a.text)
    print()

    for obj in tag_soup.find_all('div', class_='quote'):
        quote = obj.span.text
        author = obj.small.text
        # print(quote)   #To print quote
        # print(author)  #To print author's name
        print()
        csv_writer.writerow([quote, author])
    print()
    print()

    csv_file.close()

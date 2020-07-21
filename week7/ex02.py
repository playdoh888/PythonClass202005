import requests
import csv
from bs4 import BeautifulSoup


f = csv.writer(open('b-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

pages = []

for i in range(1, 52):
    url = 'https://web.archive.org/web/20121002115827/http://www.nga.gov/collection/anB' + str(i) + '.htm'
    pages.append(url)


i = 0
for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    artist_name_list = soup.find(class_='BodyText')
    artist_name_list_items = artist_name_list.find_all('a')

    print(f"Parsing: {item}")
    for artist_name in artist_name_list_items:
        if artist_name.contents:
            names = artist_name.contents[0]
            links = 'https://web.archive.org' + artist_name.get('href')
            f.writerow([names, links])

    i += 1

import requests
import json
from bs4 import BeautifulSoup

# Send an HTTP request to the website and store the response
response = requests.get('https://books.toscrape.com/')

# Parse the HTML of the website with UTF-8 encoding
soup = BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')

# Find all the elements with class "product_pod"
books = soup.find_all('article', class_='product_pod')

# Open a JSONL file for writing
with open('books.jsonl', 'w', encoding='utf-8') as jsonlfile:
    # Write the data for each book
    for book in books:
        title = book.h3.a['title'].strip()
        price = book.find('p', class_='price_color').text.strip()
        rating = book.p['class'][1].strip()
        availability = book.find('p', class_='instock availability').text.strip()
        link = book.h3.a['href'].strip()
        data = {
            'title': title,
            'price': price,
            'rating': rating,
            'availability': availability,
            'link': link
        }
        json.dump(data, jsonlfile, ensure_ascii=False)
        jsonlfile.write('\n')

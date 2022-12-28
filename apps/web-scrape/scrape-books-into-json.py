import requests
import json
from bs4 import BeautifulSoup

# Send an HTTP request to the website and store the response
response = requests.get('https://books.toscrape.com/')

# Parse the HTML of the website with UTF-8 encoding
soup = BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')

# Find all the elements with class "product_pod"
books = soup.find_all('article', class_='product_pod')

# Create a list of dictionaries containing the data for each book
data = []
for book in books:
    title = book.h3.a['title'].strip()
    price = book.find('p', class_='price_color').text.strip()
    rating = book.p['class'][1].strip()
    availability = book.find('p', class_='instock availability').text.strip()
    link = book.h3.a['href'].strip()
    data.append({
        'title': title,
        'price': price,
        'rating': rating,
        'availability': availability,
        'link': link
    })

# Open a JSON file for writing
with open('books.json', 'w', encoding='utf-8') as jsonfile:
    # Write the data to the file
    json.dump(data, jsonfile, ensure_ascii=False)

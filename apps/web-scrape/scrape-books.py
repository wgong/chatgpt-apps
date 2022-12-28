import csv
import requests
from bs4 import BeautifulSoup

# Send an HTTP request to the website and store the response
response = requests.get('https://books.toscrape.com/')

# Parse the HTML of the website
# soup = BeautifulSoup(response.text, 'html.parser')
soup = BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')

# Find all the elements with class "product_pod"
# books = soup.find_all('div', class_='product_pod')

# class=product_pod on article element not div

# fixed by the following prompt
# can you fix an error: 'product_pod' class element is not 'div', it should be 'article'
books = soup.find_all('article', class_='product_pod')

# Open a CSV file for writing
with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer
    writer = csv.writer(csvfile)

    # Write the headers
    writer.writerow(['Title', 'Price', 'Rating', 'Availability', 'Link'])

    # Print the information for each book
    for book in books:
        # title = book.h3.a['title']
        # price = book.find('p', class_='price_color').text
        # rating = book.p['class'][1]
        # availability = book.find('p', class_='instock availability').text
        # link = book.h3.a['href']

        # print(f'Title: {title}')
        # print(f'Price: {price}')
        # print(f'Rating: {rating}')
        # print(f'Availability: {availability}')
        # print(f'Link: {link}')
        # print()
        
        # ask to strip column
        title = book.h3.a['title'].strip()
        price = book.find('p', class_='price_color').text.strip()
        rating = book.p['class'][1].strip()
        availability = book.find('p', class_='instock availability').text.strip()
        link = book.h3.a['href'].strip()        

        writer.writerows([[title, price, rating, availability, link]])
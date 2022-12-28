## Prompts

### Initial prompt:
- web scrape  https://books.toscrape.com/ using python and beautifulsoup


```
pip3 install beautifulsoup4
```

### Prompt to fix an error:
- can you fix an error: 'product_pod' class element is not 'div', it should be 'article'

```
$ python3.8 scrape-books.py   # create CSV

$ python3.8 scrape-books-into-json.py   # save as JSON

```

### save books using JSONL format

- what is the difference between json and jsonl format
- can you save book data using jsonl format?

```
$ python3.8 scrape-books-into-jsonl.py   # save as JSON

```
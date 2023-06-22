from bs4 import BeautifulSoup
import requests
import database
from datetime import datetime


URL = 'https://www.ebay.de/str/amaxshopde?_ipg=72&_pgn='

def scrape():
    print(f'Scraping {URL}...')
    start = datetime.now()
    print('Reading total pages...')

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    pages = int(soup.select('.pagination__items > li:nth-child(4) > a:nth-child(1)')[0].text)

    products = []

    print('Crawling pages...')
    for i in range(pages):
        product_page = requests.get(URL + str(i))
        product_soup = BeautifulSoup(product_page.content, 'html.parser')

        products_raw = product_soup.select('.str-items-grid__container')[0].find_all('article')

        print(len(products_raw))

        for product in range(len(products_raw)):
            url = product_soup.select(f'article.str-item-card:nth-child({product + 1}) > a:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(2) > a:nth-child(1)')[0].get('href')
            title = product_soup.select(f'article.str-item-card:nth-child({product + 1}) > a:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(2) > a:nth-child(1) > span:nth-child(2)')[0].text
            image = product_soup.select(f'article.str-item-card:nth-child({product + 1}) > a:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > picture:nth-child(1) > img:nth-child(2)')[0]['src']
            price = float(product_soup.select(f'article.str-item-card:nth-child({product + 1}) > div:nth-child(3) > span:nth-child(1)')[0].text.replace(',', '.').replace('€', '').replace('EUR', '').replace(' ', ''))

            products.append((url, title, image, price))

        print('Page ' + str(i + 1) + ' of ' + str(pages) + ' crawled.')

    products = list(set(products))
    database.set_table('amax', products)

    print(f'Crawled {URL} in {datetime.now() - start}!')
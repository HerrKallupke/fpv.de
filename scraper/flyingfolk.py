from bs4 import BeautifulSoup
import requests
import database
from datetime import datetime


URL = 'https://flyingfolk.com/shop/?orderby=popularity'

def scrape():
    print(f'Scraping {URL}...')
    start = datetime.now()
    print('Reading total pages...')

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    pages = int(soup.select('.page-numbers > li:nth-child(8) > a:nth-child(1)')[0].text)

    products = []

    print('Crawling pages...')
    for i in range(pages):
        product_page = requests.get(URL + '&paged=' + str(i + 1))
        product_soup = BeautifulSoup(product_page.content, 'html.parser')

        products_raw = product_soup.select('.products')[0].find_all(class_='product-small')

        for product in products_raw:
            url = product.select('div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > p:nth-child(2) > a:nth-child(1)')[0].get('href')
            title = product.select('div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > p:nth-child(2) > a:nth-child(1)')[0].text
            image = product.find_all('img')[0]['src']
            price = float(product.find_all('bdi')[0].text.replace(',', '.').replace('€', ''))

            products.append((url, title, image, price))

        print('Page ' + str(i + 1) + ' of ' + str(pages) + ' crawled.')

    products = list(set(products))
    database.set_table('flyingfolk', products)

    print(f'Crawled {URL} in {datetime.now() - start}!')
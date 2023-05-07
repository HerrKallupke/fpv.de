from autoscraper import AutoScraper


example_url = 'https://flyingfolk.com/?s=foxeer&post_type=product'
wanted_links = [ 'https://flyingfolk.com/produkt/foxeer-predator-micro-v2-1000-tvl-cam-fpv-drone-cmos-blue/' ]
link_scraper = AutoScraper()
link_scraper.build(example_url, wanted_list=wanted_links)

example_url = 'https://flyingfolk.com/produkt/foxeer-predator-micro-v2-1000-tvl-cam-fpv-drone-cmos-blue/'
wanted_image_title_price = [ 'https://flyingfolk.com/wp-content/uploads/2020/09/Foxeer-Predator-Micro-V2-1-blue-700x458.jpg', 'Foxeer Predator Micro V2 FPV Kamera – 1.8mm – 1000TVL – CMOS – blau', '€43,87' ]
product_info_scraper = AutoScraper()
product_info_scraper.build(example_url, wanted_list=wanted_image_title_price)

def get_offer(query):
    url = f'https://flyingfolk.com/?s={query}&post_type=product'
    links = link_scraper.get_result_exact(url)

    if links == []:
        return None

    image = ''
    title = ''
    price = ''
    for data in product_info_scraper.get_result_exact(links[0]):
        if str(data).startswith('http'):
            if image == '':
                image = data
                continue
        elif '€' in data:
            if price == '':
                price = data
        else:
            if title == '':
                title = data


    return ( links[0], [ image, title, price ] )
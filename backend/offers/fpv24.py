from autoscraper import AutoScraper


example_url = 'https://www.fpv24.com/de/search?search=foxeer'
wanted_links = [ 'https://www.fpv24.com/de/foxeer/foxeer-caesar-fpv-racing-frame-3-zoll' ]
link_scraper = AutoScraper()
link_scraper.build(example_url, wanted_list=wanted_links)

example_url = 'https://www.fpv24.com/de/foxeer/foxeer-caesar-fpv-racing-frame-3-zoll'
wanted_image_title_price = [ 'https://cdnc.meilon.de/img/product/fo/fox-fr1198/fox-fr1198-256d2f_m.jpg', 'Foxeer Caesar FPV Racing Frame 3 Zoll', '44,90 € *' ]
product_info_scraper = AutoScraper()
product_info_scraper.build(example_url, wanted_list=wanted_image_title_price)

def get_offer(query):
    url = f'https://www.fpv24.com/de/search?search={query}'
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
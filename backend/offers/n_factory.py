from autoscraper import AutoScraper


example_url = 'https://n-factory.de/index.php?qs=iflight&search='
wanted_links = [ 'https://n-factory.de/iFlight-FPV-M8Q-5883-GPS-Module-V20' ]
link_scraper = AutoScraper()
link_scraper.build(example_url, wanted_list=wanted_links)

example_url = 'https://n-factory.de/iFlight-FPV-M8Q-5883-GPS-Module-V20'
wanted_image_title_price = [ 'https://n-factory.de/media/image/product/4874/lg/iflight-fpv-m8q-5883-gps-module-v20.jpg', 'iFlight FPV M8Q-5883-GPS Module V2.0', '43,95 € ' ]
product_info_scraper = AutoScraper()
product_info_scraper.build(example_url, wanted_list=wanted_image_title_price)

def get_offer(query):
    url = f'https://n-factory.de/index.php?qs={query}&search='
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
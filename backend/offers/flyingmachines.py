from autoscraper import AutoScraper


example_url = 'https://www.flyingmachines.de/search?type=article%2Cpage%2Cproduct&q=foxeer*'
wanted_links = [ 'https://www.flyingmachines.de/products/foxeer-toothless-v2-nano-1-7mm-objektiv-schwarz?_pos=1&_sid=19a121f84&_ss=r' ]
link_scraper = AutoScraper()
link_scraper.build(example_url, wanted_list=wanted_links)

example_url = 'https://www.flyingmachines.de/products/foxeer-toothless-v2-nano-1-7mm-objektiv-schwarz?_pos=1&_sid=19a121f84&_ss=r'
wanted_image_title_price = [ 'https://www.flyingmachines.de/cdn/shop/products/bb_635x635.jpg?v=1638389001', 'Foxeer Toothless V2 Nano Linse', '€36,95' ]
product_info_scraper = AutoScraper()
product_info_scraper.build(example_url, wanted_list=wanted_image_title_price)

def get_offer(query):
    url = f'https://www.flyingmachines.de/search?type=article%2Cpage%2Cproduct&q={query}'
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
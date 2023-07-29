import asyncio
import aiohttp
from aiohttp import ClientSession
import bs4
import csv
from tqdm import tqdm

MAIN_URL = 'https://kivano.kg'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}


async def fetch(url, session):
    async with session.get(url, headers=HEADERS) as response:
        return await response.text()


async def get_soup(url, session):
    html = await fetch(url, session)
    return bs4.BeautifulSoup(html, 'html.parser')


async def parse_product(product, session):
    url = MAIN_URL + product.find('div', class_='listbox_title oh').find('a')['href']

    soup = await get_soup(url, session)

    name = product.find('div', class_='listbox_title oh').text.strip()

    price = ''.join(
        filter(str.isdigit, product.find('div', class_='listbox_price text-center').find('strong').text.strip()))

    img_div = soup.find('div', class_='img_full addlight')
    img_url = 'https://kivano.kg' + img_div.find('a')['href'] if img_div else 'No image'

    description = soup.find('div', {'id': 'desc'}).text.strip()

    data = {
        'name': name,
        'price': price,
        'img_url': img_url,
        'description': description
    }

    return data


async def parse(url, session):
    print(f'Парсинг {url}')
    soup = await get_soup(url, session)

    products = soup.find_all('div', class_='item product_listbox oh')

    tasks = []
    for product in products:
        task = asyncio.create_task(parse_product(product, session))
        tasks.append(task)

    data = await asyncio.gather(*tasks)
    return data


async def main(urls):
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(parse(url, session))
            tasks.append(task)

        pages_data = await asyncio.gather(*tasks)

        products_data = []
        for page_data in pages_data:
            products_data.extend(page_data)

        print(f'Получено {len(products_data)} продуктов')

        # сохраняем данные в CSV
        with open('products.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=products_data[0].keys())
            writer.writeheader()
            writer.writerows(products_data)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    category_urls = [f'{MAIN_URL}/dukhovki?page={page}' for page in range(1, 5)]
    loop.run_until_complete(main(category_urls))
    loop.close()

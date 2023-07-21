import bs4
import requests
import xlsxwriter

main_url = 'https://kivano.kg'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# Создаем список для хранения данных
data = [['name','description','category_id','brand_id','video_provider','video_link','tags','unit_price','purchase_price','unit','slug','current_stock','sku','meta_title','meta_description','thumbnail_img','photos']]

# Функция для получения объекта BeautifulSoup
def get_soup(url, headers):
    res = requests.get(url, headers=headers)
    return bs4.BeautifulSoup(res.text, 'html.parser')

# Перебираем все страницы категории
page_num = 1
while page_num<=15:
    # Получаем страницу категории
    category_page = get_soup(main_url + '/dukhovki?page=' + str(page_num), headers)

    # Получаем все товары на странице
    products = category_page.find_all('div', class_='item product_listbox oh')

    # Если на странице нет товаров, значит достигнут конец категории
    if len(products) == 0:
        break

    # Обходим все товары и получаем необходимые данные
    for product in products:
        name = product.find('div', class_='listbox_title oh').text.strip()
        unit_price = ''.join(filter(str.isdigit, product.find('div', class_='listbox_price text-center').find('strong').text.strip()))
        category_id = '105'
        brand_id = '1'
        video_provider = 'youtube'
        video_link = ''
        tags = 'кастрюли'
        purchase_price = ''
        unit = 'шт'
        slug = ''
        current_stock = '10'
        sku = ''
        meta_title = name
         
        # Получаем ссылку на страницу товара
        product_url = main_url + product.find('div', class_='listbox_title oh').find('a')['href']
        print(product_url)

        # Заходим на страницу товара и получаем ссылку на изображение
        product_page = get_soup(product_url, headers)
        img_div = product_page.find('div', class_='img_full addlight')
        if img_div is not None:
            thumbnail_img = 'https://kivano.kg'+img_div.find('a')['href']
        else:
            thumbnail_img = 'No image found'
        photos = thumbnail_img
        description = product_page.find('div', {'id': 'desc'}).text.strip()
        meta_description = description
        data.append([name,description,category_id,brand_id,video_provider,video_link,tags,unit_price,purchase_price,unit,slug,current_stock,sku,meta_title,meta_description,thumbnail_img,photos])

    # Увеличиваем номер страницы
    page_num += 1

# Записываем данные в файл Excel
with xlsxwriter.Workbook('duhovki.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
    for row_num, info in enumerate(data):
        worksheet.write_row(row_num, 0, info)

# Парсер товаров с Kivano.kg

## Введение

Этот проект был создан для сбора информации о каждом товаре на Kivano.kg и сохранения ее в формате CSV. С помощью асинхронного программирования удалось достичь быстрого парсинга веб-страниц.

## Используемые технологии
Были использованы следующие технологии:
- ![Python](https://img.shields.io/badge/python-3670A0?&logo=python&logoColor=ffdd54)  -  основной язык программирования
- ![asyncio](https://img.shields.io/badge/asyncio-039BE5?&logo=asyncio&logoColor=white)  -  для асинхронного выполнения
- ![aiohttp](https://img.shields.io/badge/aiohttp-29334C?&logo=aiohttp&logoColor=white)  -  асинхронные HTTP запросы
- ![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-E6007A?&logo=BeautifulSoup&logoColor=white)- анализ HTML
- ![csv](https://img.shields.io/badge/csv-%230C55A5.svg?&logo=csv&logoColor=%white)   -  экспорт данных в CSV
Такое сочетание технологий позволяет быстро парсить и собирать данные о товарах.

## Архитектура
Проект состоит из следующих основных частей:

- `fetch()` - загружает веб-страницу
- `get_soup()` - создает объект BeautifulSoup из HTML
- `parse_product()` - извлекает данные одного товара
- `parse()` - парсит все товары на странице
- `main()` - вызывает все необходимые функции
Каждая функция выполняет отдельную задачу, и они скомбинированы для совместной работы.

## Порядок работы
Сначала вызывается `main()`
Он создает URL страниц и вызывает `parse()` для каждой из них
`parse()` внутри вызывает `parse_product()` для каждого товара
Собранные данные записываются в CSV файл
В результате все процессы выполняются последовательно и синхронно.

## Заключение
Данный проект является удобным средством для сбора информации о товарах на Kivano.kg. Путем доработки можно создать бота, охватывающего больше сайтов.

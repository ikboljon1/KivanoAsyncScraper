# Парсер данных о духовках с сайта Kivano.kg
Эта программа собирает информацию о всех товарах в категории "духовки" на сайте интернет-магазина Kivano.kg и записывает её в Excel-файл.

Используемые технологии
Python
BeautifulSoup - для парсинга веб-страниц
Requests - для HTTP-запросов
xlsxwriter - для работы с excel-файлами
Работа скрипта
Скрипт парсит каждую страницу категории "духовки" на сайте Kivano.kg
Для каждого товара собирает такие данные как:
название
описание
цена
картинка
и др.
Собранные данные записываются в Excel-файл
Использование
Запустите скрипт командой python kivano_parser.py. Результат будет записан в duhovki.xlsx.

При необходимости можно внести изменения в код скрипта для парсинга других категорий или сайтов.

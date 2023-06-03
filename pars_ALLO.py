import time
import requests
from bs4 import BeautifulSoup
import xlsxwriter
import pandas as pd
import json

headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)"
                         " Chrome/109.0.0.0 Mobile Safari/537.36)"}

get_data = [["Назва/Модель", "Ціна", "Посилання", "Фото"]]

for count in range(1, 2):
    url = f"https://allo.ua/ua/products/mobile/dir-asc/order-price/p-{count}/proizvoditel-nokia/"

    time.sleep(5)
    response = requests.get(url, headers=headers)

    with open('result.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup)
    # вибраний виробник Samsung( з data і буде братися вся інфа)
    data = soup.find_all("div", class_="product-card")
    # print(data)

    # витягуємо ссилки, ціну, назви на моделі(1 сторінка)
    for i in data:
        link = i.find("a").get("href")
        price = i.find("div", class_="v-pb__cur").text
        name = i.find("a", class_="product-card__title").text
        img_url = i.find("img", class_="gallery__img lazyload").get("data-src")
        # print(link, price, name, img_url)
        get_data.append([name, price, link, img_url])
        # Створюємо документ excel і вносимо туди всі знайдені дані
with xlsxwriter.Workbook("smartfone3.xlsx") as workbook:
    worksheet = workbook.add_worksheet()
    for row_num, info in enumerate(get_data):
        worksheet.write_row(row_num, 0, info)
        




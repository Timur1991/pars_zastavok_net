import requests
from bs4 import BeautifulSoup
# pip install lxml

# будем парсить https://zastavok.net/
# скачиваем изображения с сайта
# работа выполнена по видеоуроку в целях самообучения

page = 1
image_number = 0

# можно добавить к ссылке раздел, который нужно скачивать,
# например "https://zastavok.net/auto/" для скачивания автомобилей

link = f'https://zastavok.net'

# проходимся по страницам от 1 до range, в данный момент до 3-й страницы (включительно)
for storage in range(3):
    responce = requests.get(f'{link}/{page}').text
    soup = BeautifulSoup(responce, 'lxml')
    block = soup.find('div', class_='block-photo')
    all_image = block.find_all('div', class_='short_full')

    # ищем и скачиваем каждое изображение на странице
    print(f'Страница {page}:')
    for image in all_image:
        image_link = image.find('a').get('href')
        image_name = image.find('img').get('alt')
        #print(f'{image_name}: {image_link}')
        download_storage = requests.get(f'{link}{image_link}').text
        #print(download_image)
        download_soup = BeautifulSoup(download_storage, 'lxml')
        download_block = download_soup.find('div', class_='block_down')
        result_link = download_block.find('a').get('href')
        #print(result_link)

        # получаем изображение
        image_bytes = requests.get(f'{link}{result_link}').content

        # сохраняем наше полученное изображение
        with open(f'image/{image_number}-{image_name}.jpg', 'wb') as file:
            file.write(image_bytes)
        image_number += 1
        print(f'Изображение {image_number}-{image_name}" - успешно скачано!')
    page += 1





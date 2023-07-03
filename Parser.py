import requests
from bs4 import BeautifulSoup

# открываем страницу с продавцами
url = "https://uzum.uz"
response = requests.get(url)

# создаём объект BeautifulSoup для парсинга контента HTML-страницы
soup = BeautifulSoup(response.content, 'html.parser')

# извлекаем контактные данные всех продавцов
contacts = []
for seller in soup.find_all('div', class_='text-right w-100'):
    contact = {}
    contact['name'] = seller.find('h5', class_='mb-0').text
    contact['address'] = seller.find('p', class_='mb-0').text
    contact['phone'] = seller.find('p', class_='buyuk').text
    contact['email'] = seller.find('p', class_='kucuk').text
    contacts.append(contact)

# печатаем контактные данные
for contact in contacts:
    print(contact)


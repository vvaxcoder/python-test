# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request

# help('modules')

req = urllib.request.urlopen("https://www.ua-football.com/sport")
html = req.read()

soup = BeautifulSoup(html, 'html.parser')

news = soup.find_all('li', class_='liga-news-item')
# print(news)

results = []

for item in news:
    title = item.find(
        'span', class_='fz-16 fw-500 d-block').get_text(strip=True)
    description = item.find(
        'span', class_='name-dop fz-12').get_text(strip=True)
    href = item.a.get('href')
    results.append({
        'title': title,
        'description': description,
        'href': href,
    })

# print(results)
f = open('news.txt', 'w', encoding='utf-8')

i = 1
for news in results:
    f.write(f'Новость № {i}\n\n')
    f.write(f'Название: {news["title"]}\n')
    f.write(f'Описание: {news["description"]}\n')
    f.write(f'Ссылка: {news["href"]}\n\n******************\n')
    i += 1

f.close()

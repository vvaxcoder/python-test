# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request


class ParserFromLesson34:
    raw_html = ''
    html = ''
    results = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html, 'html.parser')

    def parsing(self):
        news = self.html.find_all('li', class_='liga-news-item')

        for item in news:
            title = item.find(
                'span', class_='fz-16 fw-500 d-block').get_text(strip=True)
            description = item.find(
                'span', class_='name-dop fz-12').get_text(strip=True)
            href = item.a.get('href')
            self.results.append({
                'title': title,
                'description': description,
                'href': href,
            })

    def writeToFile(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            i = 1
            for news in self.results:
                f.write(f'Новость № {i}\n\n')
                f.write(f'Название: {news["title"]}\n')
                f.write(f'Описание: {news["description"]}\n')
                f.write(f'Ссылка: {news["href"]}\n\n******************\n')
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.writeToFile()

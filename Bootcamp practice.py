from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-120338'
title = 'Titanic'

result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
box = soup.find('article', class_='main-article')
transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

with open(f'{title}.txt', 'w', encoding='utf-8') as file:
    file.write(transcript)

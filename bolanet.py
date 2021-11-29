import requests
from bs4 import BeautifulSoup

anti_block = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

url = 'https://www.bola.net/trending/'

r = requests.get(url, headers=anti_block)
contents = BeautifulSoup(r.text, 'html.parser')
most_viewd = contents.find('div', 'bigcon')
tables = most_viewd.find_all('div', 'fb-container')
for table in tables:
    judul = table.find('div', 'fb-title').text
    link_berita = table.find('div', 'fb-title').find('a')['href']
    gambar = table.find('div', 'fb-image').find('img')['src']
    waktu = table.find('div', 'fb-day').text
    urutan = table.find('div', 'fb-num').text
    print(judul)



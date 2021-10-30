import requests
from bs4 import BeautifulSoup
import pandas as pd

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/95.0.4638.69 Safari/537.36 '
}

url = 'https://store.steampowered.com/'
req = requests.get(url, headers=header)
soup = BeautifulSoup(req.text, 'html.parser')

top_sellers = soup.find('div', attrs={'id': 'tab_topsellers_content'})
content = top_sellers.find_all('a', 'tab_item')

data_list = []
for item in content:
    title = item.find('div', 'tab_item_name').text
    price = item.find('div', 'discount_final_price').text
    genre = item.find('div', 'tab_item_top_tags').text
    data = {
        'Title': title,
        'Price': price,
        'Genre': genre
    }
    data_list.append(data)

df = pd.DataFrame(data_list)
df.to_csv('Data.csv')








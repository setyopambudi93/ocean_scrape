import requests
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/95.0.4638.69 Safari/537.36 '
}

url = 'https://store.steampowered.com/hwsurvey/'

list_link =[]
def get_link():
    req = requests.get(url, headers=header)
    soup = BeautifulSoup(req.text, 'html.parser')
    items = soup.find_all('div', 'graph_holder')
    for item in items:
        try:
            link = item.find('a')['href']
        except:
            link = 'Link tidak tersedia'

        data_dict = {
            'Link': link
        }
        list_link.append(link)

    return list_link
listrik = []
def videocard():
    url = 'https://store.steampowered.com/hwsurvey/videocard/'
    req = requests.get(url, headers=header)
    soup = BeautifulSoup(req.text, 'html.parser')
    # all_video_cards = soup.find_all('div', attrs={'id': 'sub_stats'})
    distribusi_0 = soup.find_all('div', 'substats_row row_0')
    distribusi_1 = soup.find_all('div', 'substats_row row_1')
    listrik.append(distribusi_0 + distribusi_1)
    print(listrik)

    # for dis in distribusi:
    #     busi = dis.find('div', 'substats_col_left')
    #     juni = dis.find('div', 'substats_col_month')
    #     oktober = dis.find('div', 'substats_col_month_last_pct')
    #     print(busi)

















def get_item():

    req = requests.get(url, headers=header)
    soup = BeautifulSoup(req.text, 'html.parser')
    datas = soup.find_all('div', attrs={'class': 'stats_row'})

    for data in datas:
        itm = data.find('div', 'stats_col_left').text
        # popular = data.find('div', 'stats_col_mid').text

        print(itm)


if __name__ == '__main__':
    videocard()

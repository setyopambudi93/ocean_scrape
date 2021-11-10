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
    rows = soup.find_all('div', 'substats_row')
    for row in rows:
        distribution = row.find('div', 'substats_col_left').text
        mounth = row.find_all('div', 'substats_col_month')
        juni = mounth[0:4][0].text
        juli = mounth[0:4][1].text
        aug = mounth[0:4][2].text
        sept = mounth[0:4][3].text
        oct = row.find('div', 'substats_col_month_last_pct').text
        percent = row.find('div', 'substats_col_month_last_chg').text

        data_dict = {
            'OVERALL DISTRIBUTION OF CARDS': distribution,
            'JUN': juni,
            'JUL': juli,
            'AUG': aug,
            'SEPT': sept,
            'OCT': oct,
            'Percent': percent
        }
        print(data_dict)

    # for row in rows:
    #     subtat = row.find('div', 'substats_col_left')
    #     month = [r.text.strip() for r in row.find_all('div', 'substats_col_month')] + [
    #         row.find('div', 'substats_col_month_last_pct').text.strip()
    #         + ' '
    #         + row.find('div', 'substats_col_month_last_chg').text.strip()
    #     ]
    #
    #     data_dict = {
    #         'Overal': subtat,
    #         'Juni': month[0],
    #         'Juli': month[1],
    #         'August': month[2],
    #         'Sept': month[3],
    #         'Oct': month[4],
    #         'Percent': month[4].split(' ')[1]

        # }
        # print(data_dict)


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

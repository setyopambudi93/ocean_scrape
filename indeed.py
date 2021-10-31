import json

import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/95.0.4638.69 Safari/537.36 '
}


url = 'https://www.indeed.com/jobs?'
site = 'https://www.indeed.com'

def get_total_pages():
    params = {
        'q': 'Virtual assistant',
        'l': 'New York State'
    }

    req = requests.get(url, params=params, headers=header)

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/req.html', 'w+') as outfile:
        outfile.write(req.text)
        outfile.close()

    total_pages = []

    # scrape
    soup = BeautifulSoup(req.text, 'html.parser')
    pagination = soup.find('ul', "pagination-list")
    pages = pagination.find_all('li')
    for page in pages:
        total_pages.append(page.text)

    total = int(max(total_pages))
    return total


def get_all_item():
    params = {
        'q': 'Virtual assistant',
        'l': 'New York State'
    }

    req = requests.get(url, params=params, headers=header)

    with open('temp/req.html', 'w+') as outfile:
        outfile.write(req.text)
        outfile.close()

    soup = BeautifulSoup(req.text, 'html.parser')

    # scrape
    details = soup.find_all('table', 'jobCard_mainContent big6_visualChanges')
    des = soup.find_all('table', 'jobCardShelfContainer big6_visualChanges')
    new_list = []
    for detail in details:
        job_title = detail.find('h2', 'jobTitle').text
        company = detail.find('span', 'companyName')
        location = detail.find('div', 'companyLocation').text
        company_name = company.text
        try:
            company_link = site + company.find('a')['href']
        except:
            company_link = 'Link Not Available'
        # sorting
        data_dict = {
            'Job Title': job_title,
            'Company Name': company_name,
            'Company Website': company_link
        }
        new_list.append(data_dict)

    # json
    try:
        os.mkdir('json_result')
    except FileExistsError:
        pass

    with open('json_result/job_list.json', 'w+') as json_data:
        json.dump(new_list, json_data)
    print('Json has been created')


    #     data = {
    #         'Job Title': job_seeker,
    #         'Company Name': company,
    #         'Location': location
    #     }
    #     new_list.append(data)
    # return new_list


# def create_document(dataframe, filename):
#     df = pd.DataFrame(dataframe)
#     df.to_csv(f'{filename}.csv')
#     df.to_excel(f'{filename}.xlsx')
#
#
#
#
if __name__ == '__main__':
    get_all_item()

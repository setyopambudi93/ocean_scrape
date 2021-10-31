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

def get_total_pages(query, location):
    params = {
        'q': query,
        'l': location
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


def get_all_item(query, location, start, page):
    params = {
        'q': query,
        'l': location,
        'start': start
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

    with open(f'json_result/{query}_in_{location}_page_{page}.json', 'w+') as json_data:
        json.dump(new_list, json_data)
    print('Json has been created')
    return new_list

    # create csv


def create_document(dataFrame, filename):
    try:
        os.mkdir('data_result')
    except FileExistsError:
        pass

    df = pd.DataFrame(dataFrame)
    df.to_csv(f'data_result/{filename}.csv', index=False)
    df.to_excel(f'data_result/{filename}.xlsx', index=False)

    # generate
    print(f'{filename}.csv and {filename}.xlsx has been created')

def run():
    query = input('Enter your query : ')
    location = input('Enter your location : ')

    total = get_total_pages(query, location)
    counter = 0
    final_result = []
    for page in range(total):
        page += 1
        counter += 10
        final_result += get_all_item(query, location, counter, page)

    # formatting data
    try:
        os.mkdir('reports')
    except FileExistsError:
        pass

    with open('reports/{}.json'.format(query), 'w+') as final_data:
        json.dump(final_result, final_data)

    print('Data created')

    # created document
    create_document(final_result, query)


if __name__ == '__main__':
    run()

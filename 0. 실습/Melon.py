import pandas as pd
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get("https://www.melon.com/chart/index.htm", headers=headers)


if response.status_code == 200:
    html_code = response.text

soup = BeautifulSoup(html_code, 'lxml')

lst50_elements = soup.find_all('tr', class_='lst50')
lst100_elements = soup.find_all('tr', class_='lst100')
data = []
i = 1
for tr_element in lst50_elements:
    div_element = tr_element.find('div', class_='ellipsis rank01')
    text = ""
    name = ""
    singer = ""
    if div_element:
        a_element = div_element.find('a')
        if a_element:
            name = a_element.text.strip()

    div_element = tr_element.find('div', class_='ellipsis rank02')
    if div_element:
        a_element = div_element.find('a')
        if a_element:
            singer = a_element.text.strip()

    text = f'{i}. 제목: ' + name +  "  가수: " + singer
    data.append([i, name, singer])
    print(text )
    i = i + 1



for tr_element in lst100_elements:
    div_element = tr_element.find('div', class_='ellipsis rank01')
    text = ""
    name = ""
    singer = ""
    if div_element:
        a_element = div_element.find('a')
        if a_element:
            name = a_element.text.strip()

    div_element = tr_element.find('div', class_='ellipsis rank02')
    if div_element:
        a_element = div_element.find('a')
        if a_element:
            singer = a_element.text.strip()

    text = f'{i}. 제목: ' + name +  "  가수: " + singer
    print(text)
    data.append([i, name, singer])
    i = i + 1


df = pd.DataFrame(data, columns=['순위', '제목', '가수'])

# 엑셀 파일로 저장
df.to_excel('melon_chart_data.xlsx', index=False)
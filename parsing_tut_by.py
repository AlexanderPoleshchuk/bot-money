from bs4 import BeautifulSoup
import requests


URL = "https://finance.tut.by/kurs/"
HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'snap Chromium/80.0.3987.132 Chrome/80.0.3987.132 Safari/537.36', 'accept': '*/*'
}

def get_html(url, params = None):
    r = requests.get(url, headers = HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('tr')
    course_currency = {}
    for item in items:
        if item.find('td', class_='first'):
            if item.find('td', class_='first').get_text() in ['Доллар США', 'Евро', '100 российских рублей']:
                course_currency[item.find('td', class_='first').get_text()] = \
                    float(item.find('td', class_='inctances').get('data-nbrb')[:5])
    return course_currency


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        return get_content(html.text)
    else:
        return "Errors"

if __name__ == '__main__':
    print(parse())
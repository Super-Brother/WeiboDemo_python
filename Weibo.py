import requests
from bs4 import BeautifulSoup
from urllib import parse
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'
}


def get_html(url):
    html = requests.get(url, headers=headers)
    if html.status_code == 200:
        parse_html(html.text)
    else:
        print('error', html.text)
    return


def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.select('table tbody tr')
    for tr in trs:
        title = tr.select_one('td a').text
        url = tr.select_one('td a')['href']
        url = parse.urljoin('https://s.weibo.com', url)
        print(title, url)


if __name__ == '__main__':
    start = time.time()

    urls = [
        'https://s.weibo.com/top/summary?cate=realtimehot',
        'https://s.weibo.com/top/summary?cate=socialevent'
    ]
    for url in urls:
        get_html(url)

    print(time.time() - start)

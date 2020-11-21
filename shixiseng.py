import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}


def get_html(url):
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    works = soup.select('div.intern-wrap')
    for work in works:
        link = work.select_one('div p a')['href']
        details_html(link)


def details_html(url):
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    companyName = soup.select_one('a.com-name').text
    # 破解自定义字体
    salary = soup.select_one('span.job_money').text.encode('utf-8')
    salary = salary.replace(b'\xef\x87\xb6', b'0')
    salary = salary.replace(b'\xee\x85\x9d', b'1')
    salary = salary.replace(b'\xee\x95\x98', b'2')
    salary = salary.replace(b'\xee\xb6\x8c', b'3')
    salary = salary.replace(b'\xee\x9b\x88', b'4')
    salary = salary.replace(b'\xee\xb6\xa1', b'5')
    salary = salary.replace(b'\xee\x86\xaf', b'6')
    salary = salary.replace(b'\xee\x83\xa6', b'7')
    salary = salary.replace(b'\xef\xa1\xad', b'8')
    salary = salary.replace(b'\xee\x98\xb6', b'9')
    salary = salary.decode()
    print(soup.title.text, companyName, salary)


if __name__ == '__main__':
    for i in range(1, 7):
        url = 'https://www.shixiseng.com/interns?keyword=python&page={}'.format(i)
        get_html(url)

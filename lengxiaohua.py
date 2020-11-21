import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36 Edg/86.0.622.68'
}


def get_html(url):
    html = requests.get(url, headers=headers)
    # print(html.text)
    soup = BeautifulSoup(html.text, 'lxml')
    jokes = soup.select('li.article-summary')
    for joke in jokes:
        title = joke.select_one('span a').text
        print(title)
        contents = joke.select_one('div.summary-text').select('p')
        for content in contents:
            jokeContent = content.text.strip().replace('\n','').replace(' ','')
            if not jokeContent == '':
                print(jokeContent)
        print('*'*20)

if __name__ == '__main__':
    for i in range(1):
        print('正在爬取第{}页'.format(i))
        url = 'http://xiaohua.zol.com.cn/lengxiaohua/{}.html'.format(i)
        get_html(url)

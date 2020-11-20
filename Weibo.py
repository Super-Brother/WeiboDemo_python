import asyncio
import time
from urllib import parse

import aiohttp
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'
}


async def get_html(url):
    print('正在爬取。。。', url)
    # html = requests.get(url, headers=headers)
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                parse_html(await resp.text())
            else:
                print('error', resp.status)
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
    tasks = []
    for url in urls:
        tasks.append(get_html(url))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    print(time.time() - start)

    loop.close()

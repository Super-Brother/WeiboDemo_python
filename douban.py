import requests
from bs4 import BeautifulSoup
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
    'Cookie': 'll="118237"; bid=0FEiwgEFVnU; gr_user_id=b5da6ccb-c7ee-4246-aa02-726f9c81ab3e; _vwo_uuid_v2=D334EBC9F99E1776B6215120F068DE2CE|d2761ce25b3d4b953b7d681432f13199; douban-fav-remind=1; __utmc=30149280; __utmc=81379588; viewed="6709783_35218970_1320347_26333850_25745691_2037836_27086077_35016532"; ct=y; __utma=30149280.1140089955.1589271763.1605150041.1605851799.13; __utmz=30149280.1605851799.13.11.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=c1aac70d-dd90-487a-802c-e011a2c60cb1; gr_cs1_c1aac70d-dd90-487a-802c-e011a2c60cb1=user_id%3A0; __utmt_douban=1; __utma=81379588.1293952674.1589271765.1604649537.1605851801.10; __utmz=81379588.1605851801.10.8.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt_t1=1; ap_v=0,6.0; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1605851801%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.3ac3=*; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_c1aac70d-dd90-487a-802c-e011a2c60cb1=true; __utmb=81379588.2.10.1605851801; __utmb=30149280.9.8.1605851812521; _pk_id.100001.3ac3=4ec3cf99dfe2d2b8.1589271765.10.1605851813.1604649537.; RT=s=1605852387429&r=https%3A%2F%2Fbook.douban.com%2Ftop250%3Ficn%3Dindex-book250-all'
}


def get_html(url):
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    books = soup.select('tr.item')
    for book in books:
        bookName = book.select_one('td div a').text.replace('\n', '').replace(' ', '')
        author = book.select_one('td p').text
        print(bookName, author)

        try:
            oneSentence = book.select_one('td p.quote span').text
            print(oneSentence)
        except AttributeError as e:
            print('没有一句话')

        bookPicUrl = book.select_one('td a img')['src']
        save_photo(bookPicUrl, bookName)

        print('*' * 20)


def save_photo(picUrl, bookName):
    filePath = './doubanbook'
    if not os.path.exists(filePath):
        os.mkdir(filePath)

    pic = requests.get(picUrl, headers=headers)
    with open('./doubanbook/{}.jpg'.format(bookName), 'wb') as f:
        f.write(pic.content)


# 爬豆瓣读书Top250
if __name__ == '__main__':
    for i in range(10):
        url = 'https://book.douban.com/top250?start={}'.format(i * 25)
        print("正在获取第{}页".format(i))
        get_html(url)

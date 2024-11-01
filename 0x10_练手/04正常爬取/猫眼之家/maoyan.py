# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import csv
from urllib.parse import urlencode

# 请求头设置
header = {
    'Accept': '*/*;',
    'Connection': 'keep-alive',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': '__mta=208903085.1701179842456.1701183760733.1701183840823.9; _lxsdk_cuid=18c1634179ac8-00cf6dc9884ff5-7f5d547e-1fa400-18c1634179a46; uuid_n_v=v1; uuid=9E5222D0DB0011EE9F28D3BFFA06DA4952EF879DE9874685B9E56AE2B58F9419; _lxsdk=9E5222D0DB0011EE9F28D3BFFA06DA4952EF879DE9874685B9E56AE2B58F9419; _csrf=fe45c78b006dae47cf14d3f1f3399a34d98b75a764f28a3444c33b43ff043992; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1709650620,1709883537; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1709883581; __mta=208903085.1701179842456.1701183840823.1709883581338.10; _lxsdk_s=18e1d00378b-08-d51-84b%7C%7C4',
    'Host': 'www.maoyan.com',
    'Referer': 'https://www.maoyan.com/films',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76'
}

def web(url):
    db_data = requests.get(url, headers=header)
    db_data = db_data.content.decode('utf-8')
    soup = BeautifulSoup(db_data.replace("&#x",""), 'lxml')
    movie_list = soup.select('body > div.container > div.movies-channel > div.movies-panel > div.movies-list > dl.movie-list dd ')

    with open('maoyan.csv', 'a', encoding='utf-8') as csvfile:
        fieldnames = ["电影名称", "电影海报", "电影评分", "电影类型", "电影主演", "电影上映时间"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for movie in movie_list:
            movie_title = movie.select('div.channel-detail > a')[0].get_text()
            movie_img = movie.select('div.movie-item > a > div.movie-poster img')[1].attrs['data-src']
            movie_star = movie.select('.channel-detail-orange')[0].get_text()
            movie_type = movie.select('div.film-channel > div.movie-item-hover > a > div.movie-hover-info div')[1].get_text().split("\n")[2].split('              ')[1]
            movie_actors = movie.select('div.film-channel > div.movie-item-hover > a > div.movie-hover-info div')[2].get_text().split("\n")[2].split('              ')[1]
            movie_screen_time = movie.select('div.film-channel > div.movie-item-hover > a > div.movie-hover-info div')[3].get_text().split("\n")[2].split('              ')[1]

            writer.writerow({'电影名称': movie_title, '电影海报': movie_img, '电影评分': movie_star, '电影类型': movie_type, '电影主演': movie_actors, '电影上映时间': movie_screen_time})
            print("正在写入: \n" + movie_title + "\n" + movie_img + "\n" + movie_star + "\n" + movie_type + "\n" + movie_actors + "\n" + movie_screen_time + "\n")
            print('---------------------------------------------------------------------------------------------')


def setCsv(offset):
    base_url = 'https://www.maoyan.com/films'
    params = {
        'offset': offset
    }
    url = base_url + '?' + urlencode(params)
    web(url)


if __name__ == '__main__':
    offset = 0
    setCsv(offset)  # str为标签名
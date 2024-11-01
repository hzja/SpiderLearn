# import requests
# import os
# import time
# import threading
#
#
# urls = []
# for i in range(1,14):
#     urls.append('https://www.bilibili.com/video/BV1bK411A7tV?p=%s' % (i) )
#
#
# def craw(url):
#     r = requests.get(url)
#     print(url ,',', len(r.content))
#
# def parse(html):
#
# def singal_craw():
#     print('singal craw begins.')
#     for url in urls:
#         craw(url)
#     print('single craw ends.')
#
# def multi_thread():
#     print('multi_thread begins.')
#     tds = []
#     for url in urls:
#         tds.append(threading.Thread(target=craw,args=(url,)))
#
#     for td in tds:
#         td.start()
#
#     for td in tds:
#         td.join()
#
#     print('multi_thread ends.')
#
# if __name__ == '__main__':
#     start = time.time()
#     singal_craw()
#     end = time.time()
#     print('singal_craw cost:',end - start)
#
#     start = time.time()
#     multi_thread()
#     end = time.time()
#     print('multi_thread cost:',end - start)
#

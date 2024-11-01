from requests_html import HTMLSession

session = HTMLSession()

page_size = int(input("请输入总页码："))
for page in range(1, page_size + 1):

    world = session.get(f'http://www.world68.com/top.asp?t=5star&page={page}')
    world.encoding = 'gb2312'
    # world.html.encoding = "gb2312"
    # print(world.text)
    print("正在采集数据", world.url)
    title_a = world.html.find('dl>dt>a')
    for item in title_a:
        name = item.text
        url = item.attrs['href']
        with open('webs1.txt', "a+", encoding="utf-8") as f:
            f.write(f"{name},{url}\n")

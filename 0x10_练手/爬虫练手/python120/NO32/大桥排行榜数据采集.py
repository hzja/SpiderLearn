from pyquery import PyQuery as pq
import time


def remove(str):
    return str.replace("<br/>", "").replace("\n", "").replace(",", "，")


def get_data(page):
    url = "http://www.highestbridges.com/wiki/index.php?title=List_of_Highest_International_Bridges/Page_{}".format(
        page)
    print(url)
    doc = pq(url=url, encoding='utf-8')
    print(doc('title'))

    # 获取所有数据所在的行，下面使用的是 css 选择器，称作 jquery 选择器也没啥问题

    items = doc.find('table.wikitable.sortable tr').items()
    for item in items:
        td_list = item.find('td')
        rank = td_list.eq(1).find("span.sorttext").text()
        name = remove(td_list.eq(2).find("a").text())
        height = remove(td_list.eq(3).text())
        length = remove(td_list.eq(4).text())
        completed = remove(td_list.eq(5).text())
        location = remove(td_list.eq(6).text())
        country = remove(td_list.eq(7).text())
        data_tuple = (rank, name, height, length, completed, location, country)

        save(data_tuple)


def save(data_tuple):
    try:
        my_str = ",".join(data_tuple) + "\n"
        # print(my_str)
        with open(f"./data.csv", "a+", encoding="utf-8") as f:
            f.write(my_str)
            print("写入完毕")
    except Exception as e:
        pass


if __name__ == '__main__':
    for page in range(1, 14):
        get_data(page)
        time.sleep(3)

# coding=utf-8
import re
from bs4 import BeautifulSoup
import requests
from fontTools.ttLib import TTFont
from lxml import etree
import csv

def save(item):#保存项
    with open("大众点评-广州按摩足疗.csv", 'a', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(item.values())

url = 'http://www.dianping.com/guangzhou/ch30/g141'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Cookie':'s_ViewType=10; _lxsdk_cuid=18c160e3216c8-0ca5a09217876d-7f5d547e-1fa400-18c160e3216c8; _lxsdk=18c160e3216c8-0ca5a09217876d-7f5d547e-1fa400-18c160e3216c8; _hc.v=4ee89152-fe96-75f2-15a5-8c2ef2a4b80f.1701177080; WEBDFPID=4y72z6y0435u578wyw00x3v7x0x8x6xv81x839v6v2797958wux0263y-2016537080034-1701177078771WSQMEMQfd79fef3d01d5e9aadc18ccd4d0c95071832; qruuid=99670d7a-c17e-4788-ac66-b996eeeb223f; dplet=4f605a06537c4cca4da8aa79e530733b; dper=0202442110c9f7cd5ce9904a7d776b5a613f160c71700330ec8fbdbc3fcc436fe398478d32804c3d8f41f1af937971c62193056c1e788a2dc21200000000a81d000094618bb6df9217ddfc1a179b9c25fa689bb18899fc7c3d4da96005a0818f79929e6779a405523df00339d87683f19604; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_97879370719; ctu=a35b7a7236b7add3a718186d02b66f35ac212dcfe1084da159addcc47a484ae5; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1706550273; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1706550273; _lxsdk_s=18d5651f953-327-5f3-ce8%7C%7C26',
    'Host':'www.dianping.com',
    'Referer':'http://www.dianping.com/search/category/2/10/g141',
}
response = requests.get(url,headers=headers)
content = response.content.decode('utf-8')#获取网页源代码，并编译为utf-8编码
content = re.sub(r"&#x(\w+?);", r"*\1*", content)#用原数字两边加上星号的方法替换掉特殊字符,如用*f459*替换&#xf459

html = etree.HTML(content)
item_List = html.xpath('//*[@id="shop-all-list"]/ul//li')#获取项目列表

word_String = "1234567890店中美家馆小车大市公酒行国品发电金心业商司超生装园场食有新限天面工服海华水房饰城乐汽香部利子老艺花专东肉菜学福饭人百餐茶务通味所山区门药银农龙停尚安广鑫一容动南具源兴鲜记时机烤文康信果阳理锅宝达地儿衣特产西批坊州牛佳化五米修爱北养卖建材三会鸡室红站德王光名丽油院堂烧江社合星货型村自科快便日民营和活童明器烟育宾精屋经居庄石顺林尔县手厅销用好客火雅盛体旅之鞋辣作粉包楼校鱼平彩上吧保永万物教吃设医正造丰健点汤网庆技斯洗料配汇木缘加麻联卫川泰色世方寓风幼羊烫来高厂兰阿贝皮全女拉成云维贸道术运都口博河瑞宏京际路祥青镇厨培力惠连马鸿钢训影甲助窗布富牌头四多妆吉苑沙恒隆春干饼氏里二管诚制售嘉长轩杂副清计黄讯太鸭号街交与叉附近层旁对巷栋环省桥湖段乡厦府铺内侧元购前幢滨处向座下臬凤港开关景泉塘放昌线湾政步宁解白田町溪十八古双胜本单同九迎第台玉锦底后七斜期武岭松角纪朝峰六振珠局岗洲横边济井办汉代临弄团外塔杨铁浦字年岛陵原梅进荣友虹央桂沿事津凯莲丁秀柳集紫旗张谷的是不了很还个也这我就在以可到错没去过感次要比觉看得说常真们但最喜哈么别位能较境非为欢然他挺着价那意种想出员两推做排实分间甜度起满给热完格荐喝等其再几只现朋候样直而买于般豆量选奶打每评少算又因情找些份置适什蛋师气你姐棒试总定啊足级整带虾如态且尝主话强当更板知己无酸让入啦式笑赞片酱差像提队走嫩才刚午接重串回晚微周值费性桌拍跟块调糕"
#字体文件对应的字体顺序

for item in item_List:
    result={}
    result["shop_Url"]=item.xpath("./div[1]/a/@href")[0]#店铺网址
    result["shop_Img_Url"]=item.xpath("./div[1]/a/img/@data-src")[0]#店铺图片网址
    result["shop_Name"]=item.xpath("./div[1]/a/img/@title")[0]#店铺名称

    star_Class=item.xpath('.//*[@class="star_icon"]/span[1]/@class')[0]
    result["shop_Star"] = star_Class.split(' ')[1].split('_')[-1]#店铺评星等级

    result["comment_Url"]=item.xpath("./div[2]/div[2]/a[1]/@href")[0]#店铺评论网址
    
    #店铺评论条数
    comment_Class = item.xpath('./div[2]/div[2]/a[1]/b/svgmtsi[1]/@class')
    if comment_Class:
        class_Name = comment_Class[0]
        result["shop_Comment_Num"]="".join([get_Word(class_Name,"uni" + i.strip("*")) if (i.startswith('*') and i.endswith('*')) else i for i in item.xpath("./div[2]/div[2]/a[1]/b//text()")])
    else:
        result["shop_Comment_Num"]="".join(item.xpath("./div[2]/div[2]/a[1]/b//text()"))

    #店铺人均消费价格
    avgMoney_Class = item.xpath('./div[2]/div[2]/a[2]/b/svgmtsi[1]/@class')
    if avgMoney_Class:
        class_Name = avgMoney_Class[0]
        result["avgMoney"]=''.join([get_Word(class_Name,"uni" + i.strip("*")) if (i.startswith("*") and i.endswith("*")) else i for i in item.xpath("./div[2]/div[2]/a[2]/b//text()")])
    else:
        result["avgMoney"]="".join(item.xpath("./div[2]/div[2]/a[2]/b//text()"))

    #店铺种类
    shop_Type_Class = item.xpath('./div[2]/div[3]/a[1]/span/svgmtsi/@class')
    if shop_Type_Class:
        class_Name = shop_Type_Class[0]
        result["shopType"] =''.join([get_Word(class_Name,"uni" + i.strip("*")) if (i.startswith("*") and i.endswith("*")) else i for i in item.xpath("./div[2]/div[3]/a[1]/span//text()")])
    else:
        result["shopType"]="".join(item.xpath("./div[2]/div[3]/a[1]/span//text()"))
    
    #店铺位置
    location_Class = item.xpath("./div[2]/div[3]/a[2]/span/svgmtsi/@class")
    if location_Class:
        class_Name = location_Class[0]
        result['shop_location']=''.join([get_Word(class_Name,"uni"+i.strip("*")) if (i.startswith("*") and i.endswith("*")) else i for i in item.xpath("./div[2]/div[3]/a[2]/span//text()")])
    else:
        result['shop_location']="".join(item.xpath("./div[2]/div[3]/a[2]/span//text()"))
    
    #店铺团购优惠
    buy_Together = item.xpath("./div[3]/div//a/text()")
    for i in buy_Together:
        i = i.replace('\n',' ')
    result['buy_Together']=''.join(buy_Together)

    save(result)#保存结果
    print(result)
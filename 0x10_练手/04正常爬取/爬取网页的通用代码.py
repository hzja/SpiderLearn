import requests

def getHTMLText (url) :

    try :

        r = requests.get (url, timeout =30)
    
        r.raise_for_status ()  #如果状态不是200，引发HTTPError异常

        r.encoding = r.apparent_encoding

        return r.text

    except :

        return "产生异常"

if __name__ == "__main__":

    url = "https://www.icourse163.org/learn/BIT-1001870001?tid=1450316449#/learn/content?type=detail&id=1214620498&cid=1218397662"
    print (getHTMLText (url) )

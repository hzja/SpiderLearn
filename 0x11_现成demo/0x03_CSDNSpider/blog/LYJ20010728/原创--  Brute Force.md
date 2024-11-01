# 原创
：  Brute Force

# Brute Force

#### Brute Force

## Low

> 
题目源码


```
&lt;?php

if( isset( $_GET[ 'Login' ] ) ) {
    // Get username
    $user = $_GET[ 'username' ];

    // Get password
    $pass = $_GET[ 'password' ];
    $pass = md5( $pass );

    // Check the database
    $query  = "SELECT * FROM `users` WHERE user = '$user' AND password = '$pass';";
    $result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '&lt;pre&gt;' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '&lt;/pre&gt;' );

    if( $result &amp;&amp; mysqli_num_rows( $result ) == 1 ) {
        // Get users details
        $row    = mysqli_fetch_assoc( $result );
        $avatar = $row["avatar"];

        // Login successful
        echo "&lt;p&gt;Welcome to the password protected area {$user}&lt;/p&gt;";
        echo "&lt;img src=\"{$avatar}\" /&gt;";
    }
    else {
        // Login failed
        echo "&lt;pre&gt;&lt;br /&gt;Username and/or password incorrect.&lt;/pre&gt;";
    }

    ((is_null($___mysqli_res = mysqli_close($GLOBALS["___mysqli_ston"]))) ? false : $___mysqli_res);
}

?&gt;

```

> 
源码中暴露的问题：
- GET 登录不够安全，一般使用 POST 方式进行登录- 用户名和密码都没有进行过滤
利用burpsuite抓包爆破


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210608195536944.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210608195602540.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

## Medium

> 
题目源码


```
&lt;?php

if( isset( $_GET[ 'Login' ] ) ) {
    // Sanitise username input
    $user = $_GET[ 'username' ];
    $user = ((isset($GLOBALS["___mysqli_ston"]) &amp;&amp; is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $user ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));

    // Sanitise password input
    $pass = $_GET[ 'password' ];
    $pass = ((isset($GLOBALS["___mysqli_ston"]) &amp;&amp; is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $pass ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
    $pass = md5( $pass );

    // Check the database
    $query  = "SELECT * FROM `users` WHERE user = '$user' AND password = '$pass';";
    $result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '&lt;pre&gt;' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '&lt;/pre&gt;' );

    if( $result &amp;&amp; mysqli_num_rows( $result ) == 1 ) {
        // Get users details
        $row    = mysqli_fetch_assoc( $result );
        $avatar = $row["avatar"];

        // Login successful
        echo "&lt;p&gt;Welcome to the password protected area {$user}&lt;/p&gt;";
        echo "&lt;img src=\"{$avatar}\" /&gt;";
    }
    else {
        // Login failed
        sleep( 2 );
        echo "&lt;pre&gt;&lt;br /&gt;Username and/or password incorrect.&lt;/pre&gt;";
    }

    ((is_null($___mysqli_res = mysqli_close($GLOBALS["___mysqli_ston"]))) ? false : $___mysqli_res);
}

?&gt;

```

> 
源码中增加了一个函数`mysql_real_escape_string()`，其作用为转义SQL语句中使用的字符串中的特殊字符，包括`\x00,\n,\r,\,',",\x1a`，如果成功，则该函数返回被转义的字符串，如果失败，则返回 false


> 
源码中暴露的问题：
- 源码登录逻辑没有太大变化，登录失败会延时两秒，导致暴破速度会慢一些- 使用了mysqli_real_escape_string()函数对用户输入进行了过滤
利用burpsuite抓包爆破


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210608200734775.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210608200923719.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

## High

> 
题目源码


```
&lt;?php

if( isset( $_GET[ 'Login' ] ) ) {
    // Check Anti-CSRF token
    checkToken( $_REQUEST[ 'user_token' ], $_SESSION[ 'session_token' ], 'index.php' );

    // Sanitise username input
    $user = $_GET[ 'username' ];
    $user = stripslashes( $user );
    $user = ((isset($GLOBALS["___mysqli_ston"]) &amp;&amp; is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $user ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));

    // Sanitise password input
    $pass = $_GET[ 'password' ];
    $pass = stripslashes( $pass );
    $pass = ((isset($GLOBALS["___mysqli_ston"]) &amp;&amp; is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $pass ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
    $pass = md5( $pass );

    // Check database
    $query  = "SELECT * FROM `users` WHERE user = '$user' AND password = '$pass';";
    $result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '&lt;pre&gt;' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '&lt;/pre&gt;' );

    if( $result &amp;&amp; mysqli_num_rows( $result ) == 1 ) {
        // Get users details
        $row    = mysqli_fetch_assoc( $result );
        $avatar = $row["avatar"];

        // Login successful
        echo "&lt;p&gt;Welcome to the password protected area {$user}&lt;/p&gt;";
        echo "&lt;img src=\"{$avatar}\" /&gt;";
    }
    else {
        // Login failed
        sleep( rand( 0, 3 ) );
        echo "&lt;pre&gt;&lt;br /&gt;Username and/or password incorrect.&lt;/pre&gt;";
    }

    ((is_null($___mysqli_res = mysqli_close($GLOBALS["___mysqli_ston"]))) ? false : $___mysqli_res);
}

// Generate Anti-CSRF token
generateSessionToken();

?&gt;

```

> 
增加的函数


```
mysqli_real_escape_string(connection,escapestring);	//转义字符串中的特殊字符
stripslashes(string)	// 删除字符串中的反斜杠
checkToken( $_REQUEST[ 'user_token' ], $_SESSION[ 'session_token' ], 'index.php' );// 增加了token的检测，token的值来源于index.php

```

> 



<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210608203019682.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210608203025272.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2021060820303176.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210608203038252.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210608203122256.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

## Impossible

> 
题目源码


```
&lt;?php

if( isset( $_POST[ 'Login' ] ) &amp;&amp; isset ($_POST['username']) &amp;&amp; isset ($_POST['password']) ) {
    // Check Anti-CSRF token
    checkToken( $_REQUEST[ 'user_token' ], $_SESSION[ 'session_token' ], 'index.php' );

    // Sanitise username input
    $user = $_POST[ 'username' ];
    $user = stripslashes( $user );
    $user = ((isset($GLOBALS["___mysqli_ston"]) &amp;&amp; is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $user ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));

    // Sanitise password input
    $pass = $_POST[ 'password' ];
    $pass = stripslashes( $pass );
    $pass = ((isset($GLOBALS["___mysqli_ston"]) &amp;&amp; is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $pass ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
    $pass = md5( $pass );

    // Default values
    $total_failed_login = 3;
    $lockout_time       = 15;
    $account_locked     = false;

    // Check the database (Check user information)
    $data = $db-&gt;prepare( 'SELECT failed_login, last_login FROM users WHERE user = (:user) LIMIT 1;' );
    $data-&gt;bindParam( ':user', $user, PDO::PARAM_STR );
    $data-&gt;execute();
    $row = $data-&gt;fetch();

    // Check to see if the user has been locked out.
    if( ( $data-&gt;rowCount() == 1 ) &amp;&amp; ( $row[ 'failed_login' ] &gt;= $total_failed_login ) )  {
        // User locked out.  Note, using this method would allow for user enumeration!
        //echo "&lt;pre&gt;&lt;br /&gt;This account has been locked due to too many incorrect logins.&lt;/pre&gt;";

        // Calculate when the user would be allowed to login again
        $last_login = strtotime( $row[ 'last_login' ] );
        $timeout    = $last_login + ($lockout_time * 60);
        $timenow    = time();

        /*
        print "The last login was: " . date ("h:i:s", $last_login) . "&lt;br /&gt;";
        print "The timenow is: " . date ("h:i:s", $timenow) . "&lt;br /&gt;";
        print "The timeout is: " . date ("h:i:s", $timeout) . "&lt;br /&gt;";
        */

        // Check to see if enough time has passed, if it hasn't locked the account
        if( $timenow &lt; $timeout ) {
            $account_locked = true;
            // print "The account is locked&lt;br /&gt;";
        }
    }

    // Check the database (if username matches the password)
    $data = $db-&gt;prepare( 'SELECT * FROM users WHERE user = (:user) AND password = (:password) LIMIT 1;' );
    $data-&gt;bindParam( ':user', $user, PDO::PARAM_STR);
    $data-&gt;bindParam( ':password', $pass, PDO::PARAM_STR );
    $data-&gt;execute();
    $row = $data-&gt;fetch();

    // If its a valid login...
    if( ( $data-&gt;rowCount() == 1 ) &amp;&amp; ( $account_locked == false ) ) {
        // Get users details
        $avatar       = $row[ 'avatar' ];
        $failed_login = $row[ 'failed_login' ];
        $last_login   = $row[ 'last_login' ];

        // Login successful
        echo "&lt;p&gt;Welcome to the password protected area &lt;em&gt;{$user}&lt;/em&gt;&lt;/p&gt;";
        echo "&lt;img src=\"{$avatar}\" /&gt;";

        // Had the account been locked out since last login?
        if( $failed_login &gt;= $total_failed_login ) {
            echo "&lt;p&gt;&lt;em&gt;Warning&lt;/em&gt;: Someone might of been brute forcing your account.&lt;/p&gt;";
            echo "&lt;p&gt;Number of login attempts: &lt;em&gt;{$failed_login}&lt;/em&gt;.&lt;br /&gt;Last login attempt was at: &lt;em&gt;${last_login}&lt;/em&gt;.&lt;/p&gt;";
        }

        // Reset bad login count
        $data = $db-&gt;prepare( 'UPDATE users SET failed_login = "0" WHERE user = (:user) LIMIT 1;' );
        $data-&gt;bindParam( ':user', $user, PDO::PARAM_STR );
        $data-&gt;execute();
    } else {
        // Login failed
        sleep( rand( 2, 4 ) );

        // Give the user some feedback
        echo "&lt;pre&gt;&lt;br /&gt;Username and/or password incorrect.&lt;br /&gt;&lt;br/&gt;Alternative, the account has been locked because of too many failed logins.&lt;br /&gt;If this is the case, &lt;em&gt;please try again in {$lockout_time} minutes&lt;/em&gt;.&lt;/pre&gt;";

        // Update bad login count
        $data = $db-&gt;prepare( 'UPDATE users SET failed_login = (failed_login + 1) WHERE user = (:user) LIMIT 1;' );
        $data-&gt;bindParam( ':user', $user, PDO::PARAM_STR );
        $data-&gt;execute();
    }

    // Set the last login time
    $data = $db-&gt;prepare( 'UPDATE users SET last_login = now() WHERE user = (:user) LIMIT 1;' );
    $data-&gt;bindParam( ':user', $user, PDO::PARAM_STR );
    $data-&gt;execute();
}

// Generate Anti-CSRF token
generateSessionToken();

?&gt;

```

> 
源码分析：



> 
防护总结：



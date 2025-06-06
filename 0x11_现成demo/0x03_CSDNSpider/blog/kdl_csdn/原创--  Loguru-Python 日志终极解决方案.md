# 原创
：  Loguru：Python 日志终极解决方案

# Loguru：Python 日志终极解决方案

> 
关注微信公众号：K哥爬虫，QQ交流群：808574309，持续分享爬虫进阶、JS/安卓逆向等技术干货！


### 日志的重要性

日志的作用非常重要，日志可以记录用户的操作、程序的异常，还可以为数据分析提供依据，日志的存在意义就是为了能够在程序在运行过程中记录错误，方便维护和调试，能够快速定位出错的地方，减少维护成本。每个程序员都应该知道，不是为了记录日志而记录日志，日志也不是随意记的。要实现能够只通过日志文件还原整个程序执行的过程，达到能透明地看到程序里执行情况，每个线程、每个过程到底执行到哪的目的。日志就像飞机的黑匣子一样，应当能够复原异常的整个现场乃至细节！

### 常见日志记录方式

#### print()

最常见的是把输出函数 `print()` 当作日志记录的方式，直接打印各种提示信息，常见于个人练习项目里，通常是懒得单独配置日志，而且项目太小不需要日志信息，不需要上线，不需要持续运行，完整的项目不推荐直接打印日志信息，现实中也几乎没有人这么做。

#### 自写模板

我们可以在不少小项目里面看到作者自己写了一个日志模板，通常利用 `print()` 或者 `sys.stdout` 稍微封装一下即可实现简单的日志输出，这里的 `sys.stdout` 是 Python 中的标准输出流，`print()` 函数是对 `sys.stdout` 的高级封装，当我们在 Python 中打印对象调用 `print(obj)` 时候，事实上是调用了 `sys.stdout.write(obj+'\n')`，`print()` 将内容打印到了控制台，然后追加了一个换行符 `\n`。

自写日志模板适合比较小的项目，可以按照自己的喜好编写模板，不需要太多复杂配置，方便快捷，但是这种记录日志的方式并不是很规范，有可能你自己觉得阅读体验不错，但是别人在接触你的项目的时候往往需要花费一定的时间去学习日志的逻辑、格式、输出方式等，比较大的项目同样不推荐这种方法。

一个简单的自写日志模板举例：

日志模板 log.py：

```
import sys
import traceback
import datetime


def getnowtime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _log(content, level, *args):
    sys.stdout.write("%s - %s - %s\n" % (getnowtime(), level, content))
    for arg in args:
        sys.stdout.write("%s\n" % arg)


def debug(content, *args):
    _log(content, 'DEBUG', *args)


def info(content, *args):
    _log(content, 'INFO', *args)


def warn(content, *args):
    _log(content, 'WARN', *args)


def error(content, *args):
    _log(content, 'ERROR', *args)


def exception(content):
    sys.stdout.write("%s - %s\n" % (getnowtime(), content))
    traceback.print_exc(file=sys.stdout)

```

调用日志模块：

```
import log


log.info("This is log info!")
log.warn("This is log warn!")
log.error("This is log error!")
log.debug("This is log debug!")

people_info = {"name": "Bob", "age": 20}

try:
    gender = people_info["gender"]
except Exception as error:
    log.exception(error)

```

日志输出：

```
2021-10-19 09:50:58 - INFO - This is log info!
2021-10-19 09:50:58 - WARN - This is log warn!
2021-10-19 09:50:58 - ERROR - This is log error!
2021-10-19 09:50:58 - DEBUG - This is log debug!
2021-10-19 09:50:58 - 'gender'
Traceback (most recent call last):
  File "D:/python3Project/test.py", line 18, in &lt;module&gt;
    gender = people_info["gender"]
KeyError: 'gender'

```

#### Logging

在一个完整的项目中，大多数人都会引入专门的日志记录库，而 Python 自带的标准库 logging 就是专门为日志记录而生的，logging 模块定义的函数和类为应用程序和库的开发实现了一个灵活的事件日志系统。由标准库模块提供日志记录 API 的关键好处是所有 Python 模块都可以使用这个日志记录功能。所以，你的应用日志可以将你自己的日志信息与来自第三方模块的信息整合起来。

logging 模块虽然强大，但是其配置也是比较繁琐的，在大型项目中通常需要单独初始化日志、配置日志格式等等，K哥在日常使用中通常都会对 logging 做如下的封装写法，使日志可以按天保存，保留15天的日志，可以配置是否输出到控制台和文件，如下所示：

```
# 实现按天分割保留日志


import os
import sys
import logging
from logging import handlers


PARENT_DIR = os.path.split(os.path.realpath(__file__))[0]  # 父目录
LOGGING_DIR = os.path.join(PARENT_DIR, "log")              # 日志目录
LOGGING_NAME = "test"                                      # 日志文件名

LOGGING_TO_FILE = True                                     # 日志输出文件
LOGGING_TO_CONSOLE = True                                  # 日志输出到控制台

LOGGING_WHEN = 'D'                                         # 日志文件切分维度
LOGGING_INTERVAL = 1                                       # 间隔少个 when 后，自动重建文件
LOGGING_BACKUP_COUNT = 15                                  # 日志保留个数，0 保留所有日志
LOGGING_LEVEL = logging.DEBUG                              # 日志等级
LOGGING_suffix = "%Y.%m.%d.log"                            # 旧日志文件名

# 日志输出格式
LOGGING_FORMATTER = "%(levelname)s - %(asctime)s - process:%(process)d - %(filename)s - %(name)s - line:%(lineno)d - %(module)s - %(message)s"


def logging_init():
    if not os.path.exists(LOGGING_DIR):
        os.makedirs(LOGGING_DIR)
    logger = logging.getLogger()
    logger.setLevel(LOGGING_LEVEL)
    formatter = logging.Formatter(LOGGING_FORMATTER)

    if LOGGING_TO_FILE:
        file_handler = handlers.TimedRotatingFileHandler(filename=os.path.join(LOGGING_DIR, LOGGING_NAME), when=LOGGING_WHEN, interval=LOGGING_INTERVAL, backupCount=LOGGING_BACKUP_COUNT)
        file_handler.suffix = LOGGING_suffix
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    if LOGGING_TO_CONSOLE:
        stream_handler = logging.StreamHandler(sys.stderr)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)


def logging_test():
    logging.info("This is log info!")
    logging.warning("This is log warn!")
    logging.error("This is log error!")
    logging.debug("This is log debug!")
    people_info = {"name": "Bob", "age": 20}

    try:
        gender = people_info["gender"]
    except Exception as error:
        logging.exception(error)


if __name__ == "__main__":
    logging_init()
    logging_test()

```

输出日志：

```
INFO - 2021-10-19 11:28:10,103 - process:15144 - test.py - root - line:52 - test - This is log info!
WARNING - 2021-10-19 11:28:10,105 - process:15144 - test.py - root - line:53 - test - This is log warn!
ERROR - 2021-10-19 11:28:10,105 - process:15144 - test.py - root - line:54 - test - This is log error!
DEBUG - 2021-10-19 11:28:10,105 - process:15144 - test.py - root - line:55 - test - This is log debug!
ERROR - 2021-10-19 11:28:10,105 - process:15144 - test.py - root - line:61 - test - 'gender'
Traceback (most recent call last):
  File "D:/python3Project/test.py", line 59, in logging_test
    gender = people_info["gender"]
KeyError: 'gender'

```

它在控制台中是这样的：

当然，如果你不需要很复杂的功能，希望简洁一点，仅仅需要在控制台输出一下日志的话，也可以只进行简单的配置：

```
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger()

```

### 更优雅的解决方案：Loguru

对于 logging 模块，即便是简单的使用，也需要自己定义格式，这里介绍一个更加优雅、高效、简洁的第三方模块：loguru，官方的介绍是：Loguru is a library which aims to bring enjoyable logging in Python. Loguru 旨在为 Python 带来愉快的日志记录。这里引用官方的一个 GIF 来快速演示其功能：

#### 安装

Loguru 仅支持 Python 3.5 及以上的版本，使用 pip 安装即可：

```
pip install loguru

```

#### 开箱即用

Loguru 的主要概念是只有一个：logger

```
from loguru import logger

logger.info("This is log info!")
logger.warning("This is log warn!")
logger.error("This is log error!")
logger.debug("This is log debug!")

```

控制台输出：

可以看到不需要手动设置，Loguru 会提前配置一些基础信息，自动输出时间、日志级别、模块名、行号等信息，而且根据等级的不同，还自动设置了不同的颜色，方便观察，真正做到了开箱即用！

#### add() / remove()

如果想自定义日志级别，自定义日志格式，保存日志到文件该怎么办？与 logging 模块不同，不需要 Handler，不需要 Formatter，只需要一个 `add()` 函数就可以了，例如我们想把日志储存到文件：

```
from loguru import logger

logger.add('test.log')
logger.debug('this is a debug')

```

我们不需要像 logging 模块一样再声明一个 FileHandler 了，就一行 `add()` 语句搞定，运行之后会发现目录下 test.log 里面同样出现了刚刚控制台输出的 debug 信息。

与 `add()` 语句相反，`remove()` 语句可以删除我们添加的配置：

```
from loguru import logger

log_file = logger.add('test.log')
logger.debug('This is log debug!')
logger.remove(log_file)
logger.debug('This is another log debug!')

```

此时控制台会输出两条 debug 信息：

```
2021-10-19 13:53:36.610 | DEBUG    | __main__:&lt;module&gt;:86 - This is log debug!
2021-10-19 13:53:36.611 | DEBUG    | __main__:&lt;module&gt;:88 - This is another log debug!

```

而 test.log 日志文件里面只有一条 debug 信息，原因就在于我们在第二条 debug 语句之前使用了 `remove()` 语句。

#### 完整参数

Loguru 对输出到文件的配置有非常强大的支持，比如支持输出到多个文件，分级别分别输出，过大创建新文件，过久自动删除等等。 下面我们来详细看一下 `add()` 语句的详细参数：

基本语法：

```
add(sink, *, level='DEBUG', format='&lt;green&gt;{time:YYYY-MM-DD HH:mm:ss.SSS}&lt;/green&gt; | &lt;level&gt;{level: &lt;8}&lt;/level&gt; | &lt;cyan&gt;{name}&lt;/cyan&gt;:&lt;cyan&gt;{function}&lt;/cyan&gt;:&lt;cyan&gt;{line}&lt;/cyan&gt; - &lt;level&gt;{message}&lt;/level&gt;', filter=None, colorize=None, serialize=False, backtrace=True, diagnose=True, enqueue=False, catch=True, **kwargs)

```

基本参数释义：

当且仅当 sink 是协程函数时，以下参数适用：

当且仅当 sink 是文件路径时，以下参数适用：

这么多参数可以见识到 `add()` 函数的强大之处，仅仅一个函数就能实现 logging 模块的诸多功能，接下来介绍几个比较常用的方法。

#### rotation 日志文件分隔

`add()` 函数的 rotation 参数，可以实现按照固定时间创建新的日志文件，比如设置每天 0 点新创建一个 log 文件：

```
logger.add('runtime_{time}.log', rotation='00:00')

```

设置超过 500 MB 新创建一个 log 文件：

```
logger.add('runtime_{time}.log', rotation="500 MB")

```

设置每隔一个周新创建一个 log 文件：

```
logger.add('runtime_{time}.log', rotation='1 week')

```

#### retention 日志保留时间

`add()` 函数的 retention 参数，可以设置日志的最长保留时间，比如设置日志文件最长保留 15 天：

```
logger.add('runtime_{time}.log', retention='15 days')

```

设置日志文件最多保留 10 个：

```
logger.add('runtime_{time}.log', retention=10)

```

也可以是一个 `datetime.timedelta` 对象，比如设置日志文件最多保留 5 个小时：

```
import datetime
from loguru import logger

logger.add('runtime_{time}.log', retention=datetime.timedelta(hours=5))

```

#### compression 日志压缩格式

`add()` 函数的 compression 参数，可以配置日志文件的压缩格式，这样可以更加节省存储空间，比如设置使用 zip 文件格式保存：

```
logger.add('runtime_{time}.log', compression='zip')

```

其格式支持：`gz`、`bz2`、`xz`、`lzma`、`tar`、`tar.gz`、`tar.bz2`、`tar.xz`

#### 字符串格式化

Loguru 在输出 log 的时候还提供了非常友好的字符串格式化功能，相当于 `str.format()`：

```
logger.info('If you are using Python {}, prefer {feature} of course!', 3.6, feature='f-strings')

```

输出：

```
2021-10-19 14:59:06.412 | INFO     | __main__:&lt;module&gt;:3 - If you are using Python 3.6, prefer f-strings of course!

```

#### 异常追溯

在 Loguru 里可以直接使用它提供的装饰器就可以直接进行异常捕获，而且得到的日志是无比详细的：

```
from loguru import logger


@logger.catch
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)


my_function(0, 0, 0)

```

日志输出：

```
2021-10-19 15:04:51.675 | ERROR    | __main__:&lt;module&gt;:10 - An error has been caught in function '&lt;module&gt;', process 'MainProcess' (30456), thread 'MainThread' (26268):
Traceback (most recent call last):

&gt; File "D:/python3Project\test.py", line 10, in &lt;module&gt;
    my_function(0, 0, 0)
    └ &lt;function my_function at 0x014CDFA8&gt;

  File "D:/python3Project\test.py", line 7, in my_function
    return 1 / (x + y + z)
                │   │   └ 0
                │   └ 0
                └ 0

ZeroDivisionError: division by zero

```

在控制台的输出是这样的：

相比 Logging，Loguru 无论是在配置方面、日志输出样式还是异常追踪，都远优于 Logging，使用 Loguru 无疑能提升开发人员效率。本文仅介绍了一些常用的方法，想要详细了解可参考 [Loguru 官方文档](https://loguru.readthedocs.io/)或关注 [Loguru GitHub](https://github.com/Delgan/loguru)。

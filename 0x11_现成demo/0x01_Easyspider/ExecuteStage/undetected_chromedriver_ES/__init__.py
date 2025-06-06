#!/usr/bin/env python3

"""

         888                                                  888         d8b
         888                                                  888         Y8P
         888                                                  888
 .d8888b 88888b.  888d888 .d88b.  88888b.d88b.   .d88b.   .d88888 888d888 888 888  888  .d88b.  888d888
d88P"    888 "88b 888P"  d88""88b 888 "888 "88b d8P  Y8b d88" 888 888P"   888 888  888 d8P  Y8b 888P"
888      888  888 888    888  888 888  888  888 88888888 888  888 888     888 Y88  88P 88888888 888
Y88b.    888  888 888    Y88..88P 888  888  888 Y8b.     Y88b 888 888     888  Y8bd8P  Y8b.     888
 "Y8888P 888  888 888     "Y88P"  888  888  888  "Y8888   "Y88888 888     888   Y88P    "Y8888  888   88888888

by UltrafunkAmsterdam (https://github.com/ultrafunkamsterdam)

"""
from __future__ import annotations


__version__ = "3.4.7"

import json
import logging
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from weakref import finalize

import selenium.webdriver.chrome.service
import selenium.webdriver.chrome.webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.common.service
import selenium.webdriver.remote.command
import selenium.webdriver.remote.webdriver

from .cdp import CDP
from .dprocess import start_detached
from .options import ChromeOptions
from .patcher import IS_POSIX
from .patcher import Patcher
from .reactor import Reactor
from .webelement import UCWebElement
from .webelement import WebElement


__all__ = (
    "Chrome",
    "ChromeOptions",
    "Patcher",
    "Reactor",
    "CDP",
    "find_chrome_executable",
)
# 这段代码定义了一个名为`__all__`的元组，其中包含6个字符串，分别是`Chrome`、`ChromeOptions`、`Patcher`、`Reactor`、`CDP`和`find_chrome_executable`。这意味着这些名字是模块中所有公开对象的名称，其他模块可以通过导入它们来使用这些对象。

logger = logging.getLogger("uc")
logger.setLevel(logging.getLogger().getEffectiveLevel())
# 这段代码的主要功能是设置一个名为 "uc" 的日志记录器的日志级别。
# 1. `logging.getLogger("uc")`：这行代码创建了一个名为 "uc" 的日志记录器。`logging.getLogger()` 函数是 Python 的日志模块提供的，用于获取一个日志记录器对象。这里传入参数 "uc"，表示要创建一个名为 "uc" 的日志记录器。
# 2. `logger.setLevel(logging.getLogger().getEffectiveLevel())`：这行代码设置了 "uc" 日志记录器的日志级别。`logger.setLevel()` 函数是日志记录器对象提供的方法，用于设置日志记录器的日志级别。
#   `logging.getLogger().getEffectiveLevel()`：这行代码获取当前全局日志记录器的有效日志级别。`logging.getLogger()` 函数是 Python 的日志模块提供的，用于获取全局日志记录器对象。`getEffectiveLevel()` 方法是全局日志记录器对象提供的方法，用于获取当前全局日志记录器的有效日志级别。
#   这样，`logger.setLevel(logging.getLogger().getEffectiveLevel())` 这行代码的意思是：将 "uc" 日志记录器的日志级别设置为当前全局日志记录器的有效日志级别。

class Chrome(selenium.webdriver.chrome.webdriver.WebDriver):
    """

    Controls the ChromeDriver and allows you to drive the browser.

    The webdriver file will be downloaded by this module automatically,
    you do not need to specify this. however, you may if you wish.

    Attributes
    ----------

    Methods
    -------

    reconnect()

        this can be useful in case of heavy detection methods
        -stops the chromedriver service which runs in the background
        -starts the chromedriver service which runs in the background
        -recreate session


    start_session(capabilities=None, browser_profile=None)

        differentiates from the regular method in that it does not
        require a capabilities argument. The capabilities are automatically
        recreated from the options at creation time.

    --------------------------------------------------------------------------
        NOTE:
            Chrome has everything included to work out of the box.
            it does not `need` customizations.
            any customizations MAY lead to trigger bot migitation systems.

    --------------------------------------------------------------------------
    """

    _instances = set()
    session_id = None
    debug = False
#     这段代码定义了一个名为`MyClass`的类，其中包含三个属性：`_instances`、`session_id`和`debug`。
# 1. `_instances`：这是一个内部属性，用于存储该类的所有实例。这里使用`set`类型，因为它可以存储唯一的元素，并且可以更快地执行集合操作。
# 2. `session_id`：这是一个类属性，表示当前实例的会话ID。它被初始化为`None`，但在后续代码中可能被更新。
# 3. `debug`：这是一个类属性，表示当前实例的调试模式。它被初始化为`False`，但在后续代码中可能被更改为`True`或`False`。

    def __init__(
        self,
        options=None,
        user_data_dir=None,
        driver_executable_path=None,
        browser_executable_path=None,
        port=0,
        enable_cdp_events=False,
        service_args=None,
        service_creationflags=None,
        desired_capabilities=None,
        advanced_elements=False,
        service_log_path=None,
        keep_alive=True,
        log_level=0,
        headless=False,
        version_main=None,
        patcher_force_close=False,
        suppress_welcome=True,
        use_subprocess=True,
        debug=False,
        no_sandbox=True,
        user_multi_procs: bool = False,
        **kw,
    ):
        # 这是一个Python函数的定义，用于初始化一个WebDriver对象。函数的参数包括：
        # 1. `options`：可选参数，用于配置WebDriver的行为。
        # 2. `user_data_dir`：用户数据目录，用于存储浏览器数据。
        # 3. `driver_executable_path`：驱动程序的可执行文件路径。
        # 4. `browser_executable_path`：浏览器可执行文件路径。
        # 5. `port`：用于WebDriver与浏览器通信的端口号。
        # 6. `enable_cdp_events`：是否启用控制台事件。
        # 7. `service_args`：服务参数。
        # 8. `service_creationflags`：服务创建标志。
        # 9. `desired_capabilities`：期望功能。
        # 10. `advanced_elements`：是否启用高级元素。
        # 11. `service_log_path`：服务日志路径。
        # 12. `keep_alive`：是否保持活动状态。
        # 13. `log_level`：日志级别。
        # 14. `headless`：是否启用无头模式。
        # 15. `version_main`：主要版本号。
        # 16. `patcher_force_close`：是否强制关闭修补程序。
        # 17. `suppress_welcome`：是否 suppress欢迎信息。
        # 18. `use_subprocess`：是否使用子进程。
        # 19. `debug`：是否启用调试模式。
        # 20. `no_sandbox`：是否禁用沙箱。
        # 21. `user_multi_procs`：是否允许用户多进程。
        # 22. `**kw`：其他关键字参数。

        """
        Creates a new instance of the chrome driver.

        Starts the service and then creates new instance of chrome driver.

        Parameters
        ----------

        options: ChromeOptions, optional, default: None - automatic useful defaults
            this takes an instance of ChromeOptions, mainly to customize browser behavior.
            anything other dan the default, for example extensions or startup options
            are not supported in case of failure, and can probably lowers your undetectability.


        user_data_dir: str , optional, default: None (creates temp profile)
            if user_data_dir is a path to a valid chrome profile directory, use it,
            and turn off automatic removal mechanism at exit.

        driver_executable_path: str, optional, default: None(=downloads and patches new binary)

        browser_executable_path: str, optional, default: None - use find_chrome_executable
            Path to the browser executable.
            If not specified, make sure the executable's folder is in $PATH

        port: int, optional, default: 0
            port to be used by the chromedriver executable, this is NOT the debugger port.
            leave it at 0 unless you know what you are doing.
            the default value of 0 automatically picks an available port.

        enable_cdp_events: bool, default: False
            :: currently for chrome only
            this enables the handling of wire messages
            when enabled, you can subscribe to CDP events by using:

                driver.add_cdp_listener("Network.dataReceived", yourcallback)
                # yourcallback is an callable which accepts exactly 1 dict as parameter


        service_args: list of str, optional, default: None
            arguments to pass to the driver service

        desired_capabilities: dict, optional, default: None - auto from config
            Dictionary object with non-browser specific capabilities only, such as "item" or "loggingPref".

        advanced_elements:  bool, optional, default: False
            makes it easier to recognize elements like you know them from html/browser inspection, especially when working
            in an interactive environment

            default webelement repr:
            <selenium.webdriver.remote.webelement.WebElement (session="85ff0f671512fa535630e71ee951b1f2", element="6357cb55-92c3-4c0f-9416-b174f9c1b8c4")>

            advanced webelement repr
            <WebElement(<a class="mobile-show-inline-block mc-update-infos init-ok" href="#" id="main-cat-switcher-mobile">)>

            note: when retrieving large amounts of elements ( example: find_elements_by_tag("*") ) and print them, it does take a little more time.


        service_log_path: str, optional, default: None
             path to log information from the driver.

        keep_alive: bool, optional, default: True
             Whether to configure ChromeRemoteConnection to use HTTP keep-alive.

        log_level: int, optional, default: adapts to python global log level

        headless: bool, optional, default: False
            can also be specified in the options instance.
            Specify whether you want to use the browser in headless mode.
            warning: this lowers undetectability and not fully supported.

        version_main: int, optional, default: None (=auto)
            if you, for god knows whatever reason, use
            an older version of Chrome. You can specify it's full rounded version number
            here. Example: 87 for all versions of 87

        patcher_force_close: bool, optional, default: False
            instructs the patcher to do whatever it can to access the chromedriver binary
            if the file is locked, it will force shutdown all instances.
            setting it is not recommended, unless you know the implications and think
            you might need it.

        suppress_welcome: bool, optional , default: True
            a "welcome" alert might show up on *nix-like systems asking whether you want to set
            chrome as your default browser, and if you want to send even more data to google.
            now, in case you are nag-fetishist, or a diagnostics data feeder to google, you can set this to False.
            Note: if you don't handle the nag screen in time, the browser loses it's connection and throws an Exception.

        use_subprocess: bool, optional , default: True,

            False (the default) makes sure Chrome will get it's own process (so no subprocess of chromedriver.exe or python
                This fixes a LOT of issues, like multithreaded run, but mst importantly. shutting corectly after
                program exits or using .quit()
                you should be knowing what you're doing, and know how python works.

              unfortunately, there  is always an edge case in which one would like to write an single script with the only contents being:
              --start script--
              import undetected_chromedriver as uc
              d = uc.Chrome()
              d.get('https://somesite/')
              ---end script --

              and will be greeted with an error, since the program exists before chrome has a change to launch.
              in that case you can set this to `True`. The browser will start via subprocess, and will keep running most of times.
              ! setting it to True comes with NO support when being detected. !

        no_sandbox: bool, optional, default=True
             uses the --no-sandbox option, and additionally does suppress the "unsecure option" status bar
             this option has a default of True since many people seem to run this as root (....) , and chrome does not start
             when running as root without using --no-sandbox flag.

        user_multi_procs:
            set to true when you are using multithreads/multiprocessing
            ensures not all processes are trying to modify a binary which is in use by another.
            for this to work. YOU MUST HAVE AT LEAST 1 UNDETECTED_CHROMEDRIVER BINARY IN YOUR ROAMING DATA FOLDER.
            this requirement can be easily satisfied, by just running this program "normal" and close/kill it.


        """

        finalize(self, self._ensure_close, self)
        self.debug = debug
        self.patcher = Patcher(
            executable_path=driver_executable_path,
            force=patcher_force_close,
            version_main=version_main,
            user_multi_procs=user_multi_procs,
        )
        # 这段代码是在Python中定义一个类的方法。首先，它调用了一个名为`finalize`的函数，该函数接受三个参数：`self`（表示类实例本身），`self._ensure_close`（表示一个方法），以及`self`（表示类实例本身）。这个`finalize`函数可能用于确保类实例在方法调用完毕后正确关闭。
        # 接下来，代码设置了类实例的`debug`属性，将其值设置为`debug`。然后，它创建了一个名为`patcher`的新实例，该实例是一个名为`Patcher`的类的新实例。这个`Patcher`类可能用于处理与浏览器驱动程序相关的操作。
        # 在创建`patcher`实例时，代码传递了五个参数：`executable_path`（表示浏览器驱动程序的可执行文件路径）、`force`（表示是否强制关闭浏览器驱动程序）、`version_main`（表示浏览器驱动程序的主要版本号）和`user_multi_procs`（表示用户是否允许多进程）。这些参数将用于配置`Patcher`实例的行为。

        # self.patcher.auto(user_multiprocess = user_multi_num_procs)
        chrome_version = self.patcher.auto()
        # self.patcher = patcher
        if not options:
            options = ChromeOptions()
        # 这段代码的主要功能是获取Chrome浏览器的版本信息，并初始化一个ChromeOptions对象。以下是代码的详细解释：
        # 1. `chrome_version = self.patcher.auto()`：这行代码调用Patcher对象的`auto()`方法来获取Chrome浏览器的版本信息，并将结果存储在`chrome_version`变量中。`self.patcher`是一个Patcher对象，用于与Chrome浏览器进行交互。
        # 2. `if not options:`：这是一个条件语句，检查`options`是否为空。如果`options`为空，那么执行下面的代码。
        # 3. `options = ChromeOptions()`：如果`options`为空，那么这行代码创建一个新的ChromeOptions对象，并将其赋值给`options`变量。ChromeOptions对象用于配置和定制Chrome浏览器的各种设置。
        # 总之，这段代码的主要目的是获取Chrome浏览器的版本信息，并根据需要初始化一个ChromeOptions对象。

        try:
            if hasattr(options, "_session") and options._session is not None:
                #  prevent reuse of options,
                #  as it just appends arguments, not replace them
                #  you'll get conflicts starting chrome
                raise RuntimeError("you cannot reuse the ChromeOptions object")
        except AttributeError:
            pass
        # 这段代码是Python中的try-except语句，用于处理可能发生的异常。以下是代码的详细解释：
        # 1. `try`：表示开始尝试执行下面的代码块。
        # 2. `if hasattr(options, "_session") and options._session is not None:`：检查options对象是否具有名为"_session"的属性，并且该属性的值不为None。这是为了确保在调用此代码之前，options对象没有被使用过。
        # 3. `raise RuntimeError("you cannot reuse the ChromeOptions object")`：如果条件为真，则抛出一个名为"RuntimeError"的异常，并附带一条消息："you cannot reuse the ChromeOptions object"。这条消息表示不能重复使用ChromeOptions对象，因为它只是追加参数，而不是替换它们，这可能导致Chrome浏览器出现问题。
        # 4. `except AttributeError:`：表示尝试处理可能发生的AttributeError异常。这个异常通常发生在尝试访问不存在的属性时。
        # 5. `pass`：表示什么都不做，只是跳过当前异常。
        # 总之，这段代码的作用是检查ChromeOptions对象是否已经被使用过，如果已经被使用过，则抛出一个异常，防止再次使用该对象。

        options._session = self
        # 这段代码是Python中的一个赋值操作，将对象的`_session`属性设置为对象本身（即`self`）。这里的`options`是一个对象，`self`同样也是一个对象，`_session`是`options`对象的属性。通过这个赋值操作，`options`对象现在可以访问到`self`对象，从而实现两个对象之间的交互。

        if not options.debugger_address:
            debug_port = (
                port
                if port != 0
                else selenium.webdriver.common.service.utils.free_port()
            )
            debug_host = "127.0.0.1"
            options.debugger_address = "%s:%d" % (debug_host, debug_port)
        else:
            debug_host, debug_port = options.debugger_address.split(":")
            debug_port = int(debug_port)
        # 这段代码的主要功能是设置Selenium WebDriver的调试地址和端口。首先，它会检查options.debugger_address是否为空。如果是，它会计算一个可用的端口（如果port为0，则使用selenium.webdriver.common.service.utils.free_port()函数获取一个可用的端口）并将其设置为debug_port。然后，将调试主机设置为"127.0.0.1"，并将options.debugger_address设置为"%s:%d" % (debug_host, debug_port)。
        # 如果options.debugger_address不为空，它会将options.debugger_address拆分为调试主机和端口，并将端口转换为整数。

        if enable_cdp_events:
            options.set_capability(
                "goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"}
            )

        options.add_argument("--remote-debugging-host=%s" % debug_host)
        options.add_argument("--remote-debugging-port=%s" % debug_port)

        if user_data_dir:
            options.add_argument("--user-data-dir=%s" % user_data_dir)

        language, keep_user_data_dir = None, bool(user_data_dir)

        # see if a custom user profile is specified in options
        for arg in options.arguments:

            if any([_ in arg for _ in ("--headless", "headless")]):
                options.arguments.remove(arg)
                options.headless = True

            if "lang" in arg:
                m = re.search("(?:--)?lang(?:[ =])?(.*)", arg)
                try:
                    language = m[1]
                except IndexError:
                    logger.debug("will set the language to en-US,en;q=0.9")
                    language = "en-US,en;q=0.9"

            if "user-data-dir" in arg:
                m = re.search("(?:--)?user-data-dir(?:[ =])?(.*)", arg)
                try:
                    user_data_dir = m[1]
                    logger.debug(
                        "user-data-dir found in user argument %s => %s" % (arg, m[1])
                    )
                    keep_user_data_dir = True

                except IndexError:
                    logger.debug(
                        "no user data dir could be extracted from supplied argument %s "
                        % arg
                    )

        if not user_data_dir:
            # backward compatiblity
            # check if an old uc.ChromeOptions is used, and extract the user data dir

            if hasattr(options, "user_data_dir") and getattr(
                options, "user_data_dir", None
            ):
                import warnings

                warnings.warn(
                    "using ChromeOptions.user_data_dir might stop working in future versions."
                    "use uc.Chrome(user_data_dir='/xyz/some/data') in case you need existing profile folder"
                )
                options.add_argument("--user-data-dir=%s" % options.user_data_dir)
                keep_user_data_dir = True
                logger.debug(
                    "user_data_dir property found in options object: %s" % user_data_dir
                )

            else:
                user_data_dir = os.path.normpath(tempfile.mkdtemp())
                keep_user_data_dir = False
                arg = "--user-data-dir=%s" % user_data_dir
                options.add_argument(arg)
                logger.debug(
                    "created a temporary folder in which the user-data (profile) will be stored during this\n"
                    "session, and added it to chrome startup arguments: %s" % arg
                )

        if not language:
            try:
                import locale

                language = locale.getdefaultlocale()[0].replace("_", "-")
            except Exception:
                pass
            if not language:
                language = "en-US"

        options.add_argument("--lang=%s" % language)

        if not options.binary_location:
            options.binary_location = (
                browser_executable_path or find_chrome_executable(chrome_version)
            )
        if not os.path.exists(options.binary_location):
            time.sleep(5)
            # 如果没有安装，可以在下面的链接下载安装：https://www.google.com/chrome/beta/
            print(f"""\n\n\n要想过Cloudflare验证，需要以下目录存在115版本的Chrome Beta版浏览器，注意是Beta版不是正式版：C:\Program Files\Google\Chrome Beta
                    如果Beta版本不是115，请在软件下载目录中找到Chrome_Beta_115_win64.7z压缩包，然后解压并复制（覆盖）为C:\Program Files\Google\Chrome Beta目录即可。
                    
                    请手动关闭此程序，配置完成后重新执行任务。
                  
                    """)
            print("""To pass the Cloudflare verification, you need the following directory to exist in the 115 version of Chrome Beta, note that it is the Beta version not the official version: C:\Program Files\Google\Chrome Beta, 
                    If the Beta version is not 115, please find the Chrome_Beta_115_win64.7z compressed package in the software download directory, then unzip and copy (overwrite) to the C:\Program Files\Google\Chrome Beta directory.
                    
                    Please close this program manually and re-execute the task after the configuration is complete.
                    
                    """)

            time.sleep(100)
        else: 
            folder_path = os.path.dirname(os.path.abspath(options.binary_location))
            folder_list = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
            numeric_folders = [f for f in folder_list if f[0].isdigit()]
            version = numeric_folders[0].split('.')[0]
            if version != "115":
                time.sleep(5)
                print("Chrome Beta版本不是115，请将Chrome Beta的版本替换为115， 方法为下载115版本的Chrome Beta浏览器，然后解压并覆盖C:\Program Files\Google\Chrome Beta目录即可，软件下载目录中有Chrome_Beta_115_win64.7z版本的压缩包，可直接下载后解压替换。")
                print("Chrome Beta version is not 115, please replace the version of Chrome Beta with 115, the method is to download the 115 version of Chrome Beta browser, then unzip and overwrite the C:\Program Files\Google\Chrome Beta directory, the software download directory has Chrome_Beta_115_win64.7z version of the compressed package, you can download and unzip directly to replace.")
                print("\n请手动关闭此程序。\n")
                print("\nPlease close this program manually.\n")
                time.sleep(100)
                

        
        print("Options Binary Location: ", options.binary_location)

        self._delay = 3

        self.user_data_dir = user_data_dir
        self.keep_user_data_dir = keep_user_data_dir

        if suppress_welcome:
            options.arguments.extend(["--no-default-browser-check", "--no-first-run"])
        if no_sandbox:
            options.arguments.extend(["--no-sandbox", "--test-type"])

        if headless or options.headless:
            if self.patcher.version_main < 108:
                options.add_argument("--headless=chrome")
            elif self.patcher.version_main >= 108:
                options.add_argument("--headless=new")

        # options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        options.add_argument("--no-sandbox")
        # fixes "could not connect to chrome" error when running
        # on linux using privileged user like root (which i don't recommend)

        options.add_argument(
            "--log-level=%d" % log_level
            or divmod(logging.getLogger().getEffectiveLevel(), 10)[0]
        )

        if hasattr(options, "handle_prefs"):
            options.handle_prefs(user_data_dir)

        # fix exit_type flag to prevent tab-restore nag
        try:
            with open(
                os.path.join(user_data_dir, "Default/Preferences"),
                encoding="latin1",
                mode="r+",
            ) as fs:
                config = json.load(fs)
                if config["profile"]["exit_type"] is not None:
                    # fixing the restore-tabs-nag
                    config["profile"]["exit_type"] = None
                fs.seek(0, 0)
                json.dump(config, fs)
                fs.truncate()  # the file might be shorter
                logger.debug("fixed exit_type flag")
        except Exception as e:
            logger.debug("did not find a bad exit_type flag ")

        self.options = options

        if not desired_capabilities:
            desired_capabilities = options.to_capabilities()

        if not use_subprocess:
            self.browser_pid = start_detached(
                options.binary_location, *options.arguments
            )
        else:
            browser = subprocess.Popen(
                [options.binary_location, *options.arguments],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                close_fds=IS_POSIX,
            )
            self.browser_pid = browser.pid

        if service_creationflags:
            service = selenium.webdriver.common.service.Service(
                self.patcher.executable_path, port, service_args, service_log_path
            )
            for attr_name in ("creationflags", "creation_flags"):
                if hasattr(service, attr_name):
                    setattr(service, attr_name, service_creationflags)
                    break
        else:
            service = None

        super(Chrome, self).__init__(
            executable_path=self.patcher.executable_path,
            port=port,
            options=options,
            service_args=service_args,
            desired_capabilities=desired_capabilities,
            service_log_path=service_log_path,
            keep_alive=keep_alive,
            service=service,  # needed or the service will be re-created
        )

        self.reactor = None

        if enable_cdp_events:
            if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
                logging.getLogger(
                    "selenium.webdriver.remote.remote_connection"
                ).setLevel(20)
            reactor = Reactor(self)
            reactor.start()
            self.reactor = reactor

        if advanced_elements:
            self._web_element_cls = UCWebElement
        else:
            self._web_element_cls = WebElement

        if options.headless:
            self._configure_headless()

    def _configure_headless(self):
        orig_get = self.get
        logger.info("setting properties for headless")

        def get_wrapped(*args, **kwargs):
            if self.execute_script("return navigator.webdriver"):
                logger.info("patch navigator.webdriver")
                self.execute_cdp_cmd(
                    "Page.addScriptToEvaluateOnNewDocument",
                    {
                        "source": """

                           Object.defineProperty(window, "navigator", {
                                Object.defineProperty(window, "navigator", {
                                  value: new Proxy(navigator, {
                                    has: (target, key) => (key === "webdriver" ? false : key in target),
                                    get: (target, key) =>
                                      key === "webdriver"
                                        ? false
                                        : typeof target[key] === "function"
                                        ? target[key].bind(target)
                                        : target[key],
                                  }),
                                });
                    """
                    },
                )

                logger.info("patch user-agent string")
                self.execute_cdp_cmd(
                    "Network.setUserAgentOverride",
                    {
                        "userAgent": self.execute_script(
                            "return navigator.userAgent"
                        ).replace("Headless", "")
                    },
                )
                self.execute_cdp_cmd(
                    "Page.addScriptToEvaluateOnNewDocument",
                    {
                        "source": """
                            Object.defineProperty(navigator, 'maxTouchPoints', {get: () => 1});
                            Object.defineProperty(navigator.connection, 'rtt', {get: () => 100});

                            // https://github.com/microlinkhq/browserless/blob/master/packages/goto/src/evasions/chrome-runtime.js
                            window.chrome = {
                                app: {
                                    isInstalled: false,
                                    InstallState: {
                                        DISABLED: 'disabled',
                                        INSTALLED: 'installed',
                                        NOT_INSTALLED: 'not_installed'
                                    },
                                    RunningState: {
                                        CANNOT_RUN: 'cannot_run',
                                        READY_TO_RUN: 'ready_to_run',
                                        RUNNING: 'running'
                                    }
                                },
                                runtime: {
                                    OnInstalledReason: {
                                        CHROME_UPDATE: 'chrome_update',
                                        INSTALL: 'install',
                                        SHARED_MODULE_UPDATE: 'shared_module_update',
                                        UPDATE: 'update'
                                    },
                                    OnRestartRequiredReason: {
                                        APP_UPDATE: 'app_update',
                                        OS_UPDATE: 'os_update',
                                        PERIODIC: 'periodic'
                                    },
                                    PlatformArch: {
                                        ARM: 'arm',
                                        ARM64: 'arm64',
                                        MIPS: 'mips',
                                        MIPS64: 'mips64',
                                        X86_32: 'x86-32',
                                        X86_64: 'x86-64'
                                    },
                                    PlatformNaclArch: {
                                        ARM: 'arm',
                                        MIPS: 'mips',
                                        MIPS64: 'mips64',
                                        X86_32: 'x86-32',
                                        X86_64: 'x86-64'
                                    },
                                    PlatformOs: {
                                        ANDROID: 'android',
                                        CROS: 'cros',
                                        LINUX: 'linux',
                                        MAC: 'mac',
                                        OPENBSD: 'openbsd',
                                        WIN: 'win'
                                    },
                                    RequestUpdateCheckStatus: {
                                        NO_UPDATE: 'no_update',
                                        THROTTLED: 'throttled',
                                        UPDATE_AVAILABLE: 'update_available'
                                    }
                                }
                            }

                            // https://github.com/microlinkhq/browserless/blob/master/packages/goto/src/evasions/navigator-permissions.js
                            if (!window.Notification) {
                                window.Notification = {
                                    permission: 'denied'
                                }
                            }

                            const originalQuery = window.navigator.permissions.query
                            window.navigator.permissions.__proto__.query = parameters =>
                                parameters.name === 'notifications'
                                    ? Promise.resolve({ state: window.Notification.permission })
                                    : originalQuery(parameters)

                            const oldCall = Function.prototype.call
                            function call() {
                                return oldCall.apply(this, arguments)
                            }
                            Function.prototype.call = call

                            const nativeToStringFunctionString = Error.toString().replace(/Error/g, 'toString')
                            const oldToString = Function.prototype.toString

                            function functionToString() {
                                if (this === window.navigator.permissions.query) {
                                    return 'function query() { [native code] }'
                                }
                                if (this === functionToString) {
                                    return nativeToStringFunctionString
                                }
                                return oldCall.call(oldToString, this)
                            }
                            // eslint-disable-next-line
                            Function.prototype.toString = functionToString
                            """
                    },
                )
            return orig_get(*args, **kwargs)

        self.get = get_wrapped

    # def _get_cdc_props(self):
    #     return self.execute_script(
    #         """
    #         let objectToInspect = window,
    #             result = [];
    #         while(objectToInspect !== null)
    #         { result = result.concat(Object.getOwnPropertyNames(objectToInspect));
    #           objectToInspect = Object.getPrototypeOf(objectToInspect); }
    #
    #         return result.filter(i => i.match(/^([a-zA-Z]){27}(Array|Promise|Symbol)$/ig))
    #         """
    #     )
    #
    # def _hook_remove_cdc_props(self):
    #     self.execute_cdp_cmd(
    #         "Page.addScriptToEvaluateOnNewDocument",
    #         {
    #             "source": """
    #                 let objectToInspect = window,
    #                     result = [];
    #                 while(objectToInspect !== null)
    #                 { result = result.concat(Object.getOwnPropertyNames(objectToInspect));
    #                   objectToInspect = Object.getPrototypeOf(objectToInspect); }
    #                 result.forEach(p => p.match(/^([a-zA-Z]){27}(Array|Promise|Symbol)$/ig)
    #                                     &&delete window[p]&&console.log('removed',p))
    #                 """
    #         },
    #     )

    def get(self, url):
        # if self._get_cdc_props():
        #     self._hook_remove_cdc_props()
        return super().get(url)

    def add_cdp_listener(self, event_name, callback):
        if (
            self.reactor
            and self.reactor is not None
            and isinstance(self.reactor, Reactor)
        ):
            self.reactor.add_event_handler(event_name, callback)
            return self.reactor.handlers
        return False

    def clear_cdp_listeners(self):
        if self.reactor and isinstance(self.reactor, Reactor):
            self.reactor.handlers.clear()

    def window_new(self):
        self.execute(
            selenium.webdriver.remote.command.Command.NEW_WINDOW, {"type": "window"}
        )

    def tab_new(self, url: str):
        """
        this opens a url in a new tab.
        apparently, that passes all tests directly!

        Parameters
        ----------
        url

        Returns
        -------

        """
        if not hasattr(self, "cdp"):
            from .cdp import CDP

            cdp = CDP(self.options)
            cdp.tab_new(url)

    def reconnect(self, timeout=0.1):
        try:
            self.service.stop()
        except Exception as e:
            logger.debug(e)
        time.sleep(timeout)
        try:
            self.service.start()
        except Exception as e:
            logger.debug(e)

        try:
            self.start_session()
        except Exception as e:
            logger.debug(e)

    def start_session(self, capabilities=None, browser_profile=None):
        if not capabilities:
            capabilities = self.options.to_capabilities()
        super(selenium.webdriver.chrome.webdriver.WebDriver, self).start_session(
            capabilities, browser_profile
        )
        # super(Chrome, self).start_session(capabilities, browser_profile)

    def quit(self):
        try:
            self.service.process.kill()
            logger.debug("webdriver process ended")
        except (AttributeError, RuntimeError, OSError):
            pass
        try:
            self.reactor.event.set()
            logger.debug("shutting down reactor")
        except AttributeError:
            pass
        try:
            os.kill(self.browser_pid, 15)
            logger.debug("gracefully closed browser")
        except Exception as e:  # noqa
            logger.debug(e, exc_info=True)
        if (
            hasattr(self, "keep_user_data_dir")
            and hasattr(self, "user_data_dir")
            and not self.keep_user_data_dir
        ):
            for _ in range(5):
                try:
                    shutil.rmtree(self.user_data_dir, ignore_errors=False)
                except FileNotFoundError:
                    pass
                except (RuntimeError, OSError, PermissionError) as e:
                    logger.debug(
                        "When removing the temp profile, a %s occured: %s\nretrying..."
                        % (e.__class__.__name__, e)
                    )
                else:
                    logger.debug("successfully removed %s" % self.user_data_dir)
                    break
                time.sleep(0.1)

        # dereference patcher, so patcher can start cleaning up as well.
        # this must come last, otherwise it will throw 'in use' errors
        self.patcher = None

    def __getattribute__(self, item):
        if not super().__getattribute__("debug"):
            return super().__getattribute__(item)
        else:
            import inspect

            original = super().__getattribute__(item)
            if inspect.ismethod(original) and not inspect.isclass(original):

                def newfunc(*args, **kwargs):
                    logger.debug(
                        "calling %s with args %s and kwargs %s\n"
                        % (original.__qualname__, args, kwargs)
                    )
                    return original(*args, **kwargs)

                return newfunc
            return original

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.service.stop()
        time.sleep(self._delay)
        self.service.start()
        self.start_session()

    def __hash__(self):
        return hash(self.options.debugger_address)

    def __dir__(self):
        return object.__dir__(self)

    def __del__(self):
        try:
            self.service.process.kill()
        except:  # noqa
            pass
        self.quit()

    @classmethod
    def _ensure_close(cls, self):
        # needs to be a classmethod so finalize can find the reference
        logger.info("ensuring close")
        if (
            hasattr(self, "service")
            and hasattr(self.service, "process")
            and hasattr(self.service.process, "kill")
        ):
            self.service.process.kill()


def find_chrome_executable(version):
    """
    Finds the chrome, chrome beta, chrome canary, chromium executable

    Returns
    -------
    executable_path :  str
        the full file path to found executable

    """
    candidates = set()
    if IS_POSIX:
        for item in os.environ.get("PATH").split(os.pathsep):
            for subitem in (
                "google-chrome",
                "chromium",
                "chromium-browser",
                "chrome",
                "google-chrome-stable",
            ):
                candidates.add(os.sep.join((item, subitem)))
        if "darwin" in sys.platform:
            candidates.update(
                [
                    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                    "/Applications/Chromium.app/Contents/MacOS/Chromium",
                ]
            )
    else:
        for item in map(
            os.environ.get,
            ("PROGRAMFILES", "PROGRAMFILES(X86)", "LOCALAPPDATA", "PROGRAMW6432"),
        ):
            if item is not None:
                for subitem in (
                    "Google/Chrome/Application",
                    "Google/Chrome Beta/Application",
                    "Google/Chrome Canary/Application",
                ):
                    candidates.add(os.sep.join((item, subitem, "chrome.exe")))
    for candidate in candidates:
        if os.path.exists(candidate) and os.access(candidate, os.X_OK):
            print(f"""\n\n\n要想过Cloudflare验证，需要满足以下条件：
                  自己的环境已经安装了115版本的Chrome Beta版浏览器，注意是Beta版不是正式版，且浏览器安装路径必须保持不变，在C:\Program Files\Google\Chrome Beta\Application\chrome.exe
                  如果没有安装，可以在下面的链接下载安装：https://www.google.com/chrome/beta/
                  软件将会使用以下目录的Chrome Beta浏览器：", {os.path.normpath(candidate)}, "，请检查此浏览器版本是否为 115 版本的Beta浏览器，如果不是将无法运行。""")
            # print("The software will use the Chrome browser in the following directory:", os.path.normpath(candidate), "Please check if the version of this browser is version " + str(version) + ", if not, it will not be able to run.\n\n\n")
            print(f"""The software will use the Chrome browser in the following directory: {os.path.normpath(candidate)}, Please check if the version of this browser is version 115, if not, it will not be able to run.\n\n\n""")
            time.sleep(5)
            return os.path.normpath(candidate)

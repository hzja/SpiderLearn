# 原创
：  Flatpickr教程：使用JavaScript快速创建一个自定义日期选择器

# Flatpickr教程：使用JavaScript快速创建一个自定义日期选择器

**部分数据来源：**ChatGPT 

#### 引言

        如果您是一个网站开发者，想为自己的网站添加方便易用的日期选择对话框，那么Flatpickr日期选择对话框可能正好符合您的需要。在这篇文章中，我们将详细介绍如何使用Flatpickr日期选择对话框，并提供一份样例代码供您参考。

Flatpickr是一个轻量级、快速、灵活的JavaScript日期选择器，具有很多功能，如时间选择器、本地化支持、多种日期格式等。Flatpickr易于集成到你的网站中，只需几行简单的代码即可实现一个高度定制化的日期选择对话框。

#### 以下是一个基于Flatpickr实现的日期选择对话框的完整代码，供您参考：

```
&lt;!--声明文档类型--&gt;
&lt;!DOCTYPE html&gt;
&lt;!--html标签--&gt;
&lt;html lang="en"&gt;

&lt;head&gt;
  &lt;!--设置字符集--&gt;
  &lt;meta charset="UTF-8"&gt;
  &lt;!--设置网页标题--&gt;
  &lt;title&gt;Flatpickr日期选择对话框&lt;/title&gt;
  &lt;!--引入Flatpickr样式文件--&gt;
  &lt;link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css"&gt;
  &lt;!--定义样式--&gt;
  &lt;style&gt;
    /*设置body样式*/
    body {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      background-color: #f8f8f8;
      font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    }

    /*设置日期选择器样式*/
    .date-picker {
      position: relative;
      display: inline-block;
      cursor: pointer;
    }

    /*设置日期显示框样式*/
    #date-picker-display {
      border: 2px solid #ccc;
      border-radius: 5px;
      padding: 10px;
      font-size: 16px;
      background-color: white;
      outline: none;
      width: 300px;
    }

    /*设置日期选择器弹出框样式*/
    .date-picker-modal {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      background-color: rgba(0, 0, 0, 0.4);
      z-index: 9999;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s ease-in-out;
    }

    /*设置日期选择器弹出框显示样式*/
    .date-picker-modal.show {
      opacity: 1;
      pointer-events: auto;
    }

    /*设置日期选择器头部样式*/
    .date-picker-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 20px;
      background-color: white;
      border-bottom: 1px solid #ccc;
    }

    /*设置取消和确认按钮样式*/
    .date-picker-cancel,
    .date-picker-confirm {
      border: none;
      outline: none;
      cursor: pointer;
      font-size: 16px;
      background-color: transparent;
      color: #007bff;
    }

    /*设置取消和确认按钮的鼠标悬停样式*/
    .date-picker-cancel:hover,
    .date-picker-confirm:hover {
      text-decoration: underline;
    }

    /*设置日期选择器标题样式*/
    .date-picker-title {
      font-size: 18px;
      font-weight: bold;
      text-transform: uppercase;
    }

    /*设置日期选择器内容样式*/
    .date-picker-content {
      display: flex;
      margin: 20px;
    }

    /*设置日期选择器列样式*/
    .date-picker-column {
      flex: 1;
      height: 200px;
      overflow-y: auto;
      border-right: 1px solid #ccc;
      padding-right: 20px;
      margin-right: 20px;
    }

    /*设置日期选择器选项样式*/
    .date-picker-option {
      display: block;
      padding: 10px;
      font-size: 16px;
      color: #333;
      cursor: pointer;
    }

    /*设置日期选择器选项鼠标悬停和激活样式*/
    .date-picker-option:hover,
    .date-picker-option-active {
      background-color: #007bff;
      color: white;
    }
  &lt;/style&gt;
&lt;/head&gt;
&lt;!--设置body内容--&gt;

&lt;body&gt;
  &lt;div class="date-picker"&gt;
    &lt;!--创建一个只读的输入框--&gt;
    &lt;input type="text" id="date-picker-display" readonly&gt;
  &lt;/div&gt;
  &lt;!--引入Flatpickr库文件--&gt;
  &lt;script src="https://cdn.jsdelivr.net/npm/flatpickr"&gt;&lt;/script&gt;
  &lt;!--编写JS代码--&gt;
  &lt;script&gt;
    // 初始化Flatpickr
    flatpickr("#date-picker-display", {
      // 开启时间选择器功能
      enableTime: true,
      // 设置日期格式
      dateFormat: "Y-m-d H:i",
      // 设置默认选中日期为当前日期
      defaultDate: new Date(),
    });

    // 设置Flatpickr中文语言选项
    flatpickr.l10ns.zh = {
      weekdays: {
        shorthand: ["周日", "周一", "周二", "周三", "周四", "周五", "周六"],
        longhand: ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
      },
      months: {
        shorthand: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
        longhand: ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
      },
      rangeSeparator: " 至 ",
      weekAbbreviation: "周",
      scrollTitle: "滚动切换",
      toggleTitle: "点击切换 12/24 小时时制"
    };

    // 使用中文语言选项初始化Flatpickr
    flatpickr("#date-picker-display", {
      enableTime: true,
      dateFormat: "Y-m-d H:i",
      defaultDate: new Date(),
      locale: "zh",
      monthSelectorType: "dropdown", // 使用下拉选择框选择月份
      shorthandCurrentMonth: true, // 使用缩写月份
      weekdays: {
        shorthand: ["日", "一", "二", "三", "四", "五", "六"],
        longhand: ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
      }
    });

    // 定义年、日、时、分数组
    const years = [];
    const currentYear = new Date().getFullYear();
    for (let i = currentYear - 10; i &lt;= currentYear + 10; i++) {
      years.push(i);
    }
    const days = [];
    for (let i = 1; i &lt;= 31; i++) {
      days.push(i);
    }
    const hours = [];
    for (let i = 0; i &lt;= 23; i++) {
      hours.push(i);
    }
    const minutes = [];
    for (let i = 0; i &lt;= 59; i++) {
      minutes.push(i);
    }

    // 更新日期选择框显示内容
    function updateDatePickerDisplay() {
      const year = datePickerYearColumn.querySelector(".date-picker-option-active").textContent;
      const day = datePickerDayColumn.querySelector(".date-picker-option-active").textContent;
      const hour = datePickerHourColumn.querySelector(".date-picker-option-active").textContent;
      const selectedDate = new Date(`${year}-${monthIndex + 1}-${day} ${hour}:${minute}`);
      flatpickr("#date-picker-display", {
        enableTime: true,
        dateFormat: "Y-m-d H:i",
        defaultDate: selectedDate
      });
    }

    // 激活日期选择器的选项
    function activateDatePickerOption(element) {
      element.classList.add("date-picker-option-active");
    }

    // 取消日期选择器的选项激活
    function deactivateDatePickerOption(element) {
      element.classList.remove("date-picker-option-active");
    }

    // 滚动到日期选择器的指定选项
    function scrollToOption(element, index) {
      const options = element.querySelectorAll(".date-picker-option");
      const optionHeight = options[0].offsetHeight;
      const scrollDistance = optionHeight * (index - 2);
      element.scroll({ top: scrollDistance, behavior: "smooth" });
    }
  &lt;/script&gt;
&lt;/body&gt;

&lt;/html&gt;
```

现在让我们来逐步分析上述代码，以便理解这个日期选择对话框是如何工作的。

#### 第一步：引入Flatpickr样式文件

```
&lt;link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css"&gt;
```

#### 第二步：创建日期选择器输入框

```
&lt;div class="date-picker"&gt;
  &lt;input type="text" id="date-picker-display" readonly&gt;
&lt;/div&gt;
```

在HTML中创建一个DIV元素，并设置其class为“date-picker”，在该元素中创建一个只读的文本输入框，id为“date-picker-display”，这将用于显示日期选择器选定的日期和时间。

#### 第三步：引入Flatpickr库文件和JS代码

```
&lt;script src="https://cdn.jsdelivr.net/npm/flatpickr"&gt;&lt;/script&gt;
&lt;script&gt;
  flatpickr("#date-picker-display", {
    enableTime: true,
    dateFormat: "Y-m-d H:i",
    defaultDate: new Date(),
  });
&lt;/script&gt;
```

在HTML body标签底部，在Flatpickr样式文件之后，引入Flatpickr库文件和上面的JS代码。这段JS代码使用了Flatpickr库中的函数，将日期选择器与输入框绑定，并将日期格式设置为"Y-m-d H:i"，即“年-月-日 时:分”的形式，以便用户能够选择日期和时间。

#### 第四步：定义日期选择器样式

```
&lt;style&gt;
  /*设置body样式*/
  body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
    background-color: #f8f8f8;
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  }

  /*设置日期选择器样式*/
  .date-picker {
    position: relative;
    display: inline-block;
    cursor: pointer;
  }

  /*设置日期显示框样式*/
  #date-picker-display {
    border: 2px solid #ccc;
    border-radius: 5px;
    padding: 10px;
    font-size: 16px;
    background-color: white;
    outline: none;
    width: 300px;
  }

  /*其他样式...*/
&lt;/style&gt;
```

这部分代码提供了日期选择器的样式定义，包括整个页面的背景色、日期显示框的边框、字体等。这些样式可以根据需要进行修改。

#### 第五步：定义年、日、时、分数组

```
const years = [];
const currentYear = new Date().getFullYear();
for (let i = currentYear - 10; i &lt;= currentYear + 10; i++) {
  years.push(i);
}
const days = [];
for (let i = 1; i &lt;= 31; i++) {
  days.push(i);
}
const hours = [];
for (let i = 0; i &lt;= 23; i++) {
  hours.push(i);
}
const minutes = [];
for (let i = 0; i &lt;= 59; i++) {
  minutes.push(i);
}
```

这部分代码定义了四个数组，分别用于存储可选的年、日、时和分选项。在日期选择器弹出框中，我们将使用这些数组来显示可供用户选择的日期和时间选项。

#### 第六步：更新日期选择框显示内容

```
function updateDatePickerDisplay() {
  const year = datePickerYearColumn.querySelector(".date-picker-option-active").textContent;
  const day = datePickerDayColumn.querySelector(".date-picker-option-active").textContent;
  const hour = datePickerHourColumn.querySelector(".date-picker-option-active").textContent;
  const selectedDate = new Date(`${year}-${monthIndex + 1}-${day} ${hour}:${minute}`);
  flatpickr("#date-picker-display", {
    enableTime: true,
    dateFormat: "Y-m-d H:i",
    defaultDate: selectedDate
  });
}
```

这部分代码定义一个名为“updateDatePickerDisplay()”的函数，用于更新日期选择框中显示的日期和时间。在该函数中，我们首先获取当前年、日和小时列中被激活的选项的文本内容，并使用这些值创建一个新的Date对象，以便Flatpickr可以正确显示日期和时间。最后，我们使用“flatpickr()”函数更新日期选择框的默认日期。

#### 第七步：激活和取消日期选择器的选项

        这部分代码定义了两个函数，用于激活和取消日期选择器中的选项。当用户单击某个选项时，我们将使用这些函数将该选项标记为“active”，以便用户可以看到该选项被选择了。

```
function activateDatePickerOption(element) {
  element.classList.add("date-picker-option-active");
}

function deactivateDatePickerOption(element) {
  element.classList.remove("date-picker-option-active");
}
```

#### 第八步：滚动到日期选择器指定选项

```
function scrollToOption(element, index) {
  const options = element.querySelectorAll(".date-picker-option");
  const optionHeight = options[0].offsetHeight;
  const scrollDistance = optionHeight * (index - 2);
  element.scroll({ top: scrollDistance, behavior: "smooth" });
}
```

这部分代码定义了一个名为“scrollToOption()”的函数，用于将日期选择器滚动到指定选项。当用户选择不同时间和日期时，我们将使用该函数使得选择框能够滚动到正确的位置，以便显示正确的选项。

#### 运行效果

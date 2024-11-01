# 原创
：  Vue 项目中的自适应布局：px 转换成 vw/vh

# Vue 项目中的自适应布局：px 转换成 vw/vh

**部分数据来源：**ChatGPT

**摘要：**在移动设备上，不同分辨率的屏幕对应的界面大小不同，这就需要前端开发者使用自适应布局来适应不同的分辨率。本文介绍如何在 Vue 项目中使用 postcss-px-to-viewport 插件来实现将 px 转换为 vw/vh 的自适应布局方案。

#### 一、什么是自适应布局

        自适应布局是指页面布局随着设备屏幕尺寸变化而自动调整。例如，在桌面浏览器上访问页面时，页面宽度可能会比在移动设备上访问时更宽，因此需要根据设备的屏幕尺寸和分辨率动态调整页面的布局。这样可以使页面在不同设备和分辨率下都具有较好的可读性和可用性。

#### 二、px 转换为 vw/vh 的方案

        在实现自适应布局的过程中，常用的一种方案是将页面中的 px 单位转换成 vw/vh 单位。vw 和 vh 分别代表 viewport width 和 viewport height，即视口的宽度和高度。在不同设备上，视口的大小会不同，所以使用 vw/vh 单位可以根据不同的视口大小来动态调整元素大小。

        幸运的是，Vue 项目中可以很方便地使用 postcss-px-to-viewport 插件来实现将 px 转换成 vw/vh 的效果。该插件依据设备的尺寸进行适配，可以方便地进行自适应布局。

#### 三、如何在 Vue 项目中使用 postcss-px-to-viewport 插件

首先，在 Vue 项目中安装 postcss-px-to-viewport 插件：

```
npm install postcss-px-to-viewport --save-dev

```

然后，在项目根目录下创建 postcss.config.js 配置文件，添加如下配置：

```
module.exports = {
  // 其他配置...
  plugins: {
    'postcss-px-to-viewport': {
      viewportWidth: 750, // 设计稿宽度
      unitToConvert: 'px', // 需要转换的单位，默认为"px"
      viewportUnit: 'vw', // 转换后的单位，默认为"vw"
      selectorBlackList: ['.ignore', '.hairlines'], // 不需要转换的类名
      minPixelValue: 1, // 最小的转换单位值
      mediaQuery: false,  // 控制是否允许将媒体查询中的 px 单位进行转换为 vw/vh 单位。
      exclude: [/(\/|\\)(node_modules)(\/|\\)/] // 排除第三方模块中的样式
    }
  }
}

```

        以上的配置将项目中的 px 单位转换成 vw 单位，并且将设计稿的宽度设置为 750px，这意味着在设计稿上，1px 将被转换成 viewportWidth 的 1/750，即 0.13333vw，也就是说视口的宽度为 750px 时，对应的 1vw 为 750px/100 = 7.5px。

在打包时，该插件会自动将 px 单位转换为 vw 单位，生成的 CSS 文件中会包含 vw/vh 实际单位。

#### 四、总结

        本文介绍了如何在 Vue 项目中使用 postcss-px-to-viewport 插件来实现将 px 转换成 vw/vh 的自适应布局方案。通过使用该插件，可以方便地实现页面根据设备的尺寸进行适配，提高应用的可读性和可用性。希望本文能够对 Vue 开发者有所帮助。

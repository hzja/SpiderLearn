# 原创
：  解决 Vite + Vue3 开发中路由异步加载导致的页面无法点击等问题

# 解决 Vite + Vue3 开发中路由异步加载导致的页面无法点击等问题

**部分数据来源：**ChatGPT  

#### 引言

        前端开发中，使用 Vite + Vue3 开发项目，路由的异步加载方式实现起来较为简便。但是当您在页面进行点击等操作时未发生相应的跳转，很可能是因为您的路由未正确注册到 Vue Router 中。

#### 这里我们提供两种解决方法

#### 1. 确认路由是否正确注册到 Vue Router 中

        当使用 import 异步加载组件时，可能会存在加载的组件还未被注册到 Vue Router 中的情况。因此，在注册路由之前，我们需要等待路由组件加载完成。您可以在路由的 component 属性中使用异步函数，等待组件加载完成后注册路由。

代码示例：

```
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: "/about",
    name: "About",
    component: () =&gt; import('./views/About.vue'),
    meta: { isLogin: false }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

```

#### 2. 确认路由链接是否正确标记为组件

        在 Vue Router 中，我们通常使用 组件 生成路由链接，以确保用户可以通过点击链接进行路由跳转。如果您的路由链接不是使用 组件 生成的，例如使用 a 标签或 location.href 进行跳转，可能会导致路由激活失败。因此，请确保您的路由链接已被正确标记为 组件。

代码示例：

```
&lt;template&gt;
  &lt;div&gt;
    &lt;router-link to="/about"&gt;About&lt;/router-link&gt;
  &lt;/div&gt;
&lt;/template&gt;

```

总之，在使用 Vite + Vue3 进行前端开发过程中，路由的异步加载方式使用起来非常方便，但是一定要注意路由的注册和链接的标记，避免出现异常情况。希望这篇博客能够对您的开发有所帮助。

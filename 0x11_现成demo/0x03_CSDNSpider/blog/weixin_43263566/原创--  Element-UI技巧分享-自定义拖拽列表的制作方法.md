# 原创
：  Element-UI技巧分享：自定义拖拽列表的制作方法

# Element-UI技巧分享：自定义拖拽列表的制作方法

**部分数据来源：**ChatGPT

#### 引言

        当我们使用 Element-UI 的自定义拖拽列表时，有时候需要根据拖拽的字段位置，将数据组成不同的列表进行显示。这种情况下，我们可以通过一些简单的操作，来实现自定义拖拽列表中的分类展示。

在本文中，我们将介绍如何使用 Element-UI 和第三方组件库 vuedraggable ，快速实现自定义拖拽列表分类功能。

#### 第一步：安装 vuedraggable

在使用 vuedraggable 之前，我们需要安装这个第三方组件库，执行以下命令即可：

```
npm install vuedraggable

```

#### 第二步：引入 vuedraggable

使用 vuedraggable，我们需要在 Vue 项目中引入这个组件，具体方法如下：

```
import Vue from 'vue';
import draggable from 'vuedraggable';
Vue.component('draggable', draggable);

```

在这里，我们使用 import 引入 vuedraggable 组件，并在 Vue 实例中注册它，这样就可以在页面中直接使用了。

#### 第三步：分类数据

        在传递数据给拖拽列表组件之前，我们需要将数据进行分类。我们可以将不同类别的数据分别存储在一个数组中，并且将它们存储在一个对象中。具体的代码实现如下：

```
// 原始数据列表
const data = [
  { id: 1, name: 'Apple', type: 'fruit' },
  { id: 2, name: 'Orange', type: 'fruit' },
  { id: 3, name: 'Carrot', type: 'vegetable' },
  { id: 4, name: 'Spinach', type: 'vegetable' }
];

let groupedData = {}; // 用于存储分类后的数据

// 循环遍历原始数据，将其分类并存储
data.forEach(item =&gt; {
  // 如果当前项存在分类，将其添加到分类下
  if(groupedData[item.type]) {
    groupedData[item.type].push(item);
  } else {
    groupedData[item.type] = [item]; // 如果分类不存在，创建一个新分类存储
  }
})

```

在上述代码中，我们首先定义了一个原始数据列表和一个用于存储分类后数据的对象。通过一个foreach循环，遍历原始数据，将其分类到相应的数组中。最终，我们将分类后的数据存储在对象 groupedData 中。

#### 第四步：渲染页面

        分类后，我们就可以将分类数据传递到拖拽列表组件中，并在页面上展示它们。首先，我们需要渲染出一个容器元素，再在里面生成两个拖拽列表容器。具体的代码如下：

```
&lt;el-container&gt;
  &lt;el-header&gt;
    &lt;el-row&gt;
      &lt;el-col span="12"&gt;&lt;h4&gt;Fruit&lt;/h4&gt;&lt;/el-col&gt;
      &lt;el-col span="12"&gt;&lt;h4&gt;Vegetable&lt;/h4&gt;&lt;/el-col&gt;
    &lt;/el-row&gt;
  &lt;/el-header&gt;
  &lt;el-main&gt;
    &lt;el-row&gt;
      &lt;el-col span="6"&gt;
        &lt;draggable v-model="groupedData.fruit" tag="ul"&gt;
          &lt;li v-for="item in groupedData.fruit" :key="item.id"&gt;{{ item.name }}&lt;/li&gt;
        &lt;/draggable&gt;
      &lt;/el-col&gt;
      &lt;el-col span="6"&gt;
        &lt;draggable v-model="groupedData.vegetable" tag="ul"&gt;
          &lt;li v-for="item in groupedData.vegetable" :key="item.id"&gt;{{ item.name }}&lt;/li&gt;
        &lt;/draggable&gt;
      &lt;/el-col&gt;
    &lt;/el-row&gt;
  &lt;/el-main&gt;
&lt;/el-container&gt;

```

在上面的代码中，我们使用 Element-UI 中的 el-container、el-header、el-main、el-row 和 el-col 等组件来排版布局，生成了两个拖拽列表容器，并把集合传递给容器。这样，列表中的每个项都将按照分类进行显示。其中，我们使用了 v-model 指令来与 groupedData 对象进行双向数据绑定。

以上步骤，我们通过 v-for 指令来遍历 groupedData 中的 fruit 和 vegetable 数组，并使用 key 属性来帮助 Vue 正确渲染每个容器中的数据。

#### 完整代码示例

下面是一份完整的代码示例，包括了以上步骤中的所有代码：

```
&lt;template&gt;
  &lt;el-container&gt;
    &lt;el-header&gt;
      &lt;el-row&gt;
        &lt;el-col span="12"&gt;&lt;h4&gt;Fruit&lt;/h4&gt;&lt;/el-col&gt;
        &lt;el-col span="12"&gt;&lt;h4&gt;Vegetable&lt;/h4&gt;&lt;/el-col&gt;
      &lt;/el-row&gt;
    &lt;/el-header&gt;
    &lt;el-main&gt;
      &lt;el-row&gt;
        &lt;el-col span="6"&gt;
          &lt;draggable v-model="groupedData.fruit" tag="ul"&gt;
            &lt;li v-for="item in groupedData.fruit" :key="item.id"&gt;{{ item.name }}&lt;/li&gt;
          &lt;/draggable&gt;
        &lt;/el-col&gt;
        &lt;el-col span="6"&gt;
          &lt;draggable v-model="groupedData.vegetable" tag="ul"&gt;
            &lt;li v-for="item in groupedData.vegetable" :key="item.id"&gt;{{ item.name }}&lt;/li&gt;
          &lt;/draggable&gt;
        &lt;/el-col&gt;
      &lt;/el-row&gt;
    &lt;/el-main&gt;
  &lt;/el-container&gt;
&lt;/template&gt;

&lt;script&gt;
import draggable from "vuedraggable"; // 引入拖拽组件

export default {
  components: {
    draggable,
  },
  data() {
    return {
      data: [
        { id: 1, name: "Apple", type: "fruit" },
        { id: 2, name: "Orange", type: "fruit" },
        { id: 3, name: "Carrot", type: "vegetable" },
        { id: 4, name: "Spinach", type: "vegetable" },
      ],
      groupedData: {}, // 用于存储分类后的数据
    };
  },
  mounted() {
    this.groupData(); // 分类数据并存储
  },
  methods: {
    /**
     * 将数据按照分类进行分组并存储到 groupedData 中
     */
    groupData() {
      this.data.forEach((item) =&gt; {
        if (this.groupedData[item.type]) {
          this.groupedData[item.type].push(item);
        } else {
          this.groupedData[item.type] = [item];
        }
      });
    },
  },
};
&lt;/script&gt;

```

在完整的代码示例中，我们首先引入 vuedraggable 组件并注册，接着在数据对象中定义了一个原始数据列表和一个用于存储分类后数据的对象 groupedData 。在 mounted 周期中调用 groupData 方法，实现将数据分类后存储到 groupedData 中。然后，在页面模板中，我们使用拖拽容器来显示数据，并将 groupedData 中不同类别的数据传播到不同的列表里面。

#### 总结

        在本文中，我们介绍了如何使用 Element-UI 和第三方组件库 vuedraggable，实现自定义拖拽列表中的分类展示功能。通过一些简单的操作，实用性很强的功能实现起来非常容易。希望它能帮助你更好地应对分类展示数据的需求。

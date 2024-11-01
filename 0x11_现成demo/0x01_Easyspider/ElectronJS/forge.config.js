module.exports = {
  packagerConfig: {},
  rebuildConfig: {},
  makers: [
    {
      name: '@electron-forge/maker-squirrel',
      config: {},
    },
    {
      name: '@electron-forge/maker-zip',
      platforms: ['darwin'],
    },
    {
      name: '@electron-forge/maker-deb',
      config: {},
    },
    {
      name: '@electron-forge/maker-rpm',
      config: {},
    },
  ],
};
// 这段代码是用JavaScript编写的，定义了一个模块的输出（module.exports），其中包含一些配置信息和生成发布包的makers。
// 1. `packagerConfig`：这是一个空对象，用于存储构建发布包时的配置信息。
// 2. `rebuildConfig`：这也是一个空对象，用于存储重新构建发布包时的配置信息。
// 3. `makers`：这是一个数组，包含四个对象，每个对象代表一个生成发布包的maker。
// 4. 第一个对象：
//   - `name`：值为'@electron-forge/maker-squirrel'，表示使用squirrelmaker来生成发布包。
//   - `config`：也是一个空对象，用于存储squirrelmaker的配置信息。
// 5. 第二个对象：
//   - `name`：值为'@electron-forge/maker-zip'，表示使用zipmaker来生成发布包。
//   - `platforms`：是一个数组，包含一个元素'darwin'，表示zipmaker仅在macOS平台上可用。
// 6. 第三个对象：
//   - `name`：值为'@electron-forge/maker-deb'，表示使用debpackager来生成发布包。
//   - `config`：也是一个空对象，用于存储debpackager的配置信息。
// 7. 第四个对象：
//   - `name`：值为'@electron-forge/maker-rpm'，表示使用rpmpackager来生成发布包。
//   - `config`：也是一个空对象，用于存储rpmpackager的配置信息。
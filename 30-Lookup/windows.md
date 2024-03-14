---
DESC: win11相关
---
## Win11 快捷键

| 快捷键      | 动作               |
| ----------- | ------------------ |
| Alt + F4    | 关闭当前页面       |
| Win+A       | 打开快速设置面板   |
| Win+B       | 快速跳转系统托盘   |
| Win+E       | 打开资源管理器     |
| Win+I       | 打开设置           |
| Win+L       | 锁屏               |
| Win+N       | 打开通知/月历面板  |
| Win+P       | 修改投屏模式       |
| Win+S/Q     | 一键搜索           |
| Win+V       | 打开剪贴板         |
| Win+W       | 打开 widget 小组件 |
| Win+X       | 呼出简易开始菜单   |
| Win+光标    | 窗口排版           |
| Win+Shift+S | 截屏               |
| Win+Home    | 最小化非活动窗口   |
| Win+.     | emoji              | 

## 自定义快捷键

| 快捷键       | 动作           |
| ------------ | -------------- |
| F1           | 截屏           |
| Alt+F1       | 截屏并自动复制 |
| F3           | 贴图           |
| Ctrl+Shift+A | 重启           |
| Ctrl+Shift+Q | 关机           |
| Alt+D        | PicGo 上传     | 



## Word 排版

| 快捷键       | 动作           |
| ------------ | -------------- |
| Ctrl+Shift+N | 删除页眉的横线 | 


## Chrome

| 操作                                     | 快捷键               |
| ---------------------------------------- | -------------------- |
| 在当前标签页中打开主页                   | **Alt + Home**       |
| 打开当前标签页浏览记录中记录的上一个页面 | **Alt + 向左箭头键** |
| 打开当前标签页浏览记录中记录的下一个页面 | **Alt + 向右键**     |
|在新标签页中打开“历史记录”页|**Ctrl + h**|
|在新标签页中打开“下载内容”页|**Ctrl + j**|                                         |                      |
|为网站名称添加 `www.` 和 `.com`，然后在当前标签页中打开该网址|输入网站名称并按 **Ctrl + Enter** 键|
|为网站名称添加 `www.` 和 `.com`，然后在新的窗口中打开该网址|输入网站名称并按 **Ctrl + Shift + Enter** 键|


## Realforce 键盘
| 操作                                 | 快捷键 |
| ------------------------------------ | ------ |
| 开启默认浏览器                       | Fn+F1  |
| 开启默认邮件客户端                   | Fn+F2  |
| 计算器                               | Fn+F3  |
| 媒体播放器                           | Fn+F4  |
| 上一曲                               | Fn+F5  |
| 暂停                                 | Fn+F6  |
| 下一曲                               | Fn+F7  |
| 停止播放                             | Fn+F8  |
| 浏览器收藏夹                         | Fn+F9  |
| 打开资源管理器                       | Fn+F10 |
| 交换 Caps Lock 和 Ctrl               | Fn+F11 |
| 键盘锁，先在驱动里面设置需要失效的键 | Fn+F12 | 


## 恢复右键
管理员运行命令：
`reg.exe add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve` 重启就恢复 win10右键了

`reg.exe delete "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /va /f` 这个是恢复win11右键


## word
**批量设置编号上标**的具体操作：
1) 按**Ctrl+H**，打开查找与替换窗口，点击【更多】展开完整窗口；
2) 在**查找窗口里输入[^#]或者[^#^#]**，进行**单位数**和**双位数编号**的查找；
3) 光标置于替换为窗口中，**点击【格式】-【字体】**，**勾选【上标】**；
4) 点击【全部替换】，完成。



## 快捷键[​](https://tutorials.tinkink.net/zh-hans/vscode/copilot-usage-and-shortcut.html#%E5%BF%AB%E6%8D%B7%E9%94%AE)

Copilot 也提供了一些快捷键，可以很方便地使用。

- 接受建议：`Tab`
- 拒绝建议：`Esc`
- 打开Copilot：`Ctrl + Enter` （会打开一个单独的面板，展示10个建议）
- 下一条建议：`Alt/Option + ]`
- 上一条建议：`Alt/Option + [`
- 触发行内Copilot：`Alt/Option + \` （Coplit还没有给出建议或者建议被拒绝了，希望手工触发它提供建议）



tags: #LUT
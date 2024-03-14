---
DESC: obsidian使用方法
---

# 官方教程

 [obsidian 官方教程](https://publish.obsidian.md/chinesehelp/01+2021%E6%96%B0%E6%95%99%E7%A8%8B/2021%E5%B9%B4%E6%96%B0%E6%95%99%E7%A8%8B)


# 快捷键
| 动作     | 快捷键         |
| -------- | -------------- |
| 插入日期 | `ctrl+shift+'` |
| 插入时间 | `ctrl+shift+;` | 


# 插件使用方法

## Templater
***
| 命令                                                   | 说明                   |
| ------------------------------------------------------ | ---------------------- |
| `<% tp.file.cursor(n) %>`                              | 光标，n可以换成数字    |
| `<% tp.file.creation_date("YYYY-MM-DD-dddd HH:mm") %>` | 日期(ddd 周 dddd 星期) |
| `<% tp.date.now("YYYY-MM-DD", -1) %>`                    | 昨天的日记             |
| `<% tp.date.now("YYYY-MM-DD", +1) %>`                    | 明天的日记             |
·
### 一些链接
[日月年link生成](https://forum.obsidian.md/t/automatically-create-yesterday-today-and-tomorrow-daily-note-links-in-the-daily-template/40590)
[momentjs时间戳格式转换](https://blog.csdn.net/m0_46371029/article/details/119900775)


## 模板使用
***
### 1. 组会
`ctrl+P` - quickadd - 会议记录
### 2. 月度
`ctrl+P` - quickadd - 月度记录
### 3. 账单
`alt+N` - 账单模板 
### 4. 课堂
`alt+N` - 账单模板 - 在根目录下创建untitled file - 移动到需要位置
在需要的文件夹里创建新的笔记 - `/` - 插入模板(或者侧边栏点击模板)
### 5. 看板
同上
### 6. 书籍/电影
`ctrl+P` - douban


## Dataview
***
### 官方教程
[Obsidian-dataview 官网](https://blacksmithgu.github.io/obsidian-dataview/)

### 样式
1. Purple Red table
`cssclass: purpleRed, wideTable, fixedFc`
2. Flat Blue
`cssclass: flatBlue, wideTable`
3. Latex Like
`cssclass: academia, wideTable`
4. White red rounded
`cssclass: whiteRed, wideTable, whiteRed-rounded`
5. White red
`cssclass: whiteRed, wideTable`
6. Yellow cab
`cssclass: yellowCab, wideTable`

### 时间格式修改
用 dataformat 
```
table WITHOUT ID file.link AS "标题", dateformat(file.mtime, "yyyy-MM-dd HH:MM") as "时间"
```

### 标题修改
1. 文件名
   `TABLE WITHOUT ID file.link AS "Time"`
2. 普通标题名
   `TABLE file.mtime AS "修改时间" `

### 最近编辑
```dataview
table WITHOUT ID file.link AS "标题", dateformat(file.mtime, "yyyy-MM-dd HH:MM") as "时间", file.path AS "路径"
from !"kanban" and !"Home"
where !contains(file.name,"Day Planner")
sort file.mtime desc
limit 5
```

## Annotator: pdf 注释
***
```
---
Annotation-target: ***/***.pdf
---
```


## Citations 模板字段
***
功能：用于 zotero 导出
-   文章标题： `{{title}}`
-   关键字： `{{tags}}`
-   摘要： `{{abstractNote}}`
-   DOI: `{{DOI}}`
-   Pdf文档的zotero链接，点击即可查看pdf（需要再zotero中添加附件）： `{{pdfAttachments}}`
-   Bib 键： `{{citekey}}`


## 进度条
***
```dataviewjs

let file = dv.current()

let af = app.vault.getMarkdownFiles().filter(p=>p.path==file.file.path)[0]

let container = this.container

  

let content = await app.vault.readRaw(file.file.path)

let regexp = /(?<=\%\%)[\s\S]*?(?=\%\%)/

let rawText = regexp.exec(content)[0].split('\n').filter(p=>p.length!=0)

let Data = rawText.map(p=>p.split('+|+')).map(p=>[p[0],Number(p[1]),p[2]=Number(p[2])])

  

// 表格元素

let rank = (data,i)=>{

let com = table.createEl('div')

let title = Data[i][0]

let plan = com.createEl('span',{'text':Data[i][1]+'/'+Data[i][2]})

let progress = com.createEl('progress')

changePro(progress,Data[i][1]/Data[i][2],com)

progress.value = Data[i][1]

progress.max = Data[i][2]

  

let button = com.createEl('div',)

let btn_p = button.createEl('button',{'text':'+'})

let btn_s = button.createEl('button',{'text':'-'})

btn_p.addEventListener('click',async (evt)=> {

midifyData(i,'p')

progress.value = Data[i][1]

changePro(progress,Data[i][1]/Data[i][2],com)

plan.innerHTML = Data[i][1]+'/'+Data[i][2]

})

btn_s.addEventListener('click',async (evt)=> {

midifyData(i,'s')

progress.value = Data[i][1]

changePro(progress,Data[i][1]/Data[i][2],com)

plan.innerHTML = Data[i][1]+'/'+Data[i][2]

})

return [title,plan,progress,button]

}

  

// 表格本体

let table = container.createEl("div");

let headers = ['标题','进度','进度条','修改']

let values = Data.map((p,i)=>rank(p,i))

createTable(headers,values,table)

  

// 保存按钮

let button_ = container.createEl('div',{'id':'con'})

let btn_save = button_.createEl('button',{'text':'save'})

btn_save.addEventListener('click',async (evt)=> {

evt.preventDefault()

let data = '\n'+Data.map(p=>p.join('+|+')).join('\n')+'\n'

content = content.replace(regexp,data)

app.vault.modify(af,content)

})

  

// 排序

let sortOptions = ['名称 A-Z','名称 Z-A','百分比-正序','百分比-倒序']

let sortFun = [

(a,b)=>dv.compare(a[0],b[0]),

(a,b)=>dv.compare(b[0],a[0]),

(a,b)=>dv.compare(b[1]/b[2],a[1]/a[2]),

(a,b)=>dv.compare(a[1]/a[2],b[1]/b[2]),

]

let se = button_.createEl('select')

let op = sortOptions.map(p=>se.createEl('option',{'text':p}))

se.onchange = function() {

let index = se.selectedIndex

table.empty()

Data = Data.sort(sortFun[index])

createTable(

headers,

Data.map((p,i)=>rank(p,i)),

table)

}

  

// 其他函数

function createTable(headers,values,t) {

dv.table(headers,values)

t.appendChild(container.getElementsByTagName('table')[0])

}

function changePro(progress, p, com) {

if(p>=0 && p<0.3) progress.className = 'red'

else if(p>=0.3 && p<0.6) progress.className = 'yellow'

else if(p>=0.6 && p<1) progress.className = 'green'

else if(p==1) progress.className = 'ok'

  

}

// 修改函数

function midifyData(i,m) {

if(Data[i][1]<Data[i][2] && m=='p') Data[i][1] += 1

if(Data[i][1]>0 && m=='s') Data[i][1] -= 1

}

```

  
%%
高数 - 曲线曲面积分+|+12+|+12
电路原理+|+188+|+259
%%


## QuickAdd
***
1. 问答式笔记
```
### 行为疗法{{DATE:YYYYMMDDHHmm}} 
- 你有什么感觉？ 
- {{VALUE:你有什么感觉？}} 
- 现在你脑海中在想什么？ 
- {{VALUE:现在你脑海中在想什么？}} 
- 它真实吗？ 
- {{VALUE:它真实吗？}} 
- 我在思考，不一定意味着这是事实。
```

## 分栏
**方法 1：用 css**
> [!multi-column]
>
>> [!note]+ 第一列
>> 内容
>
>> [!note]+ 第二列
>> 内容
>
>> [!note]+ 第三列
>> 内容
>

**方法 2：用 multi-col 插件**
```start-multi-column
ID: ID_9cl9
Number of Columns: 3
Largest Column: standard
```
### 第一列
内容

--- column-end ---

### 第二列
内容
--- column-end ---

### 第三列
内容

=== end-multi-column


## 表格
***
合并单元格
-tx-
表格需要合并的，不要有空格



# Notion
***

## 文字编辑

|Windows 快捷键|Mac 快捷键|功能|
|---|---|---|
|ctrl + B|⌘ + B|选中文字加粗|
|ctrl + I|⌘ + I|选中文字变斜体|
|ctrl + U|⌘ + U|选中文字加下划线|
|ctrl + shift + S|⌘ + shift + S|选中文字加删除线|
|ctrl + K|⌘ + K|选中文字添加链接|
|ctrl + V|⌘ + V|选中文字粘贴超链接|
|ctrl + E|⌘ + E|选中文字变成代码格式|
|tab|tab|为选中内容/block添加缩进|
|shift + tab|shift + tab|为选中内容/block取消缩进|
|/turn|/turn|在block的开头或结尾插入。改变block的类型。|
|/color/color background|/color/color background|在block的开头或结尾插入。改变block的字体或背景颜色。|
|/default|/default|在block的开头或结尾插入。移除字体或背景颜色。|


## 新建内容

|Windows快捷键|Mac快捷键|功能|
|---|---|---|
|enter|enter|在block内插入新行|
|shift + enter|shift + enter|插入一个新的文字block|
|ctrl + shift + M|⌘ + shift + M|新建一个评论|
|—|—|在新行输入—可创建分隔符|
|ctrl + shift + 0|⌘ + option + 0|新建文字内容|
|ctrl + shift + 1|⌘ + option + 1|新建H1标题|
|ctrl + shift + 2|⌘ + option + 2|新建H2标题|
|ctrl + shift + 3|⌘ + option + 3|新建H3标题|
|ctrl + shift + 4|⌘ + option + 4|新建勾选框|
|ctrl + shift + 5|⌘ + option + 5|新建无序列表|
|ctrl + shift + 6|⌘ + option + 6|新建有序列表|
|ctrl + shift + 7|⌘ + option + 7|新建折叠列表（Toggle List）|
|ctrl + shift + 8|⌘ + option + 8|新建代码块|
|ctrl + shift + 9|⌘ + option + 9|新建页面，或将当前行内容转换为页面|
|ctrl + +|⌘ + +|放大|
|ctrl + –|⌘ + –|缩小|
|ctrl + shift + U|⌘ + shift + U|返回导航条上一级页面|
|alt|option|按住并拖放，克隆页面中的任意内容|

## 移动或编辑内容块 （Block）

|Windows快捷键|Mac快捷键|功能|
|---|---|---|
|esc|esc|选中当前正在编辑的Block再按一次取消选中|
|ctrl + a|⌘ + a|全选当前Block的内容|
|space|space|打开当前选中的图片|
|方向键|方向键|选择不同的block|
|shift + ↑/↓|shift + ↑/↓|选中光标前方或后方内容|
|alt + shift + click|⌘ + shift + click|同时选中多个block|
|shift + click|shift + click|选中另一个block，并将它与当前block之间的block全部选中|
|Backspace/Delete|Backspace/Delete|删除选中的block|
|ctrl + D|⌘ + D|复制当前或选中的block|
|ctrl + /|⌘ + /|修改block样式，输入color、turn into可以修改block的颜色和类型|
|ctrl + shift + 方向键|⌘ + shift + 方向键|移动block的位置|
|ctrl + alt + T|⌘ + option + T|折叠或展开折叠块(Toggle List)|
|ctrl + shift + H|⌘ + shift + H|高亮选中文字|
|ctrl + enter|⌘ + enter|多功能热键：打开一个页面链接勾选/取消勾选展开/折叠当前折叠块全屏显示图片|

## "@"命令：提示和提醒

|命令|功能|
|---|---|
|@[member’s name]|输入@和团队成员的名字，可以提醒或通知该成员|
|@[page’s name]|输入@和页面标题，可以插入该页面的链接|
|@[date]|输入@和任意格式的日期，或’today’/’yesterday’/’tomorrow’等，在输入截止日时很有用|
|@remind[date]|输入@remind和任意格式时间，你可以在该指定时间收到notion的通知|

**注：如果你只想打出@这个符号，按esc可以取消@菜单**

## `[[`命令：页面链接

|命令|功能|
|---|---|
| `[[` |输入`[[`和另一个页面的标题，可以插入该页面的链接|
|`[[`|输入`[[`和你想要的任意名字，配合方向键点击+ Add new sub-page 可以在当前页面新建一个sub-page|
|`[[`|输入`[[`和你想要的任意名字，配合方向键点击↗︎ Add new page in…可以在其他页面或database新建一个sub-page|

## "+"命令：新建页面

|命令|功能|
|---|---|
|+|输入+和任意名称，配合方向键点击+ Add new sub-page 可以在当前页面新建一个sub-page|
|+|输入+和任意名称，配合方向键点击↗︎ Add new page in…可以在其他页面或database新建一个sub-page|
|+|输入+和另一个页面的标题，可以插入该页面的链接|

注意：`[[`命令侧重于插入页面链接功能，+命令侧重新建页面功能。

##  "/"命令

### 基础"/"命令

|命令|功能|
|---|---|
|/|输入/命令会弹出Block菜单，配合方向键可新建任意类型的内容块|
|/text 或 /plain|新建文字内容块text block|
|/page|新建页面page（回车后自动打开该页面）|
|/bullet|新建无序列表|
|/num|新建有序列表|
|/todo|新建待办事项和复选框|
|/toggle|新建折叠内容块（可折叠/展开）|
|/div|新建分隔符|
|/quote|新建引用内容块|
|/h1 或 /#|新建h1标题|
|/h2 或 /##|新建h2标题|
|/h3 或 /###|新建h3标题|
|/link|新建页面链接page link|
|esc|如果只想输入/，可以按esc退出菜单|

### 行内 "/"命令

|命令|功能|
|---|---|
|/mention|提示团队中的某位成员，或者提示某个页面|
|/date 或 /reminder|添加时间戳或时间提示|
|/equation|添加TeX格式的公式|
|/emoji|添加emoji表情|

### 数据视图"/"命令

|命令|功能|
|---|---|
|/table-inline|新建行内普通表格|
|/database-inline|新建行内Database数据库表格|
|/board-inline|新建行内卡片（board）|
|/calendar-inline|新建行内日历|
|/list-inline|新建行内页面列表（list）|
|/gallery-inline|新建行内画廊数据表（gallery）|
|/timeline-inline|新建时间线数据表|
|/linked|在当前页面引用database数据表|

**注：以上命令中的-inline都可以替换为-full，替换后新建的对象都以Page的形式打开。如: /table-full, /board-full**

### 媒体"/"命令

|命令|功能|
|---|---|
|/image|插入图片|
|/pdf|插入pdf|
|/book|插入网页链接并保存为书签|
|/video|插入视频|
|/audio|插入音频|
|/code|插入代码块|
|/file|插入文档|
|/embed|插入各种外部文件（500+种格式可选）|

### 高级"/"命令

|命令|功能|
|---|---|
|/comment|在当前block插入评论|
|/duplicate|复制当前block|
|/moveto|将当前block移动到其他页面|
|/delete|删除当前块|
|/toc|插入目录|
|/button 或 /template|插入按钮|
|/bread|插入面包屑导航条|
|/math 或 /latex|插入数学公式|

## Markdown 语法

### 使用 Markdown 编辑文本格式

|命令|功能|
|---|---|
| `** 内容 **` |加粗，只适用于Text内容块|
|`_内容_` 或 `_内容_`|斜体，只适用于Text内容块|
|`内容`|把内容转换为高亮代码格式，只适用于Text内容块|
|`~内容~`|给内容增加删除线，只适用于Text内容块|

### 使用 Markdown 插入新内容块

|命令|功能|
|---|---|
|– + space|插入无序列表|
|[] + space|插入复选框|
|1. 或 a. 或 i. + space|插入有序列表|
|# + space|插入h1标题|
|## + space|插入h2标题|
|### + space|插入h3标题|
|> + space|插入折叠内容块（Toggle）|
|” + space|插入引用内容块（Quote）|


tags: #LUT 


---
cssclass: academia, wideTable, kanban
---
```dataviewjs
const time = new Date()
let today = moment(time).format('YYYY-MM-DD-dddd')
let ftMd = dv.pages("").file.sort(t=>t.cday)[0]
let total = parseInt([new Date() - ftMd.ctime]/(60*60*24*1000))

dv.paragraph(
  "## 今天是："+today +" " + '你已使用 '+total+' 天：' 
);

```

- **LUT**
    -  [[windows|win快捷键]]
    - [[obsidian]]
    - [[markdown statement|markdown]]
    - [[linux statement|linux命令]]
    - [[inspur cluster|实验室集群]]
    - [[按钮模板]]
- **快速导航**
    - [[40-Research/Home|HOME页]]
    - [[HPE note]]
    - [[日记快速到达指南]]

- **笔记**
    - `button-daily`
    - `button-bibnotes`
    - `button-feedly`
    - `button-cver`

- **动作**
    - `button-capture`
    - `button-lock`

## 最近编辑
```dataview
table WITHOUT ID file.link AS "标题", dateformat(file.mtime, "yyyy-MM-dd HH:MM") as "时间", file.path AS "路径"
from !"kanban" and !"Home"
where !contains(file.name,"Day Planner")
sort file.mtime desc
limit 5
```

## 还没写完的
```dataview
table WITHOUT ID file.link AS "标题", file.path AS "路径"
from #Todo
```




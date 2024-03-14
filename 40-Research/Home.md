---
cssclass: academia, wideTable
---
# 科研
***
## 组会记录
```dataview
TABLE WITHOUT ID file.link AS "Time", Date, Presenter, DESC
FROM #组会 
WHERE file.name != "会议模板"
SORT file.ctime
```  
## 论文笔记
```dataview
TABLE WITHOUT ID file.link AS "Title", Authors,Date, Topics, Keywords
FROM #论文笔记 
WHERE file.name != "Mdnotes Default Template"
SORT Topics
SORT Date DESC
```

## 实验
```dataview
TABLE file.mtime AS "修改时间" 
FROM #实验 
WHERE file.name != "Mdnotes Default Template"
SORT Topics
SORT Date DESC
```